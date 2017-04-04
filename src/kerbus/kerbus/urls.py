"""kerbus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView

import settings

# from api import UserViewSet
# from rest_framework import routers

from custom.views import my404handler

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^error/', include('custom.urls')),
    url('^menu/', include('asimplemenu.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^login', RedirectView.as_view(
        pattern_name='loginindex', permanent=True
    )),
    url(r'^logout', RedirectView.as_view(
        pattern_name='loginindex', permanent=True
    )),
    url('', include('main.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

if not settings.DEBUG:
    handler404 = my404handler
