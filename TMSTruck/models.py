from django.db import models
from django.contrib.auth.models import User





def w9UploadFile(instance, filename):
    return 'Users NDA NCA W9 Files/{0}{1}/{2}'.format(instance.firstName,instance.lastName, filename)


class Account(models.Model):
	user 					= models.OneToOneField(User, on_delete=models.CASCADE)
	choices 				= [('ACTIVE','ACTIVE'),('INACTIVE','INACTIVE')]
	Email					= models.EmailField(max_length=100,null=True)
	firstName    			= models.CharField(max_length=100,null=True)
	lastName 				= models.CharField(max_length=100,null=True)
	commissionRate 			= models.IntegerField(null=True)
	address 				= models.CharField(max_length=100,null=True)
	city 					= models.CharField(max_length=100,null=True)
	state 					= models.CharField(max_length=100,null=True)
	zipCode 				= models.IntegerField(null=True)
	Phone 					= models.IntegerField(null=True)
	userStatus 				= models.CharField(max_length=100,choices=choices,default='ACTIVE')
	enrolledCarriers 		= models.TextField(null=True,max_length=3000)    
	ndaNca 					= models.FileField(upload_to=w9UploadFile)
	w9_upload				= models.FileField(upload_to=w9UploadFile,null=True)

	def __str__(self):
		return self.firstName

def carrierMcFiles(instance, filename):
    return 'Carrier MC/{0}{1}/{2}'.format(instance.firstName,instance.lastName, filename)



class Carrier(models.Model):
	user					= models.ForeignKey(Account,on_delete=models.CASCADE,null=True,blank=True)
	firstName 				= models.CharField(max_length=100,null=True)
	lastName				= models.CharField(max_length=100,null=True)
	company 				= models.CharField(max_length=100,null=True)
	email					= models.EmailField(max_length=100,null=True)
	phone					= models.IntegerField(null=True)				
	mc_number 				= models.IntegerField(null=True)
	dot_number				= models.IntegerField(null=True)
	factoring_phone			= models.IntegerField(null=True)
	willing_states			= models.TextField(max_length=1000,null=True)
	carrier_status			= models.CharField(max_length=100,null=True)
	factoring_company		= models.CharField(max_length=100,null=True)
	mc_upload		 		= models.FileField(upload_to=carrierMcFiles,null=True)
	costPerMile				= models.IntegerField(null=True)


	def __str__(self):
		return '{} {}'.format(self.firstName,self.lastName)



def rate_confirmation_path(instance, filename):
    return 'LoadInformations/{0}/{1}/{2}/rate_of_confirmation/{3}'.format(instance.assignToCarrier,instance.broker_name,instance.load_number, filename)


def bill_path(instance, filename):
    return 'LoadInformations/{0}/{1}/{2}/bill_of_lading/{3}'.format(instance.assignToCarrier,instance.broker_name,instance.load_number, filename)


class AssignLoad(models.Model):
	user 					= models.ForeignKey(Account,on_delete=models.CASCADE,null=True,blank=True)
	brokerage_name 			= models.CharField(max_length=300, null=True)
	broker_name 			= models.CharField(max_length=300, null=True)
	assignToCarrier			= models.ForeignKey(Carrier,blank=True, on_delete=models.CASCADE, null=True)
	broker_address 			= models.CharField(max_length=300, null=True)
	pickupAddress 			= models.CharField(max_length=300, null=True)
	distance 				= models.IntegerField(null=True)
	weight 					= models.IntegerField(null=True)
	rate 					= models.IntegerField(null=True)
	stops 					= models.IntegerField(null=True)
	assigned_date			= models.DateTimeField(blank=True,auto_now_add=True, null=True)
	pickupDate				= models.CharField(max_length=3000,null=True, blank=True)
	is_active 				= models.BooleanField(default=True,null=True)
	is_paid 				= models.BooleanField(default=False,null=True)
	broker_phone			= models.IntegerField(null=True)
	broker_email			= models.EmailField(max_length=100,null=True)
	load_number				= models.IntegerField(null=True)
	dropOffDate				= models.CharField(max_length=3000,null=True,blank=True)	
	dropOffAddress			= models.CharField(max_length=10000,null=True)		
	first_available_pickup	= models.CharField(max_length=3000,null=True,blank=True)
	rate_confirmation		= models.FileField(blank=True,upload_to=rate_confirmation_path)
	bill_of_landing			= models.FileField(blank=True,upload_to=bill_path)
	special_comments 		= models.TextField(null=True,max_length=10000)
	final_address			= models.CharField(null=True,max_length=100, blank=True)
	is_awaiting				= models.BooleanField(null=True,default=True,blank=True)
	is_awb					= models.BooleanField(null=True,default=True,blank=True)
	def __str__(self):
		return self.broker_name





class Equipment(models.Model):
	user 					= models.ForeignKey(Carrier, on_delete=models.CASCADE)
	type 					= models.CharField(max_length=100,null=True)
	truck_number 			= models.IntegerField(null=True)
	size					= models.IntegerField(null=True)
	max_weight				= models.IntegerField(null=True)
	license_plate_number	= models.CharField(max_length=200,null=True)


	def __str__(self):
		return self.type




