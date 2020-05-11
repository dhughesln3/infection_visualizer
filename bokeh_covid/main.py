# Bokeh basics
from bokeh.io import curdoc


#import the plot function from its file
from scripts.get_plot import plot

#run the plot!
curdoc().add_root(plot())
