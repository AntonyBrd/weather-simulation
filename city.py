import requests

# Personnal key to access the openweathermap API. Please change it if you are re-using this code.
KEY='70e725f0bad91621f9c86228a244abca'

class City:
    """
    A city in this app is composed of those different attributes: 
    - Location is an optional label describing one or more positions,
    - Position is a comma-separated triple containing latitude, longitude, and elevation in metres above sea
    level
    """

    def __init__(self, name, country, climate):
        self.name = name
        self.country = country
        self.climate = climate
        self.lat = 0
        self.lon = 0
        self.elevation = 0 #TODO: handle elevation
        self.get_position()

    def to_string(self):
        return '|'.join(self.name, self.country)

    def get_position(self):
        response = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?q={},aus&appid='.format(self.name, self.country) + KEY)
        if response.status_code == 200:
            self.lat = response.json()['coord']['lat']
            self.lon = response.json()['coord']['lon']