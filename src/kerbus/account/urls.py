from django.conf.urls import url
from django.views.generic.base import RedirectView

import views

urlpatterns = [
    url(r'^login', views.index, name='loginindex'),
    url(r'^', RedirectView.as_view(
        pattern_name='loginindex', permanent=True)),
]
