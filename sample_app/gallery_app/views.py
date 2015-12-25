from django.shortcuts import render
from .models import profile
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'home.html')

def upload(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pic = request.FILES.get('docfile')
        discription = request.POST.get('discription')
        profile_obj = profile(name=name, pic=pic, discription=discription)
        profile_obj.save()
    else:
        print 'hello----'
    return render(request, 'upload.html')

def display(request):
    data = profile.objects.all()
    return render(request, 'gallery.html', {"cont":data, "media_url":settings.MEDIA_URL})

def uploadform(request):
    return render(request,'upload.html')
