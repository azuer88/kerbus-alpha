from django.conf.urls import url
# from django.conf.urls import include
# from rest_framework import routers

# from views import MenuItemViewSet
# from views import MenuGroupViewSet
from views import MenuItemList

# router = routers.DefaultRouter()
# router.register(r'item', MenuItemViewSet)
# router.register(r'group', MenuGroupViewSet)

urlpatterns = [
    # url('^', include(router.urls)),
    url('^group/(?P<group>.+)/$', MenuItemList.as_view()),
]
