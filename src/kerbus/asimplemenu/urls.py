from django.conf.urls import url

from views import MenuItemList
from views import MenuGroupDetail

urlpatterns = [
    url('^group/(?P<group>.+)/$', MenuItemList.as_view()),
    url('^(?P<pk>.+)/$', MenuGroupDetail.as_view()),
]
