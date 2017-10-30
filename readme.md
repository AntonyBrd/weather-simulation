# Simulate Weather with Python

<div>
  <div align="center">
    <img src="https://cdn.yourstory.com/wp-content/uploads/2015/05/yourstory_climate_change1.jpg" alt="intro"/>
  </div>
  <div align="center">
    <a href="https://travis-ci.org/AntonyBrd/weather-simulation">
      <img src="https://travis-ci.org/AntonyBrd/weather-simulation.svg?branch=master" alt="Build Status" />
    </a>
  </div>
<div>

# Introduction


Imagine you need you create weather data. Ne need to try to predict tomorrow's conditions,
just propose a plausible weather report using the following format:


| Location | Position          |Local Time |Conditions |Temperature | Pressure | Humidity |
|----------|:-----------------:|----------:|----------:|-----------:|---------:|---------:|
| Paris | 2.35,48.85,35|2049-07-15T01:15:11Z|Rain|+11.7|1001.7|76.0|                                     
| Montreal|-73.59,45.55,35|2031-07-11T01:14:17Z|Snow|+1.3|984.9|82.0 |                                 
| Darwin|130.84,-12.46,37|2031-11-25T01:54:15Z|Sunny|+21.3|1033.1|22.0 |                               
| Sydney|151.21,-33.87,19|2035-09-11T11:54:11Z|Sunny|+21.3|1024.7|62.0  |                              
| Marseille|5.38,43.3,12|2045-11-10T11:11:15Z|Rain|+13.7|1011.3|76.0  |                                
| Toulouse|1.44,43.6,150|2010-07-27T13:51:11Z|Rain|+14.1|1001.7|76.0  |                                


This small project introduce two solutions to generate fake weather data. 
The weather data is generated for the following cities:
- Sydney
- Darwin
- Paris
- Toulouse
- ...


# Solutions

The reader is invited to check each solution in their specific folder:
- [Solution 1](solution1-business-rules/readme.md) : Gaussian randomness and business rules
- [Solution 2](solution2-rnn/readme.md) : Create a Recurrent Neural Network that is able to produce fake data

We may need to understand the solution 1 to get the second one.
Of course, the best way to answer the problem would be a combination of the two solutions.