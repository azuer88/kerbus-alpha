from django.contrib import admin

from models import Person
from models import Account
from models import Address


class AddressInline(admin.StackedInline):
    model = Address
    extra = 1


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'modified_by', 'created_by')
    inlines = [
        AddressInline,
    ]


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
