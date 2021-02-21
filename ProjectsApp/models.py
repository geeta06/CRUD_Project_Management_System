from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
import uuid



# create models from here

def get_24_char_uuid():
    uid = uuid.uuid4().hex
    for i in range(0, 8):
        uid = uid[:i] + uid[i + 1:]
    return uid.upper()

def get_filepath_with_name(instance, name):
    date = datetime.strftime(datetime.now(), "%Y/%m/%d/")
    ext = name.split('.')[-1]
    return '/Users/lendenclub/Desktop/venv/project1/project1/'+date+get_24_char_uuid()+"."+ext

class Project(models.Model):
    """A project the user is working on."""
    name = models.CharField(max_length=100, null=True, editable=True)
    description = models.TextField(null=True, editable=True)
    duration = models.IntegerField(null=True,  blank=True) #in days
    avtar = models.ImageField(upload_to=get_filepath_with_name, editable=True)

    def __unicode__(self):
        return "" + str(self.id)


class Task(models.Model):
    """A task of a project to complete."""
    name = models.CharField(max_length=100, null=True, editable=True)
    project = models.ForeignKey(Project, related_name='task_project', on_delete=models.CASCADE)
    description = models.TextField(null=True, editable=True)
    start_date = models.DateField(blank=True, editable=True)
    end_date = models.DateField(blank=True, editable=True)


    class Meta:
        verbose_name_plural = 'tasks'

    def __unicode__(self):
        return "" + str(self.id)

