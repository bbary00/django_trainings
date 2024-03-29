from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests


def index(request):
    appid = '0248accb057037f5836783cfcf327579'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}" \
          "&units=metric&appid=" + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    context_list = []
    for city in cities:

        response = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': response['main']['temp'],
            'icon': response['weather'][0]['icon']
        }
        context_list.append(city_info)

    context = {
        'info': context_list,
        'form': form
    }

    return render(request, 'weather/index.html', context)
