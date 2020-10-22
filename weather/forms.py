from django import forms

class WeatherForm(forms.Form):
    zip = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'Zipcode'}), label=False)