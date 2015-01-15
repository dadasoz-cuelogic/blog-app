"""
-------------------------------------------------------------------------
	Author: Dadaso Zanzane

	git clone https://github.com/dadasoz-cuelogic/blog-app.git 
--------------------------------------------------------------------------

"""
from django.db import models
from auths.models import Registration
from django import forms
from captcha.fields import ReCaptchaField

class RegistrationForm(forms.Form):
	class Meta:
		model = Registration
		exclude = ('updated', 'created')
        widgets = {
            'password': forms.PasswordInput(),
        }

	first_name = forms.CharField(label='First Name', max_length=50, required=False)
	last_name = forms.CharField(label='Last Name', max_length=50, required=False)
	email = forms.CharField(label='Email', max_length=50, required=True)
	mobile = forms.CharField(label='Mobile', max_length=50, required=False)
	password = forms.CharField(label='Password', max_length=50, required=True,widget=forms.PasswordInput)
	captcha = ReCaptchaField()

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name','class': 'text-field'})
		self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name','class': 'text-field'})
		self.fields['email'].widget.attrs.update({'placeholder': 'Email','class': 'text-field'})
		self.fields['mobile'].widget.attrs.update({'placeholder': 'Mobile','class': 'text-field'})
		self.fields['password'].widget.attrs.update({'placeholder': 'Password','class': 'text-field'})
