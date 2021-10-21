import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", type=str, help="Start date in DD/MM/YYYY format")
parser.add_argument("-e", "--end", type=str, help="End date in DD/MM/YYYY format")
parser.add_argument("-o", "--output", type=str, help="output plot file")
args = parser.parse_args()

# define the start and end time for the plot
start_date=pd.to_datetime(args.start,dayfirst=True)
end_date=pd.to_datetime(args.end,dayfirst=True)

# load the data
url = "weather_tapiola.csv"
weather = pd.read_csv(url,comment='#')
# The date format in the file is in a day-first format, which matplotlib does nto understand.
# so we need to convert it.
weather['Local time in Espoo / Tapiola'] = pd.to_datetime(weather['Local time in Espoo / Tapiola'],dayfirst=True)
# select the data
weather = weather[weather['Local time in Espoo / Tapiola'].between(start_date,end_date)]
# start the figure.
fig, ax = plt.subplots()
ax.plot(useddata['Local time in Espoo / Tapiola'], useddata['T'])
# label the axes
plt.xlabel("Date of observation")
plt.ylabel("Temperature in Celsius")
plt.title("Temperature in Tapiola, Espoo, Finnland")
# save the figure
plt.savefig(args.output)
