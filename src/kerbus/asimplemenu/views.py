# from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import JSONRenderer

# rest framework security
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from models import Item, Group
from serializer import MenuItemSerializer
from serializer import MenuGroupSerializer


class MenuGroupDetail(generics.RetrieveAPIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = MenuGroupSerializer
    renderer_classes = (JSONRenderer, )
    queryset = Group.objects.all()


class MenuItemList(generics.ListAPIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = MenuItemSerializer
    renderer_classes = (JSONRenderer, )

    def get_queryset(self):
        """
        This view will return a list of menu items in the specified group.
        """
        group = self.kwargs['group']
        try:
            group_id = int(group)
        except ValueError:
            matches = Group.objects.filter(name__iexact=group)
            if len(matches):
                group_id = matches[0].id
            else:
                group_id = None

        return Item.objects.filter(groups__in=[group_id])
