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

This small project introduce a way to generate fake weather data with a very small code base. 
The weather data is generated for the following cities:
- Sydney
- Darwin
- Paris
- Toulouse
- ...


## Training the model

```
0%                                        Training on next 50 batches                                        100%
Toulouse|1.44,43.6,150|2049-01-10T09:36:52Z|Sunny|+9.6|1018.8|71.0         |\ │ ||||....,,,,,,,,,222221100000011111000||||||||||||||||||||||....         | │ loss: 1.86959
Lyon|4.85,45.75,213|2046-06-17T18:40:21Z|Sunny|+19.8|1006.3|33.0           |\ │  |n||....,,,,,,,,,22222000000111111111111|||||||||||||||||.              | │ loss: 1.84344
Marseille|5.38,43.3,12|2037-04-21T13:44:11Z|Rain|+17.2|1000.6|88.0         |\ │   ||||....,,,,,,,,,222222111111111111111111|||||||||||||||||..           | │ loss: 1.84305
Juneau|-134.42,58.3,17|2038-07-13T18:52:03Z|Sunny|+5.5|1015.7|67.0         |\ │   ||||....,,,,,,,,,2222210000001111111111||||||||||||||||||||...         | │ loss: 1.86522
Sydney|151.21,-33.87,19|2047-02-23T00:21:35Z|Sunny|+14.7|1023.5|56.0       |\ │ a|||....,,,,,,,,,222221000000111111100|||||||||||||||||||||||||....        │ loss: 1.93841
Tignes|6.92,45.5,3747|2011-03-06T04:16:08Z|Rain|+11.4|975.8|57.0           |\ │  ||||....,,,,,,,,2222222000011111111111|||||||||||||||||||||....         | │ loss: 1.87802
Darwin|130.84,-12.46,37|2035-09-28T07:04:05Z|Sunny|+19.7|1014.2|38.0       |\ │   nn||....,,,,,,,,2222111100111111111111|||||||||||||||||||||.....         │ loss: 1.93052
Montreal|-73.59,45.51,35|2037-10-30T15:34:01Z|Sunny|+9.7|1017.2|62.0       |\ │   nn||....,,,,,,,,222222000000011111111|||||||||||||||||||||||....         │ loss: 1.95017
San Fransisco|-122.42,37.77,16|2027-08-23T19:39:31Z|Sunny|+20.7|1003.9|57.0|\ │  |||s....,,,,,,,,,22222111111011111000000|||||||||||||||||||||||||||....   │ loss: 2.31931
Paris|2.35,48.85,35|2010-09-27T18:29:55Z|Rain|+24.5|1001.0|74.0            |\ │   ||||....,,,,,,,,22222200000111111111111||||||||||||||||..              | │ loss: 1.85471

TRAINING STATS: batch 0/1000 in epoch 0,     batch loss: 4.01799, batch accuracy: 0.32451
```

```
()
0%                                        Training on next 50 batches                                        100%
()
459000 (epoch 0) train_RNN.txt │ Toulouse|1.44,43.6,150|2034-01-20T05:52:20Z|Rain|+13.5|1011.6|74.0                                  |\ │ ansess||1.44444..,,,1|2002-01--11T1::::44Z|Sunn|+11..|1100..|88.0                                   \T │ loss: 0.97499
459102 (epoch 0) train_RNN.txt │ Lyon|4.85,45.75,213|2025-12-29T20:10:31Z|Rain|+17.0|994.6|86.0                                      |\ │ anns|...5,,55.5,,172202-00--12TT:1::4:Z|Sunny+11..|110..|88.0                                       \T │ loss: 1.07746
459204 (epoch 0) train_RNN.txt │ Marseille|5.38,43.3,12|2012-07-01T14:46:00Z|Sunny|+25.5|1005.4|53.0                                 |\ │ arneilll|3...,,3..,,,22202-01--1TT1:3::44ZZSunny|+11..|110...|7..0                                  \T │ loss: 0.98274
459306 (epoch 0) train_RNN.txt │ Juneau|-134.42,58.3,17|2037-02-26T13:29:17Z|Sunny|+5.7|1035.1|91.0                                  |\ │ anneu||111.44,,3..,,17200--01--11T1:1::42Z|Sunny|+1...|110...77.0                                   \T │ loss: 1.10525
459408 (epoch 0) train_RNN.txt │ Sydney|151.21,-33.87,19|2032-09-28T22:47:35Z|Rain|+9.6|966.2|83.0                                   |\ │ anneu||11.44,,,3...,,17200--01--11TT:1::42Z|Sunny++1..|100...8..                                    \T │ loss: 1.23591
459510 (epoch 0) train_RNN.txt │ Tignes|6.92,45.5,3747|2047-05-06T02:53:09Z|Rain|+12.9|992.3|74.0                                    |\ │ arnee||..44,,5..,,,1|2002-01--12T1::::44Z|Sunn|+11..|110..|88.0                                     \T │ loss: 1.11045
459612 (epoch 0) train_RNN.txt │ Darwin|130.84,-12.46,37|2048-02-14T04:43:41Z|Sunny|+33.3|1023.9|21.0                                |\ │ annea||11..4,,,3...,,172002-01--11T1::::42Z|Sunny|+11..|110...|7..0                                 \T │ loss: 1.15091
459714 (epoch 0) train_RNN.txt │ Montreal|-73.59,45.51,35|2021-05-17T13:37:23Z|Sunny|+6.3|992.9|70.0                                 |\ │ ontraall--3...,,5555,,55200--01--11T1:1::4:Z|Sunny|+1..||110.....0                                  \M │ loss: 1.12154
459816 (epoch 0) train_RNN.txt │ San Fransisco|-122.42,37.77,16|2018-12-22T17:18:33Z|Rain|+9.1|1001.3|89.0                           |\ │ areFrassssccc|122222,,7.777,172001-01--11TT:1::44Z|Sunny++1..|1100...8..                            \M │ loss: 1.16868
459918 (epoch 0) train_RNN.txt │ Paris|2.35,48.85,35|2018-03-15T19:30:41Z|Sunny|+12.8|1027.0|57.0                                    |\ │ anne||..5,,,5.5,,3|2002-01--12T1:3::4:Z|Sunny|+11..|1100..|7..0                                     \T │ loss: 0.93028
```