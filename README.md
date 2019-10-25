# ScotClimateStripes
Python script and some example datasets related to the plotting of climate change (temperature or sea level rise) as vertical stripes, a la [Ed Hawkins](twitter.com/ed_hawkins) ([#ShowYourStripes](https://showyourstripes.info/), University of Reading).

The methodology for visualising the climate data is exactly the same as ShowYourStripes; the only difference is that this is a Python version for *sea level rise* data (specifically from around Scotland), whereas ShowYourStripes are ordinarily *temperature* related.

The data used for plotting here is from the [Permanent Service for Mean Sea Level](https://www.psmsl.org) (PSMSL) which gives monthly mean sea level at a number of buoys across the globe. The monthly mean values are extracted from the CSV files provided, converted to an annual mean for each year of the buoy's operation, and then normalised to the full time-series mean to give the hotter or colder/higher or lower than average colormap used in plotting. Then the striped are visualised.

*F Muir, Oct 2019*
