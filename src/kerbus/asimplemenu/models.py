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
    parent = models.ForeignKey('Group', null=True, blank=True)

    @property
    def puid(self):
        if self.parent:
            return self.parent.id
        else:
            return 0

    def __unicode__(self):
        return self.name


class Item(models.Model):
    title = NameField()
    link = models.CharField(max_length=80,
                            blank=True, null=False, default='')
    load = models.ForeignKey(Group, null=True,
                             blank=True, related_name='submenu')
    sequence = models.IntegerField(default=0)
    groups = models.ManyToManyField(Group, related_name="items")

    @property
    def muid(self):
        if self.load:
            return self.load.id
        else:
            return 0

    def __unicode__(self):
        if self.link:
            return "%s [%s]" % (self.title, self.link)
        else:
            return self.title

    class Meta:
        ordering = ['sequence', ]
