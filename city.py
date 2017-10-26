import requests

# Personal key to access the OpenWeatherMap API. Please change it if you are re-using this code.
KEY = '70e725f0bad91621f9c86228a244abca'


class City:
    """
    A city in this app is composed of those different attributes: 
    - Location is an optional label describing one or more positions,
    - Position is a comma-separated triple containing latitude, longitude, and elevation in metres above sea
    level
    """

    def __init__(self, name, country, climate, elevation=0):
        """
        Builder for City object handling elevation. This is a quick fix because the webservice chosen here 
        does not provide this information. It would be a better idea to pick an other API.
        :param name: City's name
        :param country:  City's country code
        :param climate: City's climate
        :param elevation: City's elevation
        """
        self.name = name
        self.country = country
        self.climate = climate
        self.lat = 0
        self.lon = 0
        # TODO: handle elevation
        self.elevation = elevation
        self.get_coord()

    def build_from_json(self, json_city):
        """
        
        :param json_city: 
        :return: 
        """
        return self(json_city['name'], json_city['country'], json_city['climate'], json_city['elevation'])

    def to_string(self):
        """
        Return a row with all city information
        :return: 
        """
        return '|'.join(self.name, self.country, self.climate, '{};{};{}'.format(self.lon, self.lat, self.elevation))

    def get_coord(self):
        response = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?q={},{}&appid='.format(self.name, self.country) + KEY)
        if response.status_code == 200:
            self.lat = response.json()['coord']['lat']
            self.lon = response.json()['coord']['lon']