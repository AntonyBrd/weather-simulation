# Simulate Weather with Python

This small project introduce a way to generate fake weather data with a very small code base. 
The weather data is generated for the following cities:
- Sydney
- Perth
- Melbourne
- Adelaide
- Darwin
- Ockland

## How to use the application

### Pre requirements
- Python 2.7
- install pip
- run the following command
```bash
pip intall -r requirement.txt
```

Generating data files is as simple as running the command :
```
python main.py
```

Once `pytest` is installed, you can run unit tests with:
```
pytest
```
 


## The approach

### Step 1: Defining different climate types

To be accurate on climate, we are going to use the
[Koppen climate classification](https://en.wikipedia.org/wiki/K%C3%B6ppen_climate_classification),
which is largely used and accepted. This classification has different level of
precision, to keep it simple let just use the following groups:
- **A** Tropical 
- **B** Arid
- **C** Temperate
- **D** Cold
- **E** Polar

Each group will have a specific 
 
### Step 2: Create a list of city and get their climate

2.a Create a json file with city name and country

2.b Attribute a climate to each city <br>
_NB: We could make this step automatic by crawling into the Wikipedia page of the concerned City. 
There is a [Wikipedia Python package](https://pypi.python.org/pypi/wikipedia) that could help to do so._ 

2.c Set manually the city elevation in json data <br>
_NB: This step should also be automatic if my first API choice have been smarter_

### Step 3: Use an API to get City position



### Step 4: Simulate data

#### Relations between weather variables


 
### Step 5: Write the results to a file

## How to improve this application

There are many ways to improve this project, let's try to make it smarter.

### Solve TODOs

The way the elevation is handled is quite bad. [Here](https://visibleearth.nasa.gov/view.php?id=73934),
you can find an image of the world map with evelation for red values.

### Use better "business" rules (here: physical models)

First of all, we would need to use time zone to get day/night information. This will widely 
improve temperature accuracy.

There are many climate models that provide great estimation of the weather.
Working with people that have a good understanding of these model would definitely improve the
application.

### Use Machine Learning 

There are Neural Network specialised in data generation that it would be great to test.
For example, RNN are able to write theatre piece that have a very good structure, with a lot of input data we could 
generate data for cities that does not even exist. 

Here is a very nice example of how to build a RNN with Tensorflow :
https://github.com/martin-gorner/tensorflow-rnn-shakespeare

### Plot this data on a world map

The current output is a flat file, which is not really funny to read. Python package like `bokeh` and
many others will help to create nice visualisation.



