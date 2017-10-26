from city import City


def test_builder():
    """
    Unit test case to build a city by its name and city code
    """
    toulouse = City('Toulouse', 'fr')
    assert toulouse.name == 'Toulouse'
    assert toulouse.country == 'fr'
    empty_city = City('', '')
    assert empty_city.name == ''
    assert empty_city.country == ''

def test_get_postion():
    """
    Unit test case to get position of a city by its name and city code
    """
    toulouse = City('Toulouse', 'fr')
    toulouse.get_position()
    assert toulouse.lat == 43.6
    assert toulouse.lon == 1.44

