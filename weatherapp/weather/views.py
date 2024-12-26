from django.shortcuts import render, redirect
from .utils import fetch_weather_data
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Weather
from datetime import datetime, timedelta
from random import uniform

# Create your views here.
@login_required
def weather_view(request):
    city = request.GET.get('city', 'London')
    weather_data = fetch_weather_data(city)
    return render(request, 'weather/weather.html', {'weather': weather_data})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

#Weather view with history
def weather_view(request):
    city = request.GET.get('city', 'London')
    current_weather = fetch_weather_data(city)

    # Retrieve or create a Weather record
    if current_weather:
        weather_record, created = Weather.objects.get_or_create(
            city=current_weather['city'],
            defaults={
                'temperature': current_weather['temperature'],
                'description': current_weather['description'],
                'humidity': current_weather['humidity'],
                'pressure': current_weather['pressure'],
            }
        )
        if not created:
            # Update the record with the latest data
            weather_record.temperature = current_weather['temperature']
            weather_record.description = current_weather['description']
            weather_record.humidity = current_weather['humidity']
            weather_record.pressure = current_weather['pressure']
            weather_record.save()

        # Get the last 3 weather records as history
        history = Weather.objects.filter(city=city).order_by('-timestamp')[:3]

        # Generate a 3-day forecast
        forecast = [
            {
                'date': (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d'),
                'temperature': round(uniform(weather_record.temperature - 5, weather_record.temperature + 5), 2),
                'description': weather_record.description,
            }
            for i in range(1, 4)
        ]

        return render(request, 'weather/weather.html', {
            'weather': current_weather,
            'history': history,
            'forecast': forecast,
        })

    return render(request, 'weather/weather.html', {'error': 'City not found.'})
