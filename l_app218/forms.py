from .models import Booking
from django import forms
from django.forms.widgets import DateInput, TimeInput


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'dateField': DateInput(attrs={'type': 'date'}),
            'timeField': TimeInput(attrs={'type': 'time'}),
        }