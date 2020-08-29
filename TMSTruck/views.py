#Importing necessary libraries
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import login_restrict, admin_only, user_only, customRoles
from django.contrib.auth.models import Group,User
from .models import Account, AssignLoad, Equipment
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
import os
import json
from datetime import date, timedelta, datetime  
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import re

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

#Landing Page View
def index(request):
	template ='TMSTruck/index.html'
	context ={

	}
	return render(request,template,context)


#Signup view
def signup(request):
	message = ''
	UserSignupForm = UserRegistrationForm()
	createUser = CreateUser()
	if request.method == 'POST':
		UserSignupForm = UserRegistrationForm(request.POST,request.FILES)
		createUser = CreateUser(request.POST)
		if UserSignupForm.is_valid() and createUser.is_valid():

			form = createUser.save()
			profile = UserSignupForm.save(commit=False)
			form.first_name = profile.firstName
			form.last_name = profile.lastName
			group = Group.objects.get(name='Trainee')
			form.groups.add(group) 
			
			template = render_to_string('TMSTruck/email_templates/register_template.html',{'firstname':profile.firstName,'lastname':profile.lastName,'form':form,'username':form.username,'password':form.password})			
			
			email = EmailMessage(
				'Account Verified Successfully!!!',
				template,
				settings.EMAIL_HOST_USER,
				[form.email],
				
		)
			email.fail_silently=False
			email.send()

			
			profile.user = form
			profile.Email = form.email
			form.save()
			profile.save()
			return redirect("login")

		else:
			message=  'Please fill all fields'
		


	template ='TMSTruck/signup.html'
	context= {
		"actual_form": createUser,
		"form":UserSignupForm,
		'message':message
	}
	return render(request,template,context)





#Login View
def login_view(request):
	user = request.user
	if user.is_authenticated: 
		return redirect("dashboard")

	if request.POST:
		username= request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request,username = username,password =password)
		if user:
			login(request, user)
			return redirect("dashboard")
	return render(request, "TMSTruck/login.html")





#Dashboard View
@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def dashboard(request):
	user= request.user
	ac = Account.objects.get(user=user)
	print(ac)
	activeLoads  = AssignLoad.objects.filter(user=ac,is_active=True, is_awaiting=False, is_awb=False)
	unpaidLoads = AssignLoad.objects.filter(user=ac,is_active=False,is_paid=False, is_awaiting=False, is_awb=False)
	username = request.user.username

	def profit(completedLoads,Commission):
		total_price = 0
		for i in completedLoads:
			total_price += i.rate
			print(i.rate)
		print(total_price)
		profit = (total_price*0.1)*(Commission/100)
		return profit
	loadsCount = {
		'sevenLoads':AssignLoad.objects.filter(user=ac,is_active=False,assigned_date__range=[datetime.now()-timedelta(days=7),datetime.now()]),
		'thirtyLoads': AssignLoad.objects.filter(user=ac,is_active=False,assigned_date__range=[datetime.now()-timedelta(days=30),datetime.now()]),
		'yearLoads':AssignLoad.objects.filter(user=ac,is_active=False,assigned_date__range=[datetime.now()-timedelta(days=365),datetime.now()]),
		'customLoads':0
	}
	profits = {
		'sevenDayProfit':profit(AssignLoad.objects.filter(user=ac,is_active=False,assigned_date__range=[datetime.now()-timedelta(days=7),datetime.now()]),ac.commissionRate),
		'thirtyDayProfit':profit(AssignLoad.objects.filter(user=ac,is_active=False,assigned_date__range=[datetime.now()-timedelta(days=7),datetime.now()]),ac.commissionRate),
		'oneYearProfit':profit(AssignLoad.objects.filter(user=ac,is_active=False,assigned_date__range=[datetime.now()-timedelta(days=7),datetime.now()]),ac.commissionRate),
		'customProfit':0
	}
	

	group = request.user.groups.all()[0].name
	context = {
		'username':username,
		'activeLoads':activeLoads,
		'unpaidLoads':unpaidLoads,
		'group':group,
		'loadsCount':loadsCount,
		'profits':profits

	}

	if request.method== 'POST':
		date_to = request.POST.get('Dateto')
		date_from = request.POST.get('Datefrom')
		loadsCount['customLoads'] = AssignLoad.objects.filter(user=ac,is_active=False,is_awaiting=False,is_awb=False,assigned_date__range=[date_from,date_to]).count()
		profits['customProfit'] = profit(AssignLoad.objects.filter(user=ac,is_active=False,assigned_date__range=[date_from,date_to]),ac.commissionRate),
		con = str(profits['customProfit'])[1:-2]
		context['con'] = con
		return render(request,'TMSTruck/dashboard.html',context)
	return render(request,'TMSTruck/dashboard.html',context)




