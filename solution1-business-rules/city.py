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
        # TODO: handle elevation with a other method
        self.elevation = elevation
        self.get_coord()

    @staticmethod
    def build_from_json(json_city):
        """
        Create a city instance from input json data.
        :param json_city: a json object containing City attributes
        :return: a City object
        """
        return City(json_city['name'], json_city['country'], json_city['climate'], json_city['elevation'])

    def get_coord(self):
        """
        Compute coordinates from openweathermap API.
        NB: It uses a private key, with developer role.
        """
        response = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'.format(self.name, self.country, KEY))
        if response.status_code == 200:
            self.lat = response.json()['coord']['lat']
            self.lon = response.json()['coord']['lon']

    def to_string(self):
        """
        Return a row with all city information
        :return: a string with all the city information
        """
        return '|'.join([self.name, self.country, self.climate, ','.join([str(self.lon), str(self.lat),
                                                                          str(self.elevation)])])
