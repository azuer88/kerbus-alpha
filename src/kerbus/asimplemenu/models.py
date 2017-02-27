from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MenuItem(models.Model):
    title = models.CharField(max_length=80, 
                 blank=False, null=False, default='') 
    link = models.CharField(max_length=80, 
                 blank=False, null=False, default='') 
    
