from django.shortcuts import render
from django.http import JsonResponse
from .forms import WeatherForm
import requests

# Create your views here.
def index(request):
    return render(request, 'weather/index.html')

def get_windspeed(request):
    zipcode = request.GET['zip']
    url = 'http://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid=eb0a2f63d7ca3cc8c8a3837a065ab42a'
    weather = requests.get(url.format(zipcode)).json()

    return JsonResponse({
        "zip": zipcode,
        "city": weather['name'],
        "windspeed": weather['wind']['speed']
    })