"""
-------------------------------------------------------------------------
	Author: Dadaso Zanzane

	git clone https://github.com/dadasoz-cuelogic/blog-app.git 
--------------------------------------------------------------------------

"""
from django.db import models
from auths.models import Registration
# Create your models here.
class Blogs(models.Model):
	user_id=models.ForeignKey(Registration)
	pub_date=models.DateField()
	blog_title=models.CharField(max_length=100)
	blog_contents=models.TextField(max_length=100)