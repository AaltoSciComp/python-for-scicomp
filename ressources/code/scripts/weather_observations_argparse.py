import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, help="Input data file")
parser.add_argument("output", type=str, help="Output plot file")
parser.add_argument("-s", "--start", default="01/01/2019", type=str, help="Start date in DD/MM/YYYY format")
parser.add_argument("-e", "--end", default="16/10/2021", type=str, help="End date in DD/MM/YYYY format")      


args = parser.parse_args()

# define the start and end time for the plot
start_date=pd.to_datetime(args.start,dayfirst=True)
end_date=pd.to_datetime(args.end,dayfirst=True)

# load the data
weather = pd.read_csv(args.input,comment='#')
# The date format in the file is in a day-first format, which matplotlib does nto understand.
# so we need to convert it.
weather['Local time'] = pd.to_datetime(weather['Local time'],dayfirst=True)
# select the data
weather = weather[weather['Local time'].between(start_date,end_date)]
# start the figure.
fig, ax = plt.subplots()
ax.plot(weather['Local time'], weather['T'])
# label the axes
plt.xlabel("Date of observation")
plt.ylabel("Temperature in Celsius")
plt.title("Temperature Observations")
# adjust tick labels
fig.autofmt_xdate()
# save the figure
plt.savefig(args.output)
