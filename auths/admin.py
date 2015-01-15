"""
-------------------------------------------------------------------------
	Author: Dadaso Zanzane

	git clone https://github.com/dadasoz-cuelogic/blog-app.git 
--------------------------------------------------------------------------

"""
from django.contrib import admin
from auths.models import Registration

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    fieldsets = [("Blog Users",{'fields': ['first_name','last_name','email','mobile','password']})]
    list_display = ['first_name','email']

admin.site.register(Registration, UserAdmin)