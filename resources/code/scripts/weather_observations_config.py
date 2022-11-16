#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from optionsparser import get_parameters
import argparse 

# Lets start reading our confg file. we'll use argparse to get the config file.
parser = argparse.ArgumentParser()
parser.add_argument('input', type=str,
                    help="Config File name ")
args = parser.parse_args()

# Set optional parameters with default values and required parameter values with their type
defaults = {
           "xlabel"      : "Date of observation",
           "title"       : "Weather Observations",
           "start"       : "01/06/2021",
           "end"         : "01/10/2021",
           "output"      : "weather.png",
           "ylabel"      : "Temperature in Celsius",
           "data_column" : "T",
           }

required = {
           "input"  : str
           }
           
# now, parse the config file
parameters = get_parameters(args.input, required, defaults)

# load the data
weather = pd.read_csv(parameters.input,comment='#')

# obtain start and end date
start_date=pd.to_datetime(parameters.start,dayfirst=True)
end_date=pd.to_datetime(parameters.end,dayfirst=True)

# Data preprocessing
weather['Local time'] = pd.to_datetime(weather['Local time'],dayfirst=True)
# select the data
weather = weather[weather['Local time'].between(start_date,end_date)]

# Data plotting
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
fig.savefig(parameters.output)
