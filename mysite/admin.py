from django.contrib import admin
from .models import Info, Profile , Category,pro,GeeksModel

from django.contrib.auth.models import User

from django.contrib.auth.admin import UserAdmin




class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'


# Register your models here.



class CustomizeUserAdmin (UserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)

admin.site.register(User,CustomizeUserAdmin )

admin.site.register(Info)
admin.site.register(Category)

admin.site.register(pro)
admin.site.register(GeeksModel)

