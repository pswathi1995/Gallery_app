from __future__ import unicode_literals

from django.db import models
from time import time

# Create your models here.
def getImage(instanace, filename):
    print filename
    return "documents/%s_%s"%(str(time()),filename)

class gallery(models.Model):
    imageName = models.CharField(max_length = 120)
    imagePath = models.FileField(upload_to=getImage)
    imageDescription = models.CharField(max_length = 300)
    
