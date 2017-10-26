from city import City
import numpy as np
from datetime import date, datetime
import time
# 3 possible condition states for weather
CONDITIONS = ['Snow', 'Rain', 'Sunny']

# We consider the following climate dictionary:
# keys being the Koppen classification group and values the mean temperature for this group
CLIMATES = {'A': 27, 'B': 22, 'C': 17, 'D': 10, 'E': 5}
# TODO : deep into the classification details to do the same job for rain vs sun


def compute_theoretical_pressure(h):
    """
    Compute pressure from elevation according to the international formula of barometric leveling.
    :param: h is the elevation
    :return: p the theoretical pressure
    """
    if h > 0:
        return 1013.25 * (1 - (0.0065 * h / 288.15) ** 5.255)
    else:
        return 1013.25 * (1 - (0.0065 * h / 288.15) ** 5)


def gaussian_random(mean, sd):
    """
    Give a random variable according to the gaussian distribution (mu, sigma)
    :param mean: mu
    :param sd: sigma
    :return: the random variable value rounded with 1 decimal.
    """
    return np.around(np.random.normal(mean, sd, 1)[0], 1)


def generate_date(start_date=date(2000, 01, 02), end_date=date(2050, 01, 01)):
    """
    Generate a date formatted string between 2 defined dates. 
    Default values : 
       - start = January 2nd, 2000 
       - end = January 1st, 2050
    :return: String as a date with ISO8601 format
    """
    ts_start = time.mktime(start_date.timetuple())
    ts_end = time.mktime(end_date.timetuple())
    ts_rand = np.random.uniform(ts_start, ts_end, 1)
    return datetime.utcfromtimestamp(ts_rand).strftime('%Y-%m-%dT%H:%M:%SZ')


class Weather:
    """
     - Local time is an ISO8601 date time,
    - Conditions is either Snow, Rain, Sunny,
    - Temperature is in Celsius,
    - Pressure is in hPa, and
    - Relative humidity is a %.
    """

    def __init__(self, city, timestamp, pressure=1013.3,
                 condition=CONDITIONS[2], temperature=17, humidity=60):
        """
        Builder for Weather object.
        :param city: Concerned city
        :param timestamp: date when the weather is computed
        """
        if city.__class__ != City:
            raise "First argument has to be a City."
        else:
            self.city = city
        self.timestamp = timestamp
        self.pressure = pressure
        self.low_pressure = False
        self.condition = condition
        self.temperature = temperature
        self.mean_temperature = CLIMATES[self.city.climate]
        self.humidity = humidity
        # Firstly generate pressure
        self.generate_pressure()
        # Secondly generate temperature
        self.generate_temperature()
        # Thirdly generate condition
        self.generate_condition()
        # finally, set humidity
        self.generate_humidity()

    def is_summer(self):
        """
        Check weither it's summer or not in the concerned city
        :return: True if it is summer, False else
        """
        weather_month = datetime.strptime(self.timestamp, '%Y-%m-%dT%H:%M:%SZ').month
        if (self.city.lat > 0) & (5 < weather_month < 10):
            return True
        elif (self.city.lat < 0) & (weather_month > 10 or weather_month < 5):
            return True
        else:
            False

    def generate_pressure(self, sd=15):
        """
        Randomly generate pressure with respect to the international formula of barometric leveling.
        :param: sd standard deviation for the normal distribution of pressure
        :return: generated pressure value
        """
        theoretical_pressure = compute_theoretical_pressure(self.city.elevation)
        self.pressure = gaussian_random(theoretical_pressure, sd)
        if self.pressure < theoretical_pressure:
            self.low_pressure = True
        return theoretical_pressure

    def generate_temperature(self, sd=4):
        """
        Randomly generate temperature with dependency on season and pressure
        :param sd: sd standard deviation for the normal distribution of temperature
        :return: generated temperature value
        """
        mean_temperature = self.mean_temperature
        if self.is_summer():
            mean_temperature *= 1.2
        else:
            mean_temperature *= .8
        if self.low_pressure:
            mean_temperature -= 1.5
        self.temperature = gaussian_random(mean_temperature, sd)
        return self.temperature

    def generate_condition(self):
        """
        Randomly generate weather condition (snow, rain, sun).
        Obviously, the condition reflects temperature, pressure and season.
        Here is a quite simple algorithm, similar to a decision tree that would need to be optimized.
        :return: generated condition in the previously defined CONDITIONS list
        """
        rand = np.random.uniform(0, 1, 1)
        low_pressure_factor = .25 if self.low_pressure else 0
        low_temperature_factor = .1 if self.temperature < 3 else 0
        winter_factor = .3 if not self.is_summer() else 0
        if self.city.climate == 'A':
            climate_factor = 0
        elif self.city.climate in ['B', 'C']:
            climate_factor = 1
        else:
            climate_factor = 1.2

        if rand < climate_factor * (low_pressure_factor + low_temperature_factor):
            self.condition = CONDITIONS[0]
        elif rand < climate_factor * (low_pressure_factor + winter_factor):
            self.condition = CONDITIONS[1]
        else:
            self.condition = CONDITIONS[2]
        return self.condition

    def generate_humidity(self):
        """
        Randomly generate humidity.
        This method introduces a mistake, humidity does not increase with cold. We will pretend to minimize this
         mistake by using a large standard deviation to get more "randomness"
        :return: generated humidity
        """
        humidity = 50
        if self.condition == CONDITIONS[0]:
            humidity = gaussian_random(90, 2)
        elif self.condition == CONDITIONS[1]:
            humidity = gaussian_random(80, 8)
        elif self.city.climate == 'A':
            humidity = gaussian_random(20, 8)
        elif self.city.climate == 'B':
            humidity = gaussian_random(40, 12)
        elif self.city.climate == 'C':
            humidity = gaussian_random(60, 15)
        elif self.city.climate == 'D':
            humidity = gaussian_random(65, 12)
        elif self.city.climate == 'E':
            humidity = gaussian_random(70, 8)
        if humidity < 5:
            humidity = 5
        elif humidity > 99:
            humidity = 99
        humidity = np.around(humidity, 0)
        self.humidity = str(humidity)
        return self.humidity

    def get_temperature(self):
        """
        Get the temperature in Celsius with + in front of it for positive values.
        :return: temperature as a String in expected format
        """
        if self.temperature > 0:
            return '+{}'.format(self.temperature)
        else:
            return str(self.temperature)

    def to_string(self):
        """
        Return a row with all city information.
        :return: a string with all the city information
        """
        return '|'.join([self.city.name,  ','.join([str(self.city.lon), str(self.city.lat), str(self.city.elevation)]),
                         self.timestamp, self.condition, self.get_temperature(), str(self.pressure), self.humidity])







