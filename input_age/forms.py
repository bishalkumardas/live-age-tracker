from django import forms
import datetime

class AgeInputForm(forms.Form):
    name= forms.CharField(max_length=100)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))