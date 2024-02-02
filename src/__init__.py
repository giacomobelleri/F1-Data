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
from src import cfg

# Class of Directories 
class Directory:
    
    # Parent Directory
    parent = op.dirname(op.dirname(op.abspath(__file__)))
    
    # Subdirectories
    cache = op.join(parent, 'cache') # Cache directory
    data = op.join(parent, 'data')   # Data directory
    src = op.join(parent, 'src')     # Source directory
    cfg = op.join(src, 'cfg')        # Config directory
    fun = op.join(src, 'fun')        # Function directory
    
    if __name__ == '__main__':
        print(f"Parent directory: {parent}")
        print(f"Cache directory: {cache}")
        print(f"Data directory: {data}")
        print(f"Source directory: {src}")
        print(f"Config directory: {cfg}")
        print(f"Function directory: {fun} \n")

# Class of initialisation procedures
class ConfigInitializer:
    configured = False
    
    # Initializes processess:
    def __init__(cls):
        if not cls.configured:
            print(f"\nRunning {__file__.split('\\')[-1]}...")
            cls.initialize_path()
            cls.initialize_cache()
            cls.initialize_plt()
            cls.configured = True
            print(f"{__file__.split("\\")[-1]} ran succesfully. \n")
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
        print("Path(s) configured")
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
        print("Cache configured")
        print(f"Cache directory: {cache_dir}")
        
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
    
    def initialize_plt(cls):
        '''Initializes the plotting configuration for the project.
            
            Args:
                None
            
            Returns:
                None
        '''
        
        # Sets the plotting configuration
        ff1plt.setup_mpl()
        print("Plotting configured")
        return None

# Initializes the configuration
ConfigInitializer()
