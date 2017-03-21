from rest_framework import serializers
from models import Item, Group


class MenuItemSerializer(serializers.ModelSerializer):
    load = serializers.StringRelatedField()

    class Meta:
        model = Item
        fields = ['id', 'title', 'link', 'load']


class MenuGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
