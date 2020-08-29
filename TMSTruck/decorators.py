from django.http import HttpResponse
from django.shortcuts import redirect



def login_restrict(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard")

        else:
            return view_func(request,*args,**kwargs)

    return wrapper_func




def admin_only(view_func):
    def restrict_func(request,*args,**kwargs):

        group = None
        if request.user.groups.exists():

            group = request.user.groups.all()[0].name
        if group == 'Trainee':
            return redirect("user")

        elif group == 'Admin':
            return view_func(request,*args,**kwargs)

    return restrict_func


def user_only(view_func):
    def restrict_func(request,*args,**kwargs):

        group = None
        if request.user.groups.exists():

            group = request.user.groups.all()[0].name
        if group == 'Trainee':
            return view_func(request, *args, **kwargs)

        elif group == 'Admin':
            return redirect("dashboard")

    return restrict_func



def customRoles(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)

            elif group == 'Trainee':
                return redirect("user")

            else:
                return HttpResponse("You are not authorized to visit this page. ")


        return wrapper

    return decorator