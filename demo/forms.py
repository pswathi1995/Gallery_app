from django import forms

from .models import Sign

class ContactForm(forms.Form):
	name = forms.CharField(required=False)
	email = forms.EmailField()
	#message = forms.CharField()


class SignUpForm(forms.ModelForm):
	class Meta:
		model = Sign
		fields = ['name', 'email']
		### exclude = ['full_name']
	
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		# if not domain == 'USC':
		# 	raise forms.ValidationError("Please make sure you use your USC email.")
		if not extension == "edu":
			raise forms.ValidationError("Please use a valid .EDU email address")
		return email

	def clean_name(self):
		name = self.cleaned_data.get('name')
		#write validation code.
		return name
