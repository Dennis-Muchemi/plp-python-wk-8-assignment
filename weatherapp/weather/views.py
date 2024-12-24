from django.shortcuts import render, redirect
from .utils import fetch_weather_data
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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
    weather_data = fetch_weather_data(city)

    if weather_data and request.user.is_authenticated:
        from .models import Weather
        Weather.objects.create(
            user=request.user,
            city=weather_data['city'],
            temperature=weather_data['temperature'],
            description=weather_data['description']
        )

    history = Weather.objects.filter(user=request.user).order_by('-timestamp')[:10] if request.user.is_authenticated else []
    return render(request, 'weather/weather.html', {'weather': weather_data, 'history': history})
