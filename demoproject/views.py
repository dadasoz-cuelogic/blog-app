from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from captcha.fields import ReCaptchaField
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect


data={}

data.update({"login":""})

def loginDetails(request):
    if request.session.get('login'):
	data.update({"login":request.session['login']})
    else:
        return redirect('/login')

def news(request):

    loginDetails(request)

    data["view_name"] = "news"

    response = TemplateResponse(request, 'tpl1/news.html', data)   

    return response

def contact(request):

	loginDetails(request)

	data["view_name"] = "contact"

	response = TemplateResponse(request, 'tpl1/contact.html', data)

	return response
