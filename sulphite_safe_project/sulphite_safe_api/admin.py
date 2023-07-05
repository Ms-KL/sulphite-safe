from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Beverage, SulphiteStatus, BeverageSulphiteStatus, UserBeverageSulphiteStatus

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Beverage)
admin.site.register(SulphiteStatus)
admin.site.register(BeverageSulphiteStatus)
admin.site.register(UserBeverageSulphiteStatus)