from django import forms
from .models import MLModel

class ModelForm(forms.ModelForm):
  class Meta:
    model = MLModel
    fields = ['name', 'matematika', 'bahasa_inggris', 'bahasa_indonesia']