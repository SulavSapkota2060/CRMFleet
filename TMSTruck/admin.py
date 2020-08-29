from django.contrib import admin
from .models import Account, AssignLoad, Carrier

# Register your models here.


admin.site.register(Account)
admin.site.register(AssignLoad)
admin.site.register(Carrier)