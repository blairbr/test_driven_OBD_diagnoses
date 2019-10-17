import unittest
from unittest.mock import patch
from weather_api import WeatherApi

class Test_Weather_Api(unittest.TestCase):

    def test_weather_api(self):

        fake_json = {"cod":"200","message":0.0106,"cnt":40,"list":[{"dt":1567198800,"main":{"temp":73.94,"temp_min":70.54,"temp_max":73.94,"pressure":1018.87,"sea_level":1018.87,"grnd_level":985.61,"humidity":54,"temp_kf":1.89},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":31},"wind":{"speed":7.29,"deg":290.115},"sys":{"pod":"d"},"dt_txt":"2019-08-30 21:00:00"},{"dt":1567209600,"main":{"temp":65.3,"temp_min":62.74,"temp_max":65.3,"pressure":1020.29,"sea_level":1020.29,"grnd_level":986.92,"humidity":71,"temp_kf":1.42},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"clouds":{"all":65},"wind":{"speed":5.28,"deg":298.278},"sys":{"pod":"n"},"dt_txt":"2019-08-31 00:00:00"}]}

        with patch('weather_api.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = fake_json

            obj = WeatherApi()
            response = obj.get_current_temp()

        self.assertEqual("The temperature is currently 73.94", response)

    def test_windspeed_from_weather_api(self):

        fake_json = {"cod":"200","message":0.0106,"cnt":40,"list":[{"dt":1567198800,"main":{"temp":73.94,"temp_min":70.54,"temp_max":73.94,"pressure":1018.87,"sea_level":1018.87,"grnd_level":985.61,"humidity":54,"temp_kf":1.89},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":31},"wind":{"speed":7.29,"deg":290.115},"sys":{"pod":"d"},"dt_txt":"2019-08-30 21:00:00"},{"dt":1567209600,"main":{"temp":65.3,"temp_min":62.74,"temp_max":65.3,"pressure":1020.29,"sea_level":1020.29,"grnd_level":986.92,"humidity":71,"temp_kf":1.42},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"clouds":{"all":65},"wind":{"speed":5.28,"deg":298.278},"sys":{"pod":"n"},"dt_txt":"2019-08-31 00:00:00"}]}

        with patch('weather_api.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = fake_json

            obj = WeatherApi()
            response = obj.get_current_wind_speed()

        self.assertEqual(f"The wind speed is currently 7.29 miles per hour", response)

    def test_current_weather_conditions_from_weather_api(self):

        fake_json = {"cod":"200","message":0.0106,"cnt":40,"list":[{"dt":1567198800,"main":{"temp":73.94,"temp_min":70.54,"temp_max":73.94,"pressure":1018.87,"sea_level":1018.87,"grnd_level":985.61,"humidity":54,"temp_kf":1.89},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":31},"wind":{"speed":7.29,"deg":290.115},"sys":{"pod":"d"},"dt_txt":"2019-08-30 21:00:00"},{"dt":1567209600,"main":{"temp":65.3,"temp_min":62.74,"temp_max":65.3,"pressure":1020.29,"sea_level":1020.29,"grnd_level":986.92,"humidity":71,"temp_kf":1.42},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"clouds":{"all":65},"wind":{"speed":5.28,"deg":298.278},"sys":{"pod":"n"},"dt_txt":"2019-08-31 00:00:00"}]}

        with patch('weather_api.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = fake_json

            obj = WeatherApi()
            response = obj.get_current_weather_conditions()

        self.assertEqual("Current weather for Ann Arbor is : scattered clouds", response)


if __name__ == "__main__":
    unittest.main()