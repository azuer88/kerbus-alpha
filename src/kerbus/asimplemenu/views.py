from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from models import Item
from serializer import MenuItemSerializer

# Create your views here.
class MenuItemViewSet(viewsets.ModelViewSet):
     """
     A view that returns the menu items that should be displayed in JSON.
     """
     renderer_classes = (JSONRenderer,)

     queryset = Item.objects.all()
     serializer_class = MenuItemSerializer
