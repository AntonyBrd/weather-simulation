import json
from pprint import pprint
from city import City





def main():
    with open('./data/test_set.json') as data_file:
        data = json.load(data_file)

    for record in data:
        print('---')
        pprint(record)
        tmp_city = City.build_from_json(record)
        print 'City name :' + tmp_city.name


if __name__ == '__main__':
    main()
