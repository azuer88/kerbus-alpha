from django.conf.urls import url

from views import my404handler

urlpatterns = [
     url(r'^', my404handler, name='error_handling'),
]
