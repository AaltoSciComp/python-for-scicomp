#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import weather_functions

url = "https://raw.githubusercontent.com/AaltoSciComp/python-for-scicomp/master/resources/data/scripts/weather_tapiola.csv"
weather = pd.read_csv(url,comment='#')

# define the start and end time for the plot 
start_date=pd.to_datetime('01/06/2021',dayfirst=True)
end_date=pd.to_datetime('01/10/2021',dayfirst=True)
#Preprocess the data
weather['Local time'] = pd.to_datetime(weather['Local time'],dayfirst=True)
# select the data
weather = weather[weather['Local time'].between(start_date,end_date)]

# Now, we have the data loaded, and adapted to our needs. So lets get plotting
import matplotlib.pyplot as plt
# start the figure.
fig, ax = plt.subplots()
ax.plot(weather['Local time'], weather['T'])
# label the axes
ax.set_xlabel("Date of observation")
ax.set_ylabel("Temperature in Celsius")
ax.set_title("Temperature Observations")
# adjust the date labels, so that they look nicer
fig.autofmt_xdate()
# save the figure

# save the figure
fig.savefig('weather.png')



