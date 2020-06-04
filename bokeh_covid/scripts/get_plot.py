import bokeh.plotting.figure as bk_figure
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider
import numpy as np
from scripts.get_infections import get_infections



def plot():

    # Set up initial parameters
    x = range(11)
    y = get_infections(10,.2, 1, 2)
    source = ColumnDataSource(data=dict(x=x, y=y))

    # Set up plot
    plot = bk_figure(plot_height=400, plot_width=600, title="Probability Distribution for the Number of Infected People",
                  tools="crosshair,pan,reset,save,wheel_zoom",
                  x_range=[0, 10], y_range=[0, 1])



    plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

    # Set up widgets
    trans_prob = Slider(title="Person-to-person transmission probability", value=0.2, start=0.0, end=1.0, step=0.01)
    population = Slider(title="Community population", value=10, start=0, end=140, step=1)
    prop_infected = Slider(title="Initial proportion of population infected", value=.2, start=0.0, end=1, step=.01)
    days = Slider(title="Number of days", value=1, start=1, end=14, step=1)
    mean = Paragraph(text="Expected number of infected people: "+str(round(E(y),2)))




    # Set up callbacks
    def update_title(attrname, old, new):
        plot.title.text = text.value



    def update_data(attrname, old, new):
        # Get the current slider values
        t = trans_prob.value
        pop = population.value
        inf = prop_infected.value
        d = days.value

        # Generate the new curve
        x = range(pop+1)
        y = get_infections(pop, t, d, int(inf*pop))

        # update expectation
        mean.text="Expected number of people infected: "+str(round(E(y),2))

        #re-scale so that relevant part of x-axis stays in view
        plot.x_range.end=0
        plot.x_range.end=pop




        source.data = dict(x=x, y=y)


    for w in [trans_prob,population,prop_infected,days]:
        w.on_change('value', update_data)




    # Set up layouts and add to document
    inputs = widgetbox(population,trans_prob,prop_infected,days,mean)
    layout = row(plot,
                 widgetbox(population,trans_prob,prop_infected,days,mean))



    def modify_doc(doc):
        doc.add_root(row(layout, width=800))
        doc.title = "Sliders"
        text.on_change('value', update_title)




    return layout
