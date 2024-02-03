# Import relevant packages
import pandas as pd
import fastf1 as ff1
import fastf1.plotting as ff1plt
import matplotlib.pyplot as plt

# Importing the personalised modules
from src.fun import load_data as ld

# Session Identifiers:
session_year = 2021
session_name = 'Monaco Grand Prix'
session_type = 'Q'

# Loads the Qualifying Laps data from the F1 API
data = ld.load_session(session_year, session_name, session_type)
laps = data.laps


