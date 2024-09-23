from .models import CollaborateRequest
from django import forms

class CollaborateForm(forms.ModelForm):
	"""
	Stores a single collaboration request message
	"""
	class Meta:
		model = CollaborateRequest
		fields = ("name","email","message",)