#Logout View
def logout_user(request):
	logout(request)
	return redirect("login")



#Lists all the carriers
@login_required(login_url="login")
@customRoles(allowed_roles=['Admin'])
def all_workers(request):
	workers = Account.objects.all().order_by('-id')
	template = 'TMSTruck/all_workers.html'
	context = {
		'workers':workers
	}
	return render(request,template,context)



#Summary data




#Assign a load to the Carrier
@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def assign_load(request):
	template = 'TMSTruck/load_assignMent.html'
	form = AssignLoadForm()
	group = request.user.groups.all()[0].name
	ac = Account.objects.get(user=request.user)
	print(ac)
	carrier = Carrier.objects.filter(user=ac)
	print(carrier)
	context = {
		'form':form,
		'group':group,
		'carrier':carrier,
		}
	
	if request.method == 'POST':

		form = AssignLoadForm(request.POST,request.FILES)
		# accessing account objects
		
		account = Carrier.objects.filter(user=ac	)
		#assigning values to form manually
		a = form.save(commit=False)


		#parsing drop off data to form

		dropadd = json.loads(a.dropOffAddress)
		a.user = ac
		a.final_address = dropadd["stopAddresses"][-1]
		a.pickupDate = request.POST.get("pickupDate")
		a.dropOffDate = request.POST.get("dropOffDate")
		ac = request.POST.get("carrier")
		a.first_available_pickup = request.POST.get("first_available_pickup")
		print(ac)
		print(account.count())
		#matching accurate account instance to be filled in the form
		for i in account:
			fullName = '{} {}'.format(i.firstName,i.lastName)
			print(fullName)
			if ac == fullName:
				
				a.assignToCarrier = i
			print(a.assignToCarrier)
		
		#validating form
		if form.is_valid():

			a = form.save(commit=False)
			ca = Carrier.objects.get(id=a.assignToCarrier.id)
			j = json.loads(a.dropOffAddress)
			ad = j["stopAddresses"]
			address_list = []
			for i in ad:
				address_list.append(i)
			template = render_to_string('TMSTruck/email_templates/email_template.html',{'firstname':ca.firstName,'lastname':ca.lastName,'form':form,'address':address_list})			
			rate = request.FILES['rate_confirmation']

			#setting up email form
			email = EmailMessage(
				'New Order Assigned!!',
				template,
				settings.EMAIL_HOST_USER,
				[ca.email],
				
		)
			email.attach(rate.name, rate.read(), rate.content_type)
			email.fail_silently = False
			email.send()
			print("Email Sent")
			form.save()
			return redirect("awaiting_loads")
		else:
			print("Error")
			messages.error(request,'Error ')

	return render(request,template,context)




# Displays a carrier detail
@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def user_detail(request,pk):
	user = Carrier.objects.get(id=pk)
	completed_loads = AssignLoad.objects.filter(assignToCarrier=user,is_active=False)
	active_loads = AssignLoad.objects.filter(assignToCarrier=user,is_active=True,is_awaiting=False,is_awb=False)
	trucks = Equipment.objects.filter(user=user)
	carrier = Carrier.objects.get(id=pk)
	print(trucks)
	template = 'TMSTruck/user_detail.html'
	context = {
		'user':user,
		'carrier':carrier,
		'active_loads':active_loads,
		'completed_loads':completed_loads,
		'trucks':trucks,
		'group':request.user.groups.all()[0].name
	}

	return render(request,template,context)



