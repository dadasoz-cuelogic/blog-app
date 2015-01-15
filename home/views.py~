# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
 
def index(request):
    if request.method == 'GET':
    	print "Get"
    elif request.method == 'POST':
    	some_view(request)
    return render_to_response('home/index.html', context_instance=RequestContext(request))

def some_view(request):    
	print request.POST

#def index(request):
#    return render_to_response('home/index.html')
