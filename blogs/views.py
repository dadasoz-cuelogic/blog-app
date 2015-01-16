
"""
-------------------------------------------------------------------------
	Author: Dadaso Zanzane

	git clone https://github.com/dadasoz-cuelogic/blog-app.git 
--------------------------------------------------------------------------

"""
from django.shortcuts import get_object_or_404, render_to_response # Imports Error, and render as response
from django.http import HttpResponseRedirect, HttpResponse 
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
from blogs.models import Blogs # Imports Blog Model(for Database class)
from blogs.forms import BlogForm  # Imports Blog Form Class
from auths.models import Registration # For access registration class as foreign key constraints
from django.template.response import TemplateResponse # To generate templete response 
from datetime import datetime # import system datetime
from django.views.generic.edit import UpdateView # Update view for the form class


data={}  # Global Dictionary to store output data as in input for template/its a global includes everything

data.update({"login":"","view_name":"blogs"}) # update the dictionary


# to authenticate the user
def authenticate(func):
    def authenticate_and_call(request,*args, **kwargs):# accept the request object
        if request.session.get('login'): # checks for the session values
            data.update({"login":request.session['login']}) # if session exist add the session values to the main dict
        else:
            return redirect('/login') # if session is not availabe redirect to login
        return func(request,*args, **kwargs) # return function 
    return authenticate_and_call 

# Index view to generate the list of blogs
@authenticate # call the decorator 'authenticate'
def index(request): 
    data["view_name"] = "home"  # set view name for default
    latest_blogs_list = Blogs.objects.all().order_by('-pub_date')[:10] # get the letest 5 blogs order by pub_date descending
    data.update({'latest_blogs_list': latest_blogs_list})# Update the main data dictionary
    return render_to_response('tpl1/blogs.html',  RequestContext(request, data)) # render the template with data and request object

@authenticate # call the decorator 'authenticate'
def blogs(request): # To display list of blogs 
    data["view_name"] = "blogs" # set view name for default
    latest_blogs_list = Blogs.objects.all().order_by('-pub_date')[:10] # get the letest 5 blogs order by pub_date descending
    data.update({'latest_blogs_list': latest_blogs_list}) # Update the main data dictionary
    return render_to_response('tpl1/blogs.html',  RequestContext(request, data)) # render the template with data and request object

@authenticate # call the decorator 'authenticate'
def detail(request, blog_id): #Detail view for blog(Indivisual)
    try:
        blog = Blogs.objects.get(pk=blog_id) # Get is single matching record by id(primary key) column
        data.update({'blog': blog}) # Update the globle dict with data
    except Poll.DoesNotExist: # if record does not exist raise an exception
        raise Http404 # raise the Http404 Not found error
    return render_to_response('tpl1/detail.html', RequestContext(request, data)) # render the template with data and request object

@authenticate # call the decorator 'authenticate'
def saveBlog(request): # Save the blog to database
    blog_title=request.POST["blog_title"] # Get blog title field from request object
    blog_contents=request.POST["blog_contents"]
    user_id=data["login"]["id"] # get the login id form global data dictionary
    reg_obj=Registration.objects.get(id=user_id) # user object to pass foreign key object for user
    blog_obj=Blogs(blog_title=blog_title, blog_contents=blog_contents,user_id=reg_obj,pub_date=datetime.now()); # create the instance of class Model Blog with values
    blog_obj.save() # save the values/ database operations
    return True #return true if not exception

@authenticate # call the decorator 'authenticate'
def create(request): # create new blog
    msg="" # initalize the msg variable to send the extra message to the template
    form = BlogForm(request.POST) # get request
    if request.method == 'GET': # check for form method is "GET"
        print "Get"
    elif request.method == 'POST':  # check for form method is "POST"
       # if form.is_valid():     # Validate the formby using default validators
       saveBlog(request)    # Call the saveBlog method
       msg="Blog saved successfully!"

    data.update({"form":form,"msg":msg}) # Update the global data dictionary

    response = TemplateResponse(request, 'tpl1/createBlog.html', data) # instantiate the response variable with request object and data

    return response # return response

@authenticate # call the decorator 'authenticate'
def myblogs(request): # View the blogs of authenticated users
    data["view_name"]="myblogs" 
    try:
        latest_blogs_list = Blogs.objects.filter(user_id=data["login"]["id"]).order_by('-pub_date')[:10] # get the blogs by user_id 
        data.update({'latest_blogs_list': latest_blogs_list})   # Update the data dict
    except:
        pass
    return render_to_response('tpl1/myBlogs.html',  RequestContext(request, data)) # return response

@authenticate # call the decorator 'authenticate'
def edit(request,blog_id):    
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
