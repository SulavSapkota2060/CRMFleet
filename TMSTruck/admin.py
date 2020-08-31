from django.contrib import admin
from .models import Account, AssignLoad, Carrier

# Register your models here.

class Loads(admin.ModelAdmin):
    list_display = ('load_number','user','broker_name','assignToCarrier','dropOffDate')


admin.site.register(Account)
admin.site.register(AssignLoad,Loads)
admin.site.register(Carrier)