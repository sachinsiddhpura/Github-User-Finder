from django import forms
from .models import GitUser

class GitForm(forms.ModelForm):

	class Meta:
		model = GitUser
		fields = '__all__'