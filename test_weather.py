from weather import *
from city import City
"""
Tests for Weather class
"""


def test_builder():
    timestamp = generate_date()
    weather_toulouse = Weather(City('Toulouse', 'fr', 'C', 35), timestamp)
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
    assert datetime.strptime(random_date, '%Y-%m-%dT%H:%M:%SZ') is not None


def test_is_summer():
    toulouse = City('Toulouse', 'fr', 'C', 35)
    assert Weather(toulouse, "2028-06-12T00:08:29Z").is_summer()
    assert Weather(toulouse, "2028-08-12T00:08:29Z").is_summer()
    assert Weather(toulouse, "2028-09-12T00:08:29Z").is_summer()
    assert not Weather(toulouse, "2028-11-12T00:08:29Z").is_summer()
    sydney = City('Sydney', 'au', 'B', 12)
    assert Weather(sydney, "2028-11-12T00:08:29Z").is_summer()
    assert Weather(sydney, "2028-12-12T00:08:29Z").is_summer()
    assert Weather(sydney, "2028-02-12T00:08:29Z").is_summer()
    assert not Weather(sydney, "2028-08-12T00:08:29Z").is_summer()


def test_generate_pressure():
    toulouse = City('Toulouse', 'fr', 'C', 35)
    weather_toulouse = Weather(toulouse, "2028-06-12T00:08:29Z")
    assert (500 < weather_toulouse.generate_pressure() < 1500)
    assert (500 < weather_toulouse.generate_pressure() < 1500)
    assert (500 < weather_toulouse.generate_pressure() < 1500)

