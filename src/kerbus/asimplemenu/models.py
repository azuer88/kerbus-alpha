from __future__ import unicode_literals

from django.db import models


def _set_charfield(**kwargs):
    kwargs.setdefault('max_length', 80)
    kwargs.setdefault('blank', False)
    kwargs.setdefault('default', '')
    return kwargs


def NameField(*args, **kwargs):
    kwargs = _set_charfield(**kwargs)
    return models.CharField(*args, **kwargs)


def DescField(*args, **kwargs):
    kwargs = _set_charfield(**kwargs)
    kwargs.setdefault('max_length', 200)
    return models.CharField(*args, **kwargs)


class Group(models.Model):
    name = NameField()
    description = DescField()

    def __unicode__(self):
        return self.name


class Item(models.Model):
    title = NameField()
    link = models.CharField(max_length=80,
                            blank=True, null=False, default='')
    sequence = models.IntegerField(default=0)
    groups = models.ManyToManyField(Group, related_name="group")

    def __unicode__(self):
        if self.link:
            return "%s [%s]" % (self.title, self.link)
        else:
            return self.title

    class Meta:
        ordering = ['sequence', ]
