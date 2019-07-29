from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url="http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=043a91931df275ee5ef7788a0bf5e99f"
    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()

    weather_data = []
    for city in cities:

 
        
        city_weather = requests.get(url.format(city)).json()
        weather_d = {"city" : city  ,  
                     "temperature" : city_weather["main"]["temp"],
                     "description" : city_weather["weather"][0]["description"]  , 
                     'icon' : city_weather['weather'][0]['icon']
                    } 
        weather_data.append(weather_d)
    context = {"weather_data" : weather_data ,"form" : form}
    

    return render(request,"index.html",context)

