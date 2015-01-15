"""
-------------------------------------------------------------------------
    Author: Dadaso Zanzane

    git clone https://github.com/dadasoz-cuelogic/blog-app.git 
--------------------------------------------------------------------------

"""
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
from auths.models import Registration
from auths.forms import RegistrationForm
from django.core.urlresolvers import reverse
from captcha.fields import ReCaptchaField
from django import forms
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string
from django.shortcuts import redirect

# Create your views here.
 
def login(request):
    
    response = TemplateResponse(request, 'tpl1/login.html', {})

    if request.method == 'GET':
    	print "Get"
        retriveAll()
    elif request.method == 'POST':
    	if(validate_login(request)):
            return redirect('/blogs', foo='bar')
        else:
            response = TemplateResponse(request, 'tpl1/login.html', {"msg":"Invalid username or password"})

    return response
    #return render_to_response('tpl1/login.html', context_instance=RequestContext(request))

def sendmail(subject,html_content,sender,recipients):
    msg = EmailMultiAlternatives(subject, '', sender, recipients)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def register(request):       
    msg=""
    form = RegistrationForm(request.POST)
    if request.method == 'GET':
        print "Get"
    elif request.method == 'POST':
	   if form.is_valid():
            if(registerUser(request)==False):
                msg="Already Registred!"
    response = TemplateResponse(request, 'tpl1/registration.html', {'form': form,'msg':msg})
    return response

def validate_login(request):
    user= request.POST["email"]
    passwd = request.POST["password"]
    users=Registration.objects.filter(email = user,password=passwd)
    if len(users) == 1:
        users=users[0]
        request.session['login']={"id":users.id,"name":users.first_name,"email":users.email}
        return True
    else:
        return False

def registerUser(request):
    first_name= request.POST["first_name"]
    last_name= request.POST["last_name"]
    email= request.POST["email"]
    mobile= request.POST["mobile"]
    password = request.POST["password"]
    if Registration.objects.filter(email = email).exists():
        return False
    else:    
        reg_obj=Registration(first_name=first_name, last_name=last_name,email=email,mobile=mobile,password=password);
        reg_obj.save()
        subject = "Blog Registration"
        message = "hello "+first_name+" "+last_name+"""
        <br>
        You are Successfully registered<br>
        <b>Your Email</b>"""+email+"""<br>
        <b>Your Password</b>"""+password+"""<br>
        <br>
        Thanks
        """
        sender = "python.cues@gmail.com"
        recipients = [email]
        headers={'content-type':'text/html'}
        sendmail(subject, message, sender, recipients)
        return True

def retriveAll():
    all_entries = Registration.objects.all()
    print all_entries

def logout(request):
    request.session['login']=""
    if 'login' in request.session:
        del request.session['login']
    return redirect('/login')

    
