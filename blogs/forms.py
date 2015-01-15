"""
-------------------------------------------------------------------------
	Author: Dadaso Zanzane

	git clone https://github.com/dadasoz-cuelogic/blog-app.git 
--------------------------------------------------------------------------

"""
from django.db import models
from blogs.models import Blogs
from django import forms
from captcha.fields import ReCaptchaField
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blogs
		exclude = ('updated', 'created')   
		fields = ('blog_title','blog_contents' )  
		widget = CKEditorWidget(config_name='awesome_ckeditor')  

	blog_title = forms.CharField(label='Title', max_length=50, required=False)
	blog_contents = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'),required=False)
	#captcha = ReCaptchaField()

	def __init__(self, *args, **kwargs):
		super(BlogForm, self).__init__(*args, **kwargs)
		self.fields['blog_title'].widget.attrs.update({'placeholder': 'Title','class': 'text-field'})
		self.fields['blog_contents'].widget.attrs.update({'placeholder': 'write your contents here','class': 'text-area'})
