from django.contrib import admin
from blogs.models import Blogs
from auths.models import Registration
from django.db import models

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_title','pub_date','first_name']
    def first_name(self, obj):
    	return obj.user_id.first_name
    first_name.short_description = 'Author'

admin.site.register(Blogs, BlogAdmin)