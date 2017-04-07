from __future__ import unicode_literals

from django.db import models


def name_field(**kargs):
    kargs.setdefault('max_length', 60)
    kargs.setdefault('blank', False)
    kargs.setdefault('default', '')
    kargs.setdefault('null', False)
    return models.CharField(**kargs)


class PersonMixin(models.Model):
    first_name = name_field()
    last_name = name_field
    midde_name = name_field(blank=True)

    @property
    def full_name(self):
        if self.middle_name:
            return "%s, %s %s." % (self.last_name,
                                   self.first_name,
                                   self.midde_name)
        else:
            return "%s, %s" % (self.last_name, self.first_name)

    class Meta:
        abstract = True


class Person(PersonMixin, models.Model):
    pass
