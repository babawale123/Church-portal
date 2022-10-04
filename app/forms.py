from django import forms
from .models import Contact_Form

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact_Form
		fields = ['name','subject','message']
		widgets = {
				'name': forms.TextInput(attrs={ 'class':'form-control'}),
				'subject': forms.TextInput(attrs={ 'class':'form-control'}),
				'message': forms.Textarea(attrs={ 'class':'form-control'}),

		}