import requests
from bs4 import BeautifulSoup
from weather import Weather

class WeatherScraper:
    BASE_URL = "https://forecast.weather.gov/MapClick.php"
    
    def get_lat_lon(self, city_name):
        """Get latitude and longitude for a city using the Nominatim API."""
        NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
        params = {
            'q': city_name,
            'format': 'json'
        }
        response = requests.get(NOMINATIM_URL, params=params)
        data = response.json()

        if not data:
            raise ValueError("City not found in Nominatim database!")

        lat = data[0]['lat']
        lon = data[0]['lon']

        return lat, lon

    def fetch_data(self, city_name):
        # Get latitude and longitude for the city
        lat, lon = self.get_lat_lon(city_name)

        # Construct the URL with the obtained latitude and longitude
        url = f"{self.BASE_URL}?lat={lat}&lon={lon}"

        # Fetch webpage content
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Scrape the required weather details
        temperature_f = soup.find("p", {"class": "myforecast-current-lrg"}).text
        temperature_c = soup.find("p", {"class": "myforecast-current-sm"}).text
        humidity = soup.find("td", text="Humidity").find_next_sibling("td").text
        wind_speed = soup.find("td", text="Wind Speed").find_next_sibling("td").text

        # Create and return a Weather instance
        return Weather(temperature_f, temperature_c, humidity, wind_speed)
