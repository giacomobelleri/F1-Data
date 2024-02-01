# Description: 
#  -> This file contains the functions to load the data from the F1 API
#  -> Saves the data in .csv format in the data folder

# Imports relevant libraries
import fastf1 as ff1
import pandas as pd
import matplotlib.pyplot as plt

# Introduces Testing Variables [https://docs.fastf1.dev/events.html#sessionidentifier |Session Identifiers]
if __name__ == '__main__':
    session_year = 2021
    session_type = 'R'                      
    session_name = 'Monaco Grand Prix'
    ff1.Cache.get_cache_info() # Prints the cache info


# Loads the data from the F1 API