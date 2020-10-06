#16-1. Sitka Rainfall: Sitka is in a temperate rainforest, so it gets a fair amount of rainfall. In the data file sitka_weather_2014_simple.csv is a header called PRCP, which represents daily rainfall amounts. Make a visualization focusing on the data in this column. You can repeat the exercise for Death Valley if you’re curious how little rainfall occurs in a desert.

import csv

from datetime import datetime


from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, precip = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            precips = float(row[20])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            precip.append(precips)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, precip , c='red', alpha=0.5)
plt.fill_between(dates, precip, facecolor='blue', alpha=0.1)

# Format plot.
title = "Rains in the desert" 
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()