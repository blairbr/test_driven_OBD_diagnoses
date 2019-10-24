import requests

class WeatherApi:

    def __init__(self):
        self.url = 'http://api.openweathermap.org/data/2.5/forecast?zip=48104&appid=3182650f72b53ec159a2efe5b65b5413&units=imperial'

    def get_current_temp(self):
        json_data = requests.get(self.url).json()
        temp = json_data['list'][0]['main']['temp']
        current_temp = f"The temperature is currently {temp}"
        return current_temp

    def get_current_wind_speed(self):
        json_data = requests.get(self.url).json()
        wind_speed = json_data['list'][0]['wind']['speed']
        current_wind_speed = f"The wind speed is currently {wind_speed} miles per hour"
        return current_wind_speed

    def get_current_weather_conditions(self):
        json_data = requests.get(self.url).json()
        weather_description = json_data['list'][0]['weather'][0]['description']
        current_weather_description = f"Current weather for Ann Arbor is : {weather_description}"
        return current_weather_description
