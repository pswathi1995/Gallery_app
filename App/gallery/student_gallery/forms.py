from django import forms            
from .models import student_info
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

class MyForm(forms.ModelForm):
   error_messages = {
        'img_validate': 'Image file is too large',
        'invalidImg':'could not read uploaded image'
    }
   name = forms.CharField(label="name",widget=forms.TextInput(attrs={'class':'form-control'}),help_text='100 characters max.', error_messages={'required': '**Please enter your name!!'})
   email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}),required = True)
  # student_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required = False)
   pic = forms.ImageField(label='Photo',error_messages={'required': 'Please upload your image'},required = True)
   audio_track = forms.FileField(label='Audio',required = False)
   video_track = forms.FileField(label='Video',required = False)
   discription = forms.CharField(label='description',widget=forms.Textarea,error_messages={'required': '**Please enter about yourself!!'})



   class Meta:
       model = student_info
       fields = ('name', 'pic', 'email', 'audio_track', 'video_track','discription')

  
   def clean(self,commit = True):
       name = self.cleaned_data.get('name')
       email = self.cleaned_data.get('email')
      # user.student_id = self.cleaned_data['student_id']
       pic = self.cleaned_data.get('pic')
       #image = RestrictedFileField(content_types=['video/quicktime', 'application/pdf']) # limit to QuickTime and PDF
       audio_track = self.cleaned_data.get('audio_track')
       video_track = self.cleaned_data.get('video_track')
       discription = self.cleaned_data.get('discription')
       return self.cleaned_data
