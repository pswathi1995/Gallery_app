from __future__ import unicode_literals

from django.db import models
from time import time
# Create your models here.
def getImage(instanace, filename):
    return "documents/%s_%s"%(str(time()),filename)

def getAudio(instanace, filename):
    return "audio/%s_%s"%(str(time()),filename)

def getVideo(instanace, filename):
    return "video/%s_%s"%(str(time()),filename)

def getResume(instanace, filename):
    return "resume/%s_%s"%(str(time()),filename)

class Students(models.Model):
    student_id= models.CharField(max_length = 20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length = 120)
    last_name = models.CharField(max_length = 120)
    email = models.EmailField(max_length=60, default = '')
    mobile = models.CharField(max_length = 10)

