from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import profile
from django.conf import settings
from django.http import HttpResponseRedirect

from django.contrib import auth                 
from django.core.context_processors import csrf 
from forms import MyForm
  

# Create your views here.
def home(request):
    return render(request, 'home.html')


def upload(request):
   if request.method == 'POST':
       form = MyForm(request.POST)     # create form object
       print form.is_valid()
       if form.is_valid():
           name = request.POST.get('name')
           pic = request.FILES.get('pic')
           audio_track = request.FILES.get('audio_track')
           video_track = request.FILES.get('video_track')
           discription = request.POST.get('discription')
           profile_obj = profile(name=name, pic=pic, discription=discription, audio_track=audio_track,  video_track=video_track)
           profile_obj.save()
           data = profile.objects.all()
           return render(request, 'index.html', {"cont":data})
       print form.errors
       form = MyForm(request.POST)
       variables = RequestContext(request, {
           'error_message': form.errors,
           'form' : form,
       });
       return render_to_response('upload.html', variables)
   else:
       args = {}
       args.update(csrf(request))
       args['form'] = MyForm()
       print args
  # return render_to_response('upload.html', variables)
   return render(request, 'upload.html', args)

def display(request):
    data = profile.objects.all()
    return render(request, 'index.html', {"cont":data})

def uploadform(request):
    return render(request,'upload.html')



def editprofile(request):
    queryset = profile.objects.filter(id='35')
    if request.POST:
        form=MyForm(request.POST,instance=queryset)
        if form.is_valid():
           name = request.POST.get('name')
           pic = request.FILES.get('pic')
           audio_track = request.FILES.get('audio_track')
           video_track = request.FILES.get('video_track')
           discription = request.POST.get('discription')
           profile_obj = profile(name=name, pic=pic, discription=discription, audio_track=audio_track,  video_track=video_track)
           print profile_obj
           profile_obj.objects.update()
           data = profile.objects.all()
           return render(request, 'index.html', {"cont":data})
    else:
        data = profile.objects.get(id = '35')       
        form=MyForm(instance=data)
        template = 'editbook.html'
        data = { 'form':form }
    return render_to_response('name.html', data , RequestContext(request)) 
