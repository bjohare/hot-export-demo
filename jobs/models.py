from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, Group


class ExportFormat(models.Model):
    """Model for a ExportFormat"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    cmd = models.TextField(max_length=1000)
    objects = models.Manager()
    class Meta:
        managed = True
        db_table = 'export_formats'


class Job(models.Model):
    """Model for a Job"""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='user')
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=65000)
    status = models.CharField(max_length=30)
    format = models.ManyToManyField(ExportFormat, related_name='formats')
    objects = models.Manager()
    class Meta:
        managed = True
        db_table = 'jobs'
        


    
