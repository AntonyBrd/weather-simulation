from bokeh.sampledata import us_states
from bokeh.plotting import *

us_states = us_states.data.copy()

del us_states["HI"]
del us_states["AK"]

# separate latitude and longitude points for the borders
#   of the states.
state_xs = [us_states[code]["lons"] for code in us_states]
state_ys = [us_states[code]["lats"] for code in us_states]

# init figure
p = figure(title="Plotting Points Example: The 5 Largest Cities in Texas",
           toolbar_location="left", plot_width=1100, plot_height=700)

# Draw state lines
p.patches(state_xs, state_ys, fill_alpha=0.0,
    line_color="#884444", line_width=1.5)

#  Latitude and Longitude of 5 Cities
# ------------------------------------

# Now group these values together into a lists of x (longitude) and y (latitude)
x = [-97.7431, -96.79, -97.33, -95.36, -98.49]
y = [30.26, 32.77, 32.75, 29.76, 29.42]

# The scatter markers
p.circle(x, y, size=8, color='navy', alpha=1)

# output to static HTML file
output_file("texas.html")

# show results
show(p)