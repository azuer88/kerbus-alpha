from django.shortcuts import render, render_to_response
from django.template import RequestContext

from common.utils import render_to

# Create your views here.
def redirect_page_not_found(request):
    data = {
              "title": "Page not Found Error",
              "content": "<h1>Oops!</h1>"
           }
    return render_to_response('error.html', 
              data, 
              context_instance=RequestContext(request))


@render_to('error.html')
def my404handler(request):
    return {
       "title": "Page Not Found",
       "content": "<h1>Ooops!</h1>",
    }


