from city import City
"""
Tests for City class
"""


def test_builder():
    toulouse = City('Toulouse', 'fr', 'C', 35)
    assert toulouse.name == 'Toulouse'
    assert toulouse.country == 'fr'
    empty_city = City('', '', '', '')
    assert empty_city.name == ''
    assert empty_city.country == ''


def test_get_coord():
    toulouse = City('Toulouse', 'fr', 'C', 35)
    toulouse.get_coord()
    assert toulouse.lat == 43.6
    assert toulouse.lon == 1.44


def test_to_string():
    toulouse = City('Toulouse', 'fr', 'C', 35)
    assert toulouse.to_string().startswith('Toulouse|')
