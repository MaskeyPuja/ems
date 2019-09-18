from django import forms

from .models import Profile, Task

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile

		fields = ('user', 'name', 'address')

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task

		fields = ('name', 'description', 'assigned_by', 'assigned_to', 'assigned_date', 'status')