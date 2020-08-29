from django.forms import ModelForm
from .models import *
from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm



class CreateUser(UserCreationForm):

    class Meta:
        model=User
        fields = ['username','email','password1','password2']



class profileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []


        

class UserRegistrationForm(ModelForm):
    
    class Meta:
        model=Account
        fields = "__all__"
        exclude = ['user','Email']






class AssignLoadForm(ModelForm):
    class Meta:
        model=AssignLoad
        fields = '__all__'
        exclude = ['is_active','is_paid']



class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'
        exclude = ['user']




class CarrierForm(ModelForm):
    class Meta:
        model = Carrier
        fields = '__all__'