@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager','Trainee'])
def user_info(request):
	user=request.user
	account = Account.objects.get(user=request.user)

	template = 'TMSTruck/user_info.html'
	context = {
		'user':user,
		'account':account,
		'group':request.user.groups.all()[0].name
	}
	return render(request,template,context)


@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager','Trainee'])
def change_password(request):
    form = PasswordChangeForm(request.user)
	
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
	    
    return render(request, 'TMSTruck/change_password.html', {
        'form': form,
		'group':request.user.groups.all()[0].name
    })




#Carrier Dashboard -- Might be removed
@login_required(login_url='login')
@user_only
def user(request):
	user = request.user
	account = Account.objects.get(user=user)
	group = user.groups.all()[0].name
	template = 'TMSTruck/user_profile.html'
	context = {
		'account':account,
		'group':group,
	}
	return render(request,template,context)




# Profile page
@login_required(login_url='login')
@user_only
def myProfile(request):
	template = 'TMSTruck/user_MyProfile.html'
	user = request.user
	account = Account.objects.get(user=user)
	completed_loads = AssignLoad.objects.filter(assignToCarrier=account,is_active=False)
	active_loads = AssignLoad.objects.filter(assignToCarrier=account,is_active=True)
	trucks = Equipment.objects.filter(user=account)
	print(trucks)
	context = {
		'user':account,
		'active_loads':active_loads,
		'completed_loads':completed_loads,
		'trucks':trucks,
	}
	return render(request,template,context)



#Details of the load
@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
@login_required(login_url='login')
def load_detail(request,pk):
	group = request.user.groups.all()[0].name
	load = AssignLoad.objects.get(id=pk)
	j = json.loads(load.dropOffAddress)
	print(type(j))
	a = j["stopAddresses"]
	template = 'TMSTruck/load_detail.html'
	address_list = []
	print(j)
	for i in a:
		address_list.append(i)
		
	context = {
		'load':load,
		'group':group,
		'address':address_list
	}
	return render(request,template,context)



# Equipment details




# Adding equipment
@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def add_equipment(request,pk):
	form = EquipmentForm()
	template = 'TMSTruck/add_equipment.html'
	context = {
		'form':form
	}
	carrier = Carrier.objects.get(id=pk)
	if request.method == 'POST':
		form = EquipmentForm(request.POST)
		if form.is_valid():
			a = form.save(commit=False)
			a.user = carrier
			a.save()
			return redirect("dashboard")
		else:
			print("Nope")
			return redirect("dashboard")
	return render(request,template,context)



#Removing Equipment
@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
@login_required(login_url='login')
def remove_equipment(request,pk):
	equip = Equipment.objects.get(id=pk)
	equip.delete()

	return redirect("all_carrier")


#User's Active loads
@login_required(login_url='login')
def user_active_load(request):
	user = request.user
	account = Account.objects.get(user=user)
	
	active_loads = AssignLoad.objects.filter(assignToCarrier=account,is_active=True)
	template = 'TMSTruck/user_activeLoads.html'
	context = {
		'active_loads':active_loads
	}
	return render(request,template,context)





@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def complete_load(request):
	incomplete_loads = AssignLoad.objects.filter(is_active=True,is_awb=False,is_awaiting=False)
	group = request.user.groups.all()[0].name
	template = 'TMSTruck/load_info/complete.html'
	context = {
		'incomplete_loads':incomplete_loads,
		'group':group
	}

	return render(request,template,context)
	
@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def all_carrier(request):
	acc = Account.objects.get(user=request.user)
	carriers = Carrier.objects.filter(user =acc)
	template = 'TMSTruck/carrier/all_carrier.html'
	group = request.user.groups.all()[0].name
	context = {
		'carriers':carriers,
		'group':group
	}
	return render(request,template,context)

