import json
from pprint import pprint
from city import City
from weather import Weather, generate_date


def main():
    """
    Main job for this weather simulation application.
    """

    # Create an empty city list
    city_list = []

    # Open input json file containing all city information
    with open('./data/test_set.json') as data_file:
        data = json.load(data_file)

    # Add each input city in the city list
    for record in data:
        tmp_city = City.build_from_json(record)
        print('Loading city ' + tmp_city.name)
        pprint(record)
        city_list.append(tmp_city)
        print 'City as a string : \"{}'.format(tmp_city.to_string())

    # Do 10 weather simulation for each city and write the outcome to a text file
    text_file = open("./weather_output.txt", "w")
    for _ in xrange(9):
        for city in city_list:
            tmp_weather = Weather(city, generate_date())
            text_file.write(tmp_weather.to_string() + '\n')
    text_file.close()

if __name__ == '__main__':
    main()
