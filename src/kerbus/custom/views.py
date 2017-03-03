from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.template import loader 

from common.utils import render_to

# Create your views here.
def _page_not_found(request):
    t = loader.get_template('error.html')
    data = {
              "title": "Page not Found Error",
              "content":  {
                  "title": "Oops!",
                  "message": "Oh, no!!!!  You broke the internet!"
              }
           }
    return HttpResponseNotFound(t.render(data, request),
             content_type='text/html')


@render_to('error.html')
def _my404handler(request):
    return {
       "title": "Page Not Found",
       "content": "<h1>Ooops!</h1>",
    }


def my404handler(request):
    return _page_not_found(request)
