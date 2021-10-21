#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import weather_functions

url = "https://raw.githubusercontent.com/tpfau/python-for-scicomp/ScriptUpdate/ressources/data/scripts/weather_tapiola.csv"
weather = pd.read_csv(url,comment='#')

# define the start and end time for the plot 
start_date=pd.to_datetime('01/06/2021',dayfirst=True)
end_date=pd.to_datetime('01/10/2021',dayfirst=True)
weather = weather_functions.preprocessing(weather,start_date,end_date)

# Now, we have the data loaded, and adapted to our needs. So lets get plotting
plt,fig = weather_functions.plot_data(weather['Local time'], weather['T'])
# save the figure
plt.savefig('weather.png')



