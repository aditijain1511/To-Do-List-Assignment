from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = "__all__"

class UpdateForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = "__all__"

