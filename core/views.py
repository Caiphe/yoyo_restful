from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
import requests


def index(request):
    maximum_values = []
    minimum_values = []
    average_values = []
    median_values = []

    if request.method == 'POST':
        city = request.POST.get('city')
        number_of_days = request.POST.get('number_of_days')

        # It's a free api they get only give us up to 3 days forecast
        if not int(number_of_days) > 10:
            api_key = settings.WEATHER_KEY
            base_url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={number_of_days}&aqi=no&alerts=no'
            weather_data = requests.get(base_url).json()

            for item in weather_data['forecast']['forecastday']:
                maximum_values.append(item['day']['maxtemp_c'])
                minimum_values.append(item['day']['mintemp_c'])
                average_values.append(item['day']['avgtemp_c'])
                median_values.append((item['day']['maxtemp_c'] + item['day']['mintemp_c'] + item['day']['avgtemp_c']) / 3)
        else:
            messages.error(request, "Number of days should be Max 3")
    context = {
        "maximum": maximum_values,
        "minimum": minimum_values,
        "average": average_values,
        "median": median_values
    }

    return render(request, 'index.html', context)

