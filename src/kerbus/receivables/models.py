from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


def name_field(**kargs):
    kargs.setdefault('max_length', 60)
    kargs.setdefault('blank', False)
    kargs.setdefault('default', '')
    kargs.setdefault('null', False)
    return models.CharField(**kargs)


class PersonMixin(models.Model):
    first_name = name_field()
    last_name = name_field()
    middle_name = name_field(blank=True)

    class Meta:
        ordering = ('last_name', 'first_name', 'middle_name', )
        abstract = True
        unique_together = [('last_name', 'first_name', 'middle_name', ), ]

    def _get_mi(self):
        return u"%c." % self.middle_name[0] \
            if self.middle_name.strip() else ""

    @property
    def full_name(self):
        namestr = "%s, %s %s" % (
            self.last_name,
            self.first_name,
            self._get_mi())
        return namestr.strip()

    def __unicode__(self):
        return u"%s" % self.full_name


class CreatedModifiedMixin(models.Model):
    created_by = models.ForeignKey(User,
                                   related_name='%(app_label)s_%(class)s' +
                                   '_created_by',
                                   editable=False,
                                   default=1)
    modified_by = models.ForeignKey(User,
                                    related_name='%(app_label)s_%(class)s' +
                                    '_modified_by',
                                    editable=False,
                                    default=1)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


ADDRESS_TYPE_CHOICE = [
        (1, "Home Address"),
        (2, "Work Address"),
        (3, "Other Address"),
    ]


class Address(models.Model):
    kind = models.SmallIntegerField("Type", default=1)
    street = models.CharField("Street Address",
                              max_length=100, default='')
    barangay = models.CharField("Barangay / District",
                                max_length=100, default='')
    city = models.CharField("City / Municipality",
                            max_length=100, default='')
    zipcode = models.CharField("ZIP Code",
                               max_length=20, default='')
    province = models.CharField("Province / Region",
                                max_length=100, default='')

    class Meta:
        verbose_name_plural = "Addresses"


class Person(PersonMixin, CreatedModifiedMixin, models.Model):
    pass


class Account(CreatedModifiedMixin, models.Model):
    pass
