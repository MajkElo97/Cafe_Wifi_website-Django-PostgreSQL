from django import forms
from .models import Cafe


class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = [
            'name',
            'map_url',
            'img_url',
            'location',
            'has_sockets',
            'has_toilet',
            'has_wifi',
            'seats',
            'coffee_price',
        ]

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    map_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    img_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    has_sockets = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), required=False)
    has_toilet = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), required=False)
    has_wifi = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), required=False)
    seats = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    coffee_price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
