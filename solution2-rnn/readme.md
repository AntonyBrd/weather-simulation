# Simulate Weather using a Recurrent Neural Network 

<div>
  <div align="center">
    <a href="https://leonardoaraujosantos.gitbooks.io/artificial-inteligence/">
      <img src="https://leonardoaraujosantos.gitbooks.io/artificial-inteligence/content/image_folder_6/recurrent.jpg" alt="Deep Learning Theory" />
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


The code used in that solution has been created by Martin Gorner. I had the pleasure to met him 
twice in Toulouse, he is very inspiring and make deep learning accessible to (almost) everybody.
The complete code he wrote can be found
[on his Githib repository](https://github.com/martin-gorner/tensorflow-rnn-shakespeare).

# Theoretical aspect of the solution

[!](../resources/RNN.BDU.dataflow.png)

# Practical aspect of the solution

## Gathering input data

For now, we are using the output of solution 1 to train the model. Of course, it would be better to gather real data.

## Training the model

At the beginning, the model is completely wrong, producing rows that does not make any sens.
The only thing that have been dreaded is the delimiter. As a consequence, the loss is very high, and the accuracy is low.

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

As the input pattern is very repetitive and quite simple to copy, 9 batches are enough
for the model to replicate the data structure. The loss is now 4 times lower than it was during the first batch.
```
()
0%                                        Training on next 50 batches                                        100%
()
Toulouse|1.44,43.6,150|2034-01-20T05:52:20Z|Rain|+13.5|1011.6|74.0      |\ │ ansess||1.44444..,,,1|2002-01--11T1::::44Z|Sunn|+11..|1100..|88.0       \T │ loss: 0.97499
Lyon|4.85,45.75,213|2025-12-29T20:10:31Z|Rain|+17.0|994.6|86.0           |\ │ anns|...5,,55.5,,172202-00--12TT:1::4:Z|Sunny+11..|110..|88.0            \T │ loss: 1.07746
Marseille|5.38,43.3,12|2012-07-01T14:46:00Z|Sunny|+25.5|1005.4|53.0      |\ │ arneilll|3...,,3..,,,22202-01--1TT1:3::44ZZSunny|+11..|110...|7..0       \T │ loss: 0.98274
Juneau|-134.42,58.3,17|2037-02-26T13:29:17Z|Sunny|+5.7|1035.1|91.0       |\ │ anneu||111.44,,3..,,17200--01--11T1:1::42Z|Sunny|+1...|110...77.0        \T │ loss: 1.10525
Sydney|151.21,-33.87,19|2032-09-28T22:47:35Z|Rain|+9.6|966.2|83.0        |\ │ anneu||11.44,,,3...,,17200--01--11TT:1::42Z|Sunny++1..|100...8..         \T │ loss: 1.23591
Tignes|6.92,45.5,3747|2047-05-06T02:53:09Z|Rain|+12.9|992.3|74.0         |\ │ arnee||..44,,5..,,,1|2002-01--12T1::::44Z|Sunn|+11..|110..|88.0          \T │ loss: 1.11045
Darwin|130.84,-12.46,37|2048-02-14T04:43:41Z|Sunny|+33.3|1023.9|21.0     |\ │ annea||11..4,,,3...,,172002-01--11T1::::42Z|Sunny|+11..|110...|7..0      \T │ loss: 1.15091
Montreal|-73.59,45.51,35|2021-05-17T13:37:23Z|Sunny|+6.3|992.9|70.0      |\ │ ontraall--3...,,5555,,55200--01--11T1:1::4:Z|Sunny|+1..||110.....0       \M │ loss: 1.12154
San Fransisco|-122.42,37.77,16|2018-12-22T17:18:33Z|Rain|+9.1|1001.3|89.0|\ │ areFrassssccc|122222,,7.777,172001-01--11TT:1::44Z|Sunny++1..|1100...8.. \M │ loss: 1.16868
Paris|2.35,48.85,35|2018-03-15T19:30:41Z|Sunny|+12.8|1027.0|57.0         |\ │ anne||..5,,,5.5,,3|2002-01--12T1:3::4:Z|Sunny|+11..|1100..|7..0          \T │ loss: 0.93028
()
TRAINING STATS: batch 450/1000 in epoch 0,   batch loss: 1.08582, batch accuracy: 0.62745```
```


After a few minutes, the progression of the accuracy is very slow and tend to a maximum.
Without some parameter tuning it is not interesting to keep training the model. 


![](resources/Tensorboard_RNN.jpg "Accuracy and loss stabilisation")


But when we look at the data that the model is able to generate, we can see that we are very close to the reality.

```
()
0%                                        Training on next 50 batches                                        100
()
Toulouse|1.44,43.6,150|2031-07-26T08:52:53Z|Sunny|+20.8|1018.4|94.0       |\ │ oulouse|1.44,43.6,150|2020-02-15T12:22:22Z|Sunny|+10.1|1017.1|54.0           |\P │ loss: 0.37877
Lyon|4.85,45.75,213|2030-12-14T21:06:32Z|Rain|+16.0|1014.7|72.0            |\ │ yon|4.85,45.75,213|2020-02-16T10:42:42Z|Rain|+11.1|1000.5|84.0               |\T │ loss: 0.37483
Marseille|5.38,43.3,12|2040-10-24T10:46:24Z|Sunny|+19.6|1040.9|41.0        |\ │ arseille|5.38,43.3,12|2044-02-12T12:22:42Z|Runny|+10.1|1011.1|54.0           |\L │ loss: 0.39041
Juneau|-134.42,58.3,17|2040-03-31T23:39:48Z|Sunny|-0.4|998.1|66.0          |\ │ uneau|-134.42,58.3,17|2020-02-15T12:22:12Z|Sunny|+1.2|198.5|78.0             |\M │ loss: 0.41933
Sydney|151.21,-33.87,19|2048-11-07T19:19:02Z|Rain|+18.5|1008.1|83.0        |\ │ ydney|151.21,-33.87,19|2042-02-16T12:22:12Z|Sain|+12.2|1007.8|88.0           |\J │ loss: 0.35442
Tignes|6.92,45.5,3747|2025-12-18T08:29:13Z|Rain|+17.8|1014.9|74.0          |\ │ ignes|6.92,45.5,3747|2040-02-19T00:02:12Z|Rain|+11.1|1000.5|88.0             |\S │ loss: 0.38278
Darwin|130.84,-12.46,37|2016-03-02T09:14:43Z|Sunny|+36.2|1027.1|14.0       |\ │ arwin|130.84,-12.46,37|2041-02-05T03:52:11Z|Sunny|+20.9|1018.1|24.0          |\T │ loss: 0.35441
Montreal|-73.59,45.51,35|2008-10-12T02:45:11Z|Sunny|+10.9|1033.6|52.0      |\ │ ontreal|-73.59,45.51,35|2042-02-19T12:22:22Z|Runny|+10.1|1011.1|74.0         |\D │ loss: 0.36828
San Fransisco|-122.42,37.77,16|2035-06-05T02:27:37Z|Sunny|+27.4|1018.6|32.|\ │ an Fransisco|-122.42,37.77,16|2044-02-15T13:22:22Z|Sunny|+10.9|1015.1|54.0   |\M │ loss: 0.40290
Paris|2.35,48.85,35|2021-02-13T18:15:16Z|Sunny|+16.8|1022.8|56.0           |\ │ aris|2.35,48.85,35|2020-02-12T00:02:42Z|Runny|+10.1|1017.5|54.0              |\S │ loss: 0.37246
()
TRAINING STATS: batch 750/1000 in epoch 2,   batch loss: 0.37986, batch accuracy: 0.8451
```

## Run the RNN

Now, let's the model speak on its own:

```
Marseille|5.38,43.3,12|2035-11-11T01:11:11Z|Rain|+13.7|1011.3|76.0                                 
Lyon|4.85,45.75,213|2020-10-10T10:55:15Z|Rain|+11.7|1011.3|72.0                             
Toulouse|1.42,43.6,150|2035-07-25T03:55:11Z|Sunny|+13.1|1013.7|62.0                                 
Paris|2.35,48.85,35|2049-07-15T01:15:11Z|Rain|+11.7|1001.7|76.0                                     
San Fransisco|-122.42,37.77,19|2031-09-10T11:14:55Z|Sunny|+11.3|1014.7|42.0                         
Montreal|-73.59,45.55,35|2031-07-11T01:14:17Z|Snow|+1.3|984.9|82.0                                  
Darwin|130.84,-12.46,37|2031-11-25T01:54:15Z|Sunny|+21.3|1033.1|22.0                                
Tignes|6.92,45.5,3747|2035-09-25T05:55:51Z|Sunny|+25.2|1013.7|62.0                                  
Sydney|151.21,-33.87,19|2035-09-11T11:54:11Z|Sunny|+21.3|1024.7|62.0                                
Juneau|-134.42,58.3,17|2010-07-15T03:15:55Z|Snow|+2.2|1001.2|89.0                                   
Marseille|5.38,43.3,12|2045-11-10T11:11:15Z|Rain|+13.7|1011.3|76.0                                  
Lyon|4.85,45.75,213|2025-11-23T10:51:51:|Rain|+11.7|1011.3|81.0                                     
Toulouse|1.44,43.6,150|2010-07-27T13:51:11Z|Rain|+14.1|1001.7|76.0                                  
Paris|2.35,48.85,35|2045-07-27T05:55:15Z|Rain|+15.7|1001.5|82.0                                     
San Fransisco|-122.42,37.77,16|2011-10-23T00:51:11Z|Rain|+13.1|984.6|86.0                           
Montreal|-73.59,45.51,35|2031-07-27T02:55:55Z|Sunny|+21.3|1023.2|72.0                               
Darwin|130.84,-12.46,37|2011-12-12T12:14:11Z|Sunny|+23.3|1033.1|11.0                                
Tignes|6.92,45.5,3747|2015-07-29T15:11:15Z|Sunny|+11.1|994.7|52.0                                   
Sydney|151.21,-33.87,19|2010-11-11T01:14:41Z|Rain|+9.7|1001.3|81.0                                  
Juneau|-134.42,58.3,17|2015-09-17T13:15:11Z|Snow|+3.3|1001.2|89.0                                   
Marseille|5.38,43.3,12|2030-07-23T11:51:15Z|Rain|+13.1|1013.1|76.0                                  
Lyon|4.85,45.75,213|2020-07-11T11:55:11Z|Rain|+11.7|999.6|76.0                                      
Toulouse|1.44,43.6,150|2035-07-27T13:14:11Z|Sunny|+13.1|1013.7|62.0                                
Paris|2.35,48.85,35|2045-11-13T11:55:55Z|Sunny|+13.3|996.7|52.0                              
San Fransisco|-122.42,37.77,16|2035-09-25T13:51:11Z|Rain|+13.7|1001.3|72.0                    
Montreal|-73.59,45.51,35|2045-07-25T12:55:11Z|Rain|+15.7|1003.2|82.0                           
Darwin|130.84,-12.46,37|2035-07-15T11:15:51Z|Sunny|+12.3|1033.3|20.0                             
Tignes|6.99,45.5,3747|2015-09-29T13:55:51Z|Sunny|+11.1|1014.7|62.0                                  
Sydney|151.21,-33.87,19|2010-11-11T01:44:11Z|Sunny|+21.1|1013.4|41.0     
```

Whereas cities follow the define order that we gave in the input file (), the date and the weather data
has been generated, and it is very loyal to the rules we defined in the first solution.

## RNN known limitation

Keep in mid that the data structure remain the same all the time. Also, . As a consequence, building a model that 
produce real text, sounds or images will be far more complicated, and it will need a tremendously longer computation
time to train.

Indeed, RNN may need to remember all previous states at any given time. If you are processing a lot of data, we will
need a huge amount computational resources. Of course, we can use only a part of these previous states in keeping only a
 time window.

With RNN we may encounter issues with gradient descent, such as
[Vanishing](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) or
Exploding gradient (see [this article](http://www.cs.toronto.edu/~rgrosse/courses/csc321_2017/readings/L15%20Exploding%20and%20Vanishing%20Gradients.pdf)
from Toronto University). Just notice that you may waste your time in training for 100 epochs, as the model will quickly
 stop to get better. In my example I've stopped the training at 2.5 epochs, and I could have stopped it at 1.5.

## Source

Free lecture on Deep Learning with Tensor Flow : [Big Data University](https://cognitiveclass.ai/courses/deep-learning-tensorflow/)

https://leonardoaraujosantos.gitbooks.io/artificial-inteligence/