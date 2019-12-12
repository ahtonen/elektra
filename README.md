# ARC 2019

This repository contains Python scripts that were developed onboard S/y Elektra, [Marsaudon Composites TS42](http://catamaran-ts42.com), during the Atlantic Ocean crossing from Las Palmas, Canary Islands, to Rodney Bay, Saint Lucia. In this crossing we were boat #150 in *Multihull division* of [ARC2019](https://www.worldcruising.com/arc/event.aspx)

## Optimum true wind angles
`computeVMG.py` script had its motivation in finding the optimum true wind angle (TWA) downwind for maximising velocity made good (VMG).

The only performance data available for this task were polars from a sister boat, S/y Guyander, in `Guyader-gastronomieV1.pol`.

Since the data were already in tabular format, I decided to use Pandas and Numpy to make the trigonometric computations that are needed for VMG speeds.

## Race statistics
At high seas a modern fast Internet connection is something that is typically not available without costs of thousands of USDs. Most often information is transmitted in very compressed email format and files over 50kB are avoided. Iridium Go that we used had a data call rate of 9600bps. Back to modem age, in other words.

Hence, the race tracker in ARC organizers web pages was out ot question. The only information we got was an email of other competitors positions (latitude and longitude) that came every 4th hour.

Example snippet:

``POSADRENA
1;161;27.4480N;15.3736W;11/27/19 12:00:13
1;153;26.5780N;16.5668W;11/29/19 00:00:13
1;42;19.1270N;24.4375W;11/29/19 00:00:13
1;132;23.1692N;21.1077W;11/29/19 00:00:05
...``

Since this was also nicely in tabular format I put it into a Pandas dataframe. Combined with a file that had competitor boats' numbers and names I could aggregate a master dataframe that contained all positions for all boats since the start of the race.

After that it was rather straightforward to add more features. First thing that was added was an average velocity of each close opponent. Also distance to us was interesting. And how much each boat has still to go before reaching the finish.

Race statistics combined with the weather routing program, weather forecasts and positions on the map provided us a very neat tool to guess strategies of other boats and revise ours each day, many times, as we got new position reports.

## Data science in a racing catamaran

For those interested data science during free watches, or when I was not helming in watch, having sleep deprivation, in screaming and shaking boat and during middle of night is, I must say, an interesting experience.

Additional challenge is that there is no Internet were you could Google how others have solved the problem. No API or framework documentation either. Except if you have downloaded them to your computer before departure. I had done it for Pandas and Numpy that probably made this whole exercise possible.

Good luck is always needed. Also in sailing and weather routing :)