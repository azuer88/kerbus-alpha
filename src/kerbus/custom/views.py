from django.shortcuts import render

from common.utils import render_to

# Create your views here.
def _page_not_found(request):
    data = {
              "title": "Page not Found Error",
              "content": "<h1>Oops!</h1>"
           }
    return render(request, 'error.html', 
              data) 


@render_to('error.html')
def _my404handler(request):
    return {
       "title": "Page Not Found",
       "content": "<h1>Ooops!</h1>",
    }


def my404handler(request):
    return _page_not_found(request)
