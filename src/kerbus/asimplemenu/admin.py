from django.contrib import admin

from models import Item, Group


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'membership', 'sequence',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent')
