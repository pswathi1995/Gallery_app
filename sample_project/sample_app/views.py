from django.shortcuts import render

from .models import gallery
from django.conf import settings 
# Create your views here.

def landing(request):
    return render(request, 'landingPage.html')

def upload(request):
    if request.method == 'POST':
        imageName = request.POST.get('imageName')
        imagePath = request.FILES.get('imagePath')
        imageDescription = request.POST.get('imageDescription')
        gallery_obj = gallery(imageName=imageName, imagePath=imagePath, imageDescription=imageDescription)
        gallery_obj.save()
    else:
        print 'hello----'
    return render(request, 'upload.html')

def display(request):
    data = gallery.objects.all()
    return render(request, 'display.html', {"cont":data})

def uploadPage(request):
    return render(request,'upload.html')
