# Description: 
#  -> This file contains the functions to load the data from the F1 API
#  -> Saves the data in .csv format in the data folder

# Imports relevant libraries
import os.path as op
import sys
import fastf1 as ff1
import pandas as pd
import src.cfg.config

# Introduces Testing Variables [https://docs.fastf1.dev/events.html#sessionidentifier |Session Identifiers]
if __name__ == '__main__':
    cache_info = ff1.Cache.get_cache_info() # Prints the cache info
    print(f"Cache info: {cache_info} \n")

# Loads the data from the F1 API
print("Loading data from the F1 API...")

if __name__ == '__main__':
    session_year = 2021
    session_type = 'R'                      
    session_name = 'Monaco Grand Prix'

# Loads the data from the F1 API
def load_session(year, type, name):
    session = ff1.get_session(year, type, name)
    session.load()
    print(f"Data from {year} {type} '{name}' loaded")
    return session

if __name__ == '__main__':
    data = load_session(session_year, session_name, session_type)
    print(f"\n {data.laps.head()}")