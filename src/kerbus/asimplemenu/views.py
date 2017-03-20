from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from models import MenuItem
from serializer import MenuItemSerializer

# Create your views here.
class MenuItemViewSet(viewsets.ModelViewSet):
     """
     A view that returns the menu items that should be displayed in JSON.
     """
     renderer_classes = (JSONRenderer,)

     queryset = MenuItem.objects.all()
     serializer_class = MenuItemSerializer
