from weather import *
from city import City
"""
Tests for Weather class
"""


def test_builder():
    """
    Unit test case to build a city by its name and city code
    """
    date = generate_date()
    weather_toulouse = Weather(City('Toulouse', 'fr', 'C', 35), date)
    assert weather_toulouse.city.name == 'Toulouse'
    assert weather_toulouse.city.elevation == 35


def test_compute_theoretical_pressure():
    assert compute_theoretical_pressure(0) == 1013.25
    assert compute_theoretical_pressure(-50) > 1013.25
    assert compute_theoretical_pressure(50) < 1013.25


def test_generate_date():
    random_date = generate_date()
    print(random_date)
    assert len(random_date) == 20
    assert random_date[0] == '2'
    assert random_date[10] == 'T'
    assert random_date[19] == 'Z'
