from __future__ import unicode_literals

from django.db import models
from time import time

# Create your models here.

def getImage(instanace, filename):
    print filename
    return "documents/%s_%s"%(str(time()),filename)

class profile(models.Model):
    name = models.CharField(max_length = 120)
    pic = models.FileField(upload_to=getImage)
    discription = models.CharField(max_length=500)
    def __str__(self):
	return self.email
