from city import City
import numpy as np
import datetime
import time
# 3 possible condition states for weather
CONDITIONS = ['Snow', 'Rain', 'Sunny']

# We consider the following
CLIMATES = ['A', 'B', 'C', 'D', 'E']


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


def gaussian(mean, sd):
    np.random.normal(mean, sd, 1)


def generate_date(start_date=datetime.date(2000, 01, 02), end_date=datetime.date(2050, 01, 01)):
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
    return datetime.datetime.utcfromtimestamp(ts_rand).strftime('%Y-%m-%dT%H:%M:%SZ')




class Weather:
    """
     - Local time is an ISO8601 date time,
    - Conditions is either Snow, Rain, Sunny,
    - Temperature is in Celsius,
    - Pressure is in hPa, and
    - Relative humidity is a %.
    """

    def __init__(self, city, date):
        """
        Builder for Weather object.
        :param city: 
        :param date: 
        """
        if city.__class__ != City:
            raise "First argument has to be a City."
        else:
            self.city = city
        self.date = date


