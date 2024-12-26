import requests

def fetch_weather_data(city):
    api_key = "426af6347cd40cfa1a368d99e80d7c20"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url).json()
    
    if 'main' in response:
        # Current weather
        current_weather = {
            'city': response['name'],
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'humidity': response['main']['humidity'],
            'pressure': response['main']['pressure'],
        }

        return current_weather
    return None
    
