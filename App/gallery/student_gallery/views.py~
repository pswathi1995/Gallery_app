from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import student_info
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
           email = request.POST.get('email')
           audio_track = request.FILES.get('audio_track')
           video_track = request.FILES.get('video_track')
           discription = request.POST.get('discription')
           student_info_obj = student_info(name=name, pic=pic,email = email, discription=discription, audio_track=audio_track,  video_track=video_track)
           student_info_obj.save()
           data = student_info.objects.all()
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
    data = student_info.objects.all()
    return render(request, 'index.html', {"cont":data})

def uploadform(request):
    return render(request,'upload.html')

  
from django.contrib import auth                 
from django.core.context_processors import csrf 
from forms import MyForm

def register_user(request):
    if request.method == 'POST':
        form = MyForm(request.POST)     # create form object
        print form.is_valid()
        if form.is_valid():
            print "ramya"
            form.save()
            return HttpResponseRedirect('display')
    args = {}
    args.update(csrf(request))
    args['form'] = MyForm()
    print args
    return render(request, 'upload.html', args)
