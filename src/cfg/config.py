# This file is used to configure the project.
# It sets the path and cache for the project.

# Importing relevant files:
import os
import sys
import time
import fastf1 as ff1
from src.cfg.directory import Directory as dir

# Class of initialisation procedures
class ConfigInitializer:
    configured = False
    
    # Initializes processess:
    def __init__(self):
        if not ConfigInitializer.configured:
            self.initialize_path()
            self.initialize_cache()
            ConfigInitializer.configured = True
            print(f"\n{__file__.split("\\")[-1]} ran succesfully. \n")
        else:
            print("Already configured")
    
    @classmethod
    def initialize_path(self):
        '''Initializes the path for the project.
            
            Args:
                None
            
            Returns:
                None
        '''
        
        # Adds the source folder to the path
        sys.path.append(dir.src)
        #sys.path.append(dir.cfg) not necessary as to import file from cfg you need to append it anyways
        sys.path.append(dir.fun)
        print("Path(s) configured")
        return None
    
    @classmethod
    def initialize_cache(self):
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
        cache_dir = dir.cache
        os.makedirs(cache_dir, exist_ok=True) # Creates the cache folder if it doesn't exist
        ff1.Cache.enable_cache(cache_dir)     # Enables the cache on "Cache"
        print("Cache configured")
        
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

# Initializes the configuration
ConfigInitializer()