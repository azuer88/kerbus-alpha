from rest_framework import serializers
from models import Item, Group


class MenuItemSerializer(serializers.ModelSerializer):
    load = serializers.StringRelatedField()

    class Meta:
        model = Item
        fields = ['id', 'title', 'link', 'load']


class MenuItemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        obj = {
            "id": value.id,
            "title": value.title,
            "link": value.link,
            "load": value.muid,
        }
        return obj


class MenuGroupSerializer(serializers.ModelSerializer):
    items = MenuItemRelatedField(many=True, queryset=Item.objects.all())

    class Meta:
        model = Group
        fields = ('id', 'name', 'description', 'items')
