
"""
-------------------------------------------------------------------------
	Author: Dadaso Zanzane

	git clone https://github.com/dadasoz-cuelogic/blog-app.git 
--------------------------------------------------------------------------

"""
from django.shortcuts import get_object_or_404, render_to_response #Imports Error, and render as response
from django.http import HttpResponseRedirect, HttpResponse 
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
from blogs.models import Blogs #Imports Blog Model(for Database class)
from blogs.forms import BlogForm  #Imports Blog Form Class
from auths.models import Registration #For access registration class as foreign key constraints
from django.template.response import TemplateResponse #To generate templete response 
from datetime import datetime # import system datetime
from django.views.generic.edit import UpdateView #Update view for the form class


# Create your views here.
data={}  #Global Dictionary to store output data as in input for template/its a global includes everything

data.update({"login":"","view_name":"blogs"}) #update the dictionary


#Login details function which checks for the login sessions and stores to the login as key value
#redirects to login if not loggedin
#requires the request instance
def loginDetails(request):
    if request.session.get('login'):
        data.update({"login":request.session['login']})
    else:
        return redirect('/login/')


#Index view to generate the list of blogs
def index(request):
    if request.session.get('login'):
        data.update({"login":request.session['login']})
    else:
        return redirect('/login/')   #check for login 
    data["view_name"] = "home"  #set view name for default
    latest_blogs_list = Blogs.objects.all().order_by('-pub_date')[:10] #get the letest 5 blogs order by pub_date descending
    data.update({'latest_blogs_list': latest_blogs_list})
    return render_to_response('tpl1/blogs.html',  RequestContext(request, data))

def blogs(request):
    if request.session.get('login'):
        data.update({"login":request.session['login']})
    else:
        return redirect('/login/')
    data["view_name"] = "blogs"
    latest_blogs_list = Blogs.objects.all().order_by('-pub_date')[:10]
    data.update({'latest_blogs_list': latest_blogs_list})
    return render_to_response('tpl1/blogs.html',  RequestContext(request, data))

def detail(request, blog_id):
    loginDetails(request)
    try:
        blog = Blogs.objects.get(pk=blog_id)
        data.update({'blog': blog})
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('tpl1/detail.html', RequestContext(request, data))


def saveBlog(request):
    loginDetails(request)
    blog_title=request.POST["blog_title"]
    blog_contents=request.POST["blog_contents"]
    user_id=data["login"]["id"]
    reg_obj=Registration.objects.get(id=user_id)
    blog_obj=Blogs(blog_title=blog_title, blog_contents=blog_contents,user_id=reg_obj,pub_date=datetime.now());
    blog_obj.save()
    return True

def create(request):
    if request.session.get('login'):
        data.update({"login":request.session['login']})
    else:
        return redirect('/login/')
    loginDetails(request)
    if data["login"]=="":
        return redirect('/login')
    data["view_name"]="create"
    msg=""
    form = BlogForm(request.POST)
    if request.method == 'GET':
        print "Get"
    elif request.method == 'POST':
       # if form.is_valid():
       saveBlog(request)
       msg="Blog saved successfully!"

    data.update({"form":form,"msg":msg})

    response = TemplateResponse(request, 'tpl1/createBlog.html', data)

    return response

def myblogs(request):
    if request.session.get('login'):
        data.update({"login":request.session['login']})
    else:
        return redirect('/login/')
    loginDetails(request)
    data["view_name"]="myblogs"
    try:
        latest_blogs_list = Blogs.objects.filter(user_id=data["login"]["id"]).order_by('-pub_date')[:10]
        data.update({'latest_blogs_list': latest_blogs_list})   
    except:
        return render_to_response('tpl1/login.html',  RequestContext(request, data))
    return render_to_response('tpl1/myBlogs.html',  RequestContext(request, data))

def edit(request,blog_id):
    if request.session.get('login'):
        data.update({"login":request.session['login']})
    else:
        return redirect('/login/')
    loginDetails(request)    
    data["view_name"]="editBlog"
    msg=""
    record = Blogs(id=blog_id)
    form = BlogForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            blog_title=request.POST["blog_title"]
            id=request.POST["id"]
            blog_contents=request.POST["blog_contents"]
            user_id=data["login"]["id"]
            reg_obj=Registration.objects.get(id=user_id)
            blog_form = Blogs(blog_title=blog_title, blog_contents=blog_contents,user_id=reg_obj,pub_date=datetime.now(),id=id)
            blog_form.save()
            msg="Blog saved successfully!"
        else:
            msg="Invalid Security Code!"
    else:
        a=Blogs.objects.get(pk=int(blog_id))
        form = BlogForm(instance=a)
        data.update({"blog_id":blog_id})
    data.update({"blog_id":blog_id})    
    data.update({"form":form,"msg":msg})

    response = TemplateResponse(request, 'tpl1/editBlog.html', data)

    return response

def delete(request,blog_id):
    delete = Blogs.objects.get(pk=blog_id).delete()
    return redirect('/blogs/myblogs/')