@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def add_carrier(request):
	form = CarrierForm()
	template = 'TMSTruck/add_carrier.html'
	group = request.user.groups.all()[0].name
	context = {
		'form':form,
		'group':group
	}
	if request.method == 'POST':
		form = CarrierForm(request.POST, request.FILES)
		a = form.save(commit=False)
		a.user = Account.objects.get(user=request.user)
		print(a.user)
		if form.is_valid():
			form.save()

		else:
			return HttpResponse("Invalid Form")

	return render(request,template,context)


@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def training_center(request):
	group=request.user.groups.all()[0].name
	template = 'TMSTruck/training/video.html'
	context = {
		'group':group
	}

	return render(request,template,context)


@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting'])
def invoicing(request,pk):
	user = request.user
	carrier = Carrier.objects.get(id=pk)
	loads = AssignLoad.objects.filter(assignToCarrier=carrier,is_active=False,is_paid=False)
	template = 'TMSTruck/carrier/carrier_invoice.html'
	dates = date.today()
	total = 0
	for i in loads:
		total+= i.rate

	invoice_total = total *0.1

	print(invoice_total)
	context = {
		'user':user,
		'carrier':carrier,
		'user_loads':loads,
		'invoice_total':invoice_total,
		'date':dates,
		'send_email':'Email Invoice',
		'button':'Generate Invoice'

	}
	data = {
		'user':user,
		'carrier':carrier,
		'user_loads':loads,
		'invoice_total':invoice_total,
		'date':dates,
	}
	if request.method == 'POST':
		pdf = render_to_pdf('TMSTruck/carrier/carrier_invoice.html', data)
		response = HttpResponse(pdf, content_type='application/pdf')
		filename = 'Invoice{}{}.pdf'.format(carrier.firstName,carrier.lastName)
		content = "attachment; filename={}".format(filename)
		response['Content-Disposition'] = content

		email = EmailMessage(
				'Account Verified Successfully!!!',
				template,
				settings.EMAIL_HOST_USER,
				['docs@jalogisticsusa.com',carrier.email],
				
		)
		email.attach(filename, pdf.getvalue() , 'application/pdf')
		email.fail_silently=False
		email.send()
		print('sent')
	
		return response

	return render(request,template,context)



@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def mark_completed(request,pk):
	
	load = AssignLoad.objects.get(id=pk)
	load_form = AssignLoadForm(instance = load)
	a = load_form.save(commit=False)
	a.is_active = False
	a.save()
	return redirect("dashboard")

@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def mark_paid(request,pk):
	
	load = AssignLoad.objects.get(id=pk)
	load_form = AssignLoadForm(instance = load)
	a = load_form.save(commit=False)
	a.is_paid = True
	
	a.save()
	return redirect("unpaid")


@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def all_loads(request):
	ac = Account.objects.get(user=request.user)
	all_loads = AssignLoad.objects.filter(user=ac,is_awaiting=False, is_awb=False).order_by('-id')
	group = request.user.groups.all()[0].name
	template = 'TMSTruck/load_info/all_loads.html'
	context = {
		'all_loads':all_loads,
		'group':group
	}

	return render(request,template,context)


@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def awaiting_loads(request):
	ac = Account.objects.get(user=request.user)
	awaiting_loads = AssignLoad.objects.filter(user=ac,is_awaiting=True,is_awb=True)
	awb_loads = AssignLoad.objects.filter(user=ac,is_awb=True,is_awaiting=False)
	group = request.user.groups.all()[0].name
	template = 'TMSTruck/load_info/awaiting.html'
	
	context = {
		'awaiting_loads':awaiting_loads,
		'awb':awb_loads,
		'group':group
	}

	return render(request,template,context)



