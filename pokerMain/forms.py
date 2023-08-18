from django import forms
from django.forms import Textarea

from .models import report


class ContactForm(forms.ModelForm):
    class Meta:
        model = report
        fields = ['Name', 'Email', 'Bug']
        widgets = {
            'Bug': Textarea(attrs={"rows": 5, "cols": 32})
        }


