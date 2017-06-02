from django.contrib import admin

from models import Person
from models import Account
from models import Location


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'modified_by', 'created_by')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
