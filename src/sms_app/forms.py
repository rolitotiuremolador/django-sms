from django import forms
from .models import Process

class NewProcessForm(forms.ModelForm):
    kpi_name = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 4, 'placeholder':'New kpi name for this process.'}
        ), 
        max_length=500,
        help_text = 'Max length of text is 500'
        )

    class Meta:
        model = Process
        fields = [
            'process_name',
            'kpi_name'
            ]