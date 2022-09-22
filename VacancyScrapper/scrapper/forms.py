from django import forms

from .models import JobCategory


class JobForm(forms.ModelForm):
    class Meta:
        model = JobCategory
        fields = '__all__'
