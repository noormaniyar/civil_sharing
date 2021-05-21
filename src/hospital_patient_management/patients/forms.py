from django import forms
from .models import Bed


class BedCreateForm(forms.ModelForm):

    class Meta:
        model = Bed
        fields = ['bed_name', 'extra_info']