def awaiting_detail(request,pk):	

	if request.method == 'POST':

		form = AssignLoadForm(request.POST,request.FILES)
		# accessing account objects

		account = Carrier.objects.all()

		#assigning values to form manually
		a = form.save(commit=False)
		print('Rate: ',a.rate_confirmation)

		#parsing drop off data to form

		dropadd = json.loads(a.dropOffAddress)

		a.final_address = dropadd["stopAddresses"][-1]
		b = AssignLoad.objects.get(id=pk)
		a.pickupDate = b.pickupDate
		a.dropOffDate = b.dropOffDate
		a.user = b.user
		ac = request.POST.get("carrier")
		a.first_available_pickup = b.first_available_pickup
		print(ac)

		#matching accurate account instance to be filled in the form
		for i in account:
			if ac == i.firstName:
				print(i)
				a.assignToCarrier = i
			
		
		#validating form
		if form.is_valid():
			print("Checking")
			
			a = form.save(commit=False)
			print(a.assignToCarrier)
			ca = Carrier.objects.get(id=a.assignToCarrier.id)
			carrier_detail = {
				'firstName':ca.firstName,
				'lastName':ca.lastName,
				'email':ca.email,
			}
			j = json.loads(a.dropOffAddress)
			ad = j["stopAddresses"]
			address_list = []
			for i in ad:
				address_list.append(i)
			template = render_to_string('TMSTruck/email_templates/broker_template.html',{'carrier':carrier_detail,'form':form,'address':address_list})			
			rate = request.FILES['rate_confirmation']

			#setting up email form
			email = EmailMessage(
				'New Order Assigned!!',
				template,
				settings.EMAIL_HOST_USER,
				[a.broker_email],
				
		)
			email.attach(rate.name, rate.read(), rate.content_type)
			email.fail_silently = False
			email.send()
			a.is_awaiting=False
			
			a.save()	
			AssignLoad.objects.get(id=pk).delete()
	
			print("Email Sent")
			return redirect("awaiting_loads")
		else:
			print("Error")
			messages.error(request,'Error ')

	else:
		template = 'TMSTruck/load_info/awaiting_detail.html'
		load = AssignLoad.objects.get(id=pk)
		form = AssignLoadForm(instance=load)
		group = request.user.groups.all()[0].name
		j = json.loads(load.dropOffAddress)
		a = j["stopAddresses"]
		address_list = []
		for i in a:
			address_list.append(i)
		context = {
			'form':form,
			'group':group,
			'load':load,
			'address':address_list,
			}
	return render(request,template,context)

@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def is_await(request,pk):
	
	load = AssignLoad.objects.get(id=pk)
	load_form = AssignLoadForm(instance = load)
	a = load_form.save(commit=False)
	a.is_awaiting = False
	a.save()
	return redirect("awb",pk=pk)







#-------------------------------------------------------------------------------------------------#
@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def awb(request,pk):	

	if request.method == 'POST':

		form = AssignLoadForm(request.POST,request.FILES)
		# accessing account objects

		account = Carrier.objects.all()

		pre = AssignLoad.objects.get(id=pk)
		#assigning values to form manually
		a = form.save(commit=False)

		a.rate_confirmation = pre.rate_confirmation
		#parsing drop off data to form

		dropadd = json.loads(a.dropOffAddress)

		a.final_address = dropadd["stopAddresses"][-1]
		b = AssignLoad.objects.get(id=pk)
		a.pickupDate = b.pickupDate
		a.user = b.user
		a.dropOffDate = b.dropOffDate
		ac = request.POST.get("carrier")
		a.first_available_pickup = b.first_available_pickup
		print(ac)

		#matching accurate account instance to be filled in the form
		for i in account:
			if ac == i.firstName:
				print(i)
				a.assignToCarrier = i
			
		
		#validating form
		if form.is_valid():
			print("Checking")
			print(a.bill_of_landing)
			
			a = form.save(commit=False)
			print(a.assignToCarrier)
			ca = Carrier.objects.get(id=a.assignToCarrier.id)
			carrier_detail = {
				'firstName':ca.firstName,
				'lastName':ca.lastName,
				'email':ca.email,
			}
			template = render_to_string('TMSTruck/email_templates/broker_template.html',{'carrier':carrier_detail,'form':form})			
			bill = request.FILES['bill_of_landing']
			#setting up email form
			email1 = EmailMessage(
				'Bill Of Lading',
				'Bill',
				settings.EMAIL_HOST_USER,
				[ca.email],
				
		)
			email1.attach(bill.name, bill.read(), bill.content_type)
			email1.fail_silently = False
			email1.send()
			print("Email Sent")
			
			a.is_awb=False
			a.is_awaiting=False
			a.is_active=True
			a.save()
			AssignLoad.objects.get(id=pk).delete()

			return redirect("awaiting_loads")
			
		else:
			print("Error")
			messages.error(request,'Error ')

	else:
		template = 'TMSTruck/load_info/awb_detail.html'
		load = AssignLoad.objects.get(id=pk)
		form = AssignLoadForm(instance=load)
		group = request.user.groups.all()[0].name
		j = json.loads(load.dropOffAddress)
		a = j["stopAddresses"]
		address_list = []
		for i in a:
			address_list.append(i)
		context = {
			'form':form,
			'group':group,
			'load':load,
			'address':address_list,
			}
	return render(request,template,context)

