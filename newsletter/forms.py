from django import forms

from .models import NewsletterUser, Newsletter

class NewsletterUserSignUpForm(forms.ModelForm):
	class Meta:
		model = NewsletterUser
		fields = ['email']

		widgets = {
				'email': forms.TextInput(attrs={ 'class':'form-control'}),
			
		}

		def clean_email(self):
			email = self.cleaned_data.get('email')

			return email

class NewsletterCreationForm(forms.ModelForm):

	class Meta:
		model = Newsletter
		fields = ['subject', 'body', 'email', 'status']

		widgets = {
				'subject': forms.TextInput(attrs={ 'class':'form-control'}),
				'body': forms.Textarea(attrs={ 'class':'form-control'}),
				'email': forms.SelectMultiple(attrs={ 'class':'form-control related-widget-wrapper','required id':'id_email','name':'email'}),
				'status': forms.Select(attrs={ 'class':'form-control'}),
			
		}


		