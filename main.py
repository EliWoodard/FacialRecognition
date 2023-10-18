from scraper import WeatherScraper
from weather import Weather
import requests
from bs4 import BeautifulSoup

def main():
    # Welcome the user and provide a brief description of the program.
    print("Welcome! This is my Weather Scraper!")
    print("Enter a city name to fetch its current weather data.")
    print("----------------------------------------------------\n")

    # Get input from the user for the city name.
    city_name = input("Enter the name of the city: ")

    # Create an instance of the WeatherScraper class.
    scraper = WeatherScraper()

    try:
        weather_data = scraper.fetch_data(city_name)

        # Display the fetched weather data to the user.
        print("\n-------------------------------")
        print("Weather Data:")
        print(weather_data)  # Uses the __str__ method from the Weather class.
        print("-------------------------------")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
