class Weather:
    def __init__(self, temperature_f, temperature_c, humidity, wind_speed):
        self.temperature_f = temperature_f
        self.temperature_c = temperature_c
        self.humidity = humidity
        self.wind_speed = wind_speed

    def __str__(self):
        return (f"Temperature (Fahrenheit): {self.temperature_f}\n"
                f"Temperature (Celsius): {self.temperature_c}\n"
                f"Humidity: {self.humidity}\n"
                f"Wind Speed: {self.wind_speed}")
