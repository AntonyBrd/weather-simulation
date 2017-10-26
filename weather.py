from city import City
# 3 possible condition states for weather
CONDITIONS = ['Snow', 'Rain', 'Sunny']

# We consider the following
CLIMATES = []


def compute_theoretical_pressure(h):
    """
    Compute pressure from elevation according to the international formula of barometric leveling.
    :param: h is the elevation
    :return: p the theoretical pressure
    """
    return 1013.25 * (1 - (0.0065 * h / 288.15) ** 5.255)


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


