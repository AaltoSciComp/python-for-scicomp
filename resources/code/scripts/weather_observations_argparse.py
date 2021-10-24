import pandas as pd
import argparse
import weather_functions

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, help="Input data file")
parser.add_argument("output", type=str, help="Output plot file")
parser.add_argument("-s", "--start", default="01/01/2019", type=str, help="Start date in DD/MM/YYYY format")
parser.add_argument("-e", "--end", default="16/10/2021", type=str, help="End date in DD/MM/YYYY format")      

args = parser.parse_args()

# load the data
weather = pd.read_csv(args.input,comment='#')

# define the start and end time for the plot
start_date=pd.to_datetime(args.start,dayfirst=True)
end_date=pd.to_datetime(args.end,dayfirst=True)

# preprocess the data
weather = weather_functions.preprocessing(weather,start_date,end_date)

# plot the data
ax,fig = weather_functions.plot_data(weather['Local time'], weather['T'])

# save the figure
fig.savefig(args.output)
