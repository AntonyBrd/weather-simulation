import json
from pprint import pprint
from city import City
from weather import Weather, generate_date


def make_len_100(row):
    if len(row) > 100:
        return row[0:99]
    elif len(row) < 100:
        return row.ljust(100)


def main(num_iter=1000):
    """
    Main job for this weather simulation application.
    """

    # Create an empty city list
    city_list = []

    # Open input json file containing all city information
    with open('../data/test_set.json') as data_file:
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
    for i in xrange(num_iter):
        if (i % 10) == 0:
            print('Iteration {} / {}'.format(i, num_iter))
        for city in city_list:
            tmp_weather = Weather(city, generate_date())
            text_file.write(make_len_100(tmp_weather.to_string()) + '|\n')
    text_file.close()

if __name__ == '__main__':
    main()
