from django import forms
from .models import urlInfo

class urlExpandForm(forms.ModelForm):
	
	class Meta:
		model = urlInfo
		fields = ('short',)