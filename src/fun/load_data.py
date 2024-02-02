# Description: 
#  -> This file contains the functions to load the data from the F1 API
#  -> Saves the data in .csv format in the data folder


# Imports relevant libraries
import os.path as op
import sys
import fastf1 as ff1
import pandas as pd

from src.cfg.config import ConfigInitializer

# Introduces Testing Variables [https://docs.fastf1.dev/events.html#sessionidentifier |Session Identifiers]
if __name__ == '__main__':
    cache_info = ff1.Cache.get_cache_info() # Prints the cache info
    print(f"Cache info: {cache_info} \n")

# Loads the data from the F1 API
print("Loading data from the F1 API...")