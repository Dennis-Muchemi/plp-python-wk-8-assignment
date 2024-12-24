import requests

def fetch_weather_data(city):
    api_key = "426af6347cd40cfa1a368d99e80d7c20"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        alerts = data.get('alerts', [])
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'alerts': alerts
        }
    return None
