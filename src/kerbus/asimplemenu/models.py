from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MenuItem(models.Model):
    title = models.CharField(max_length=80, 
                 blank=False, null=False, default='') 
    link = models.CharField(max_length=80, 
                 blank=True, null=False, default='') 
    sequence = models.IntegerField(default=0)
    def __unicode__(self):
        if self.link:
           return "%s [%s]" % (self.title, self.link)
        else:
           return self.title    
    
    class Meta:
        ordering = ['sequence',]
