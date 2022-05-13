from django.contrib import messages
from django.http import response
from django.shortcuts import get_object_or_404, render, redirect
import requests
from decouple import config
from pprint import pprint
from .models import City

def index(request):
    cities = City.objects.all()
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
    # city = "Berlin"
    # response = requests.get(url.format(city, config("API_KEY")))
    # content = response.json()
    # pprint(content)
    
    user_city = request.GET.get("name")
    if user_city:
        response = requests.get(url.format(user_city, config("API_KEY")))
        # print(response)
        # print(response.status_code)
        if response.status_code == 200:
            content = response.json()
            pprint(content)
            response_city = content["name"]
            if City.objects.filter(name=response_city):
                messages.warning(request, "City already exixts.")
            else:
                City.objects.create(name=response_city)
                messages.success(request, "City successfully created.")
        else:
            messages.warning(request, "City not found.")
    
    city_data = []
    for city in cities:
        # print(city)
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
        response = requests.get(url.format(city, config("API_KEY")))
        content = response.json()
        # pprint(content)
        data = {
            "city" : city,
            "temp" : int(content["main"]["temp"]),
            "desc" : content["weather"][0]["description"],
            "icon" : content["weather"][0]["icon"],
        }
        city_data.append(data)
    # pprint(city_data)
    
    context = {
        "city_data" : city_data
    }
    return render(request, 'weatherapp/index2.html', context)


def city_delete(request, id):
    city = get_object_or_404(City, id=id)
    city.delete()
    messages.success(request, "City successfully deleted.")
    return redirect("home")
    