@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def is_awb(request,pk):
	
	load = AssignLoad.objects.get(id=pk)
	load_form = AssignLoadForm(instance = load)
	a = load_form.save(commit=False)
	a.is_awb = False
	a.save()
	return redirect("dashboard")













@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager','Trainee'])
def quiz(request):
	
	if request.method == 'POST':
		try:		
			score = request.POST.get('Myscore','')
			s = float(score)
			if s >=80.0:

				group = Group.objects.get(name='Logistics Manager')
				tr = Group.objects.get(name='Trainee')
				request.user.groups.add(group)
				request.user.groups.remove(tr)
				return redirect("dashboard")

			else:
				return HttpResponse("YOU FAILED :( ")
		except:
			return HttpResponse("Complete the quiz first")
	template = 'TMSTruck/training/quiz.html'
	context = {

	}
	return render(request,template,context)


@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def unpaid_loads(request):
	unpaid_loads = AssignLoad.objects.filter(is_active=False,is_paid=False,is_awb=False,is_awaiting=False)
	template = 'TMSTruck/load_info/unpaid_loads.html'
	group = request.user.groups.all()[0].name
	context = {
		'unpaid_loads':unpaid_loads,
		'group':group
	}
	return render(request,template,context)


@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting'])
def pdf_invoice(request,pk):
	user = request.user
	carrier = Carrier.objects.get(id=pk)
	loads = AssignLoad.objects.filter(assignToCarrier=carrier,is_active=False)
	template = 'TMSTruck/carrier/carrier_invoice.html'
	dates = date.today()
	total = 0
	for i in loads:
		total+= i.rate

	invoice_total = total * 0.1
	print(invoice_total)
	context = {
		'user':user,
		'carrier':carrier,
		'user_loads':loads,
		'invoice_total':invoice_total,
		'date':dates

	}

	pdf = render_to_pdf(template, context)

	return HttpResponse(pdf, content_type='application/pdf')
	



@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting'])
def all_invoice(request):
	ac = Account.objects.get(user=request.user)
	carrier = Carrier.objects.all()
	ca = carrier.values()
	template = 'TMSTruck/carrier/all_invoice.html'
	carrierList = [car for car in carrier]
	all_loads = AssignLoad.objects.filter(user=ac)
	group = request.user.groups.all()[0].name


	print(ca)	

	context = {
		'carriers':carrier,
		'group':group,
		
	}
				
			
	
	return render(request,template,context)





@login_required(login_url="login")
@customRoles(allowed_roles=['Admin'])
def all_users(request):
	template = 'TMSTruck/all_users.html'
	all_user = Account.objects.all()
	context = {
		'all_users':all_user,
		'group':request.user.groups.all()[0].name
	}

	return render(request,template,context)


@login_required(login_url="login")
@customRoles(allowed_roles=['Admin','Accounting','Hiring Manager', 'Logistics Manager'])
def remove_carrier(request,pk):
	Carrier.objects.get(id=pk).delete()

	return redirect("all_carrier")