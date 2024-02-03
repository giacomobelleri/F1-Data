# This file is used to initialize the src directory as a package

# Import relevant packages
import os
import sys
import time
import numpy as np
import pandas as pd
import os.path as op
import matplotlib.pyplot as plt

# Importing the Fast F1 API
import fastf1 as ff1
import fastf1.plotting as ff1plt

# Importing the personalised modules
from src.cfg.directory import Directory

# Class of initialisation procedures
class ConfigInitializer:
    configured = False
    
    # Initializes processess:
    def __init__(cls):
        if not cls.configured:
            print(f"\nInitializing {__file__.split('\\')[-2]}...")
            cls.initialize_path()
            cls.initialize_cache()
            cls.initialize_plt()
            cls.configured = True
            print(f"{__file__.split("\\")[-2]} initialised succesfully. \n")
        else:
            print("Already configured")
    
    @classmethod
    def initialize_path(cls):
        '''Initializes the path for the project.
            
            Args:
                None
            
            Returns:
                None
        '''
        
        # Adds the source folder to the path
        sys.path.append(Directory.src)
        sys.path.append(Directory.cfg) 
        sys.path.append(Directory.fun)
        print("-> Path(s) configured")
        return None
    
    @classmethod
    def initialize_cache(cls):
        '''Initializes the cache for the fastf1 library.
            
            Args:
                None
            
            Returns:
                None
        '''
        
        # Saves start time(s):
        if __name__ == '__main__':
            clock_start_time = time.time()
            exec_start_time = time.process_time()
        
        # Sets global cache directory to "Cache"
        cache_dir = Directory.cache
        os.makedirs(cache_dir, exist_ok=True) # Creates the cache folder if it doesn't exist
        ff1.Cache.enable_cache(cache_dir)     # Enables the cache on "Cache"
        print("-> Cache configured")
        print(f"--> Cache directory: {cache_dir}")
        
        # Prints script information:
        if __name__ == '__main__':
            # Saves end time(s):
            clock_end_time = time.time()
            exec_end_time = time.process_time()
                
            # Prints the time it took to run the script:
            print("Cache created succesfully. \n" +
                    f" -> Cache directory: {cache_dir} \n" +
                    f" -> Cache creation time: {(clock_end_time - clock_start_time):.5f} s \n" + 
                    f" -> Cache creation CPU time: {(exec_end_time - exec_start_time):.5f} s \n" )
            
        return None
    
    def initialize_data(cls):
        '''Initializes the data for the project.
            
            Args:
                None
            
            Returns:
                None
        '''
        
        # Sets the data directory
        data_dir = Directory.data
        os.makedirs(data_dir, exist_ok=True)
    
    def initialize_plt(cls):
        '''Initializes the plotting configuration for the project.
            
            Args:
                None
            
            Returns:
                None
        '''
        
        # Sets the plotting configuration
        ff1plt.setup_mpl()
        print("-> Plotting configured")
        return None

# Initializes the configuration
ConfigInitializer()
