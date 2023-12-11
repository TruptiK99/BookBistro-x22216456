from django import forms
from .models import Booktable

class BooktableForm(forms.ModelForm):
    class Meta:
        fields = ('table', 'image', 'no_of_people', 'description')
        labels = {
            'table':'Table',
            'image':'Image',
            'no_of_people':'No of People',
            'description':'Description',
        }