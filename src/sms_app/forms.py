from django import forms
from .models import Process

class NewProcessForm(forms.ModelForm):
    process_description = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Process
        fields = [
            'process_name',
            'process_description'
            ]