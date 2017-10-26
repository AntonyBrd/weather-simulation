import json
from pprint import pprint
from city import City
from weather import Weather, generate_date

def main():

    with open('./data/test_set.json') as data_file:
        data = json.load(data_file)
    text_file = open("./weather_output.txt", "w")

    for _ in xrange(10):
        for record in data:
            print('----------------')
            pprint(record)
            tmp_city = City.build_from_json(record)
            print 'City name :' + tmp_city.name
            print tmp_city.to_string()
            tmp_weather = Weather(tmp_city, generate_date())
            text_file.write(tmp_weather.to_string() + '\n')

    text_file.close()

if __name__ == '__main__':
    main()
