from django.conf.urls import url

import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.snippet_detail, name="snippet_detail"),
    url(r'^', views.snippet_list, name="snippet_list"),
]
