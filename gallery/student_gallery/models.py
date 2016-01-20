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

class student_info(models.Model):
    name = models.CharField(max_length = 120)
    email = models.EmailField(max_length=60, default = '')
    pic = models.ImageField(upload_to=getImage)
    discription = models.CharField(max_length=500)
    audio_track = models.FileField(upload_to=getAudio, default = '')
    video_track = models.FileField(upload_to=getVideo, default = '')
    resume = models.FileField(upload_to=getResume, default = '')

    def __str__(self):
	return self.email



