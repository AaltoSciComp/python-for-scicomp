#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from optionsparser import get_parameters
import weather_functions
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
start_date=pd.to_datetime(parameters.start_date,dayfirst=True)
end_date=pd.to_datetime(parameters.end_date,dayfirst=True)

# Data preprocessing
weather = weather_functions.preprocessing(weather,start_date,end_date)

# Data plotting
plt,fig = weather_functions.plot_data(weather['Local time'], weather[parameters.data_column], parameters)

# save the figure
plt.savefig(parameters.output_file)
