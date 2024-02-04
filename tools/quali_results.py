# Import relevant packages
import pandas as pd
import fastf1 as ff1
import fastf1.plotting as ff1plt
import matplotlib.pyplot as plt

# Importing the personalised modules
from src.fun import load_data as ld
from src.fun import plotting as pt

# Session Identifiers:
session_year = 2021
session_name = 'Monaco Grand Prix'
session_type = 'Q'

# Loads the Qualifying Laps data from the F1 API
data = ld.load_session(session_year, session_name, session_type)
laps = data.laps
print(data.results.columns)

# Determines the fastest lap of each driver
fastest_laps = laps.groupby('Driver')['LapTime'].min() # Fastest lap of each driver
sorted_laps = fastest_laps.sort_values(ascending=True) # Sorts the fastest laps
relative_laps = sorted_laps - sorted_laps.iloc[0] # LapTime relative to pole lap
drivers = list(sorted_laps.index) # Drivers in the session

# Plots the fastest lap of each driver relative to pole lap
# pt.quali_results_hist(drivers, relative_laps)


