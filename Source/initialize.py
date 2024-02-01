# Import all the necessary modules and set up the cache directory
import os
import time
import fastf1 as ff1 # Import fastf1


class Initializer:
    
    # Initilized flag to avoid multiple initializations
    initialized = False
    
    # Initializes processess:
    def __init__(self):
        if not Initializer.initialized:
            self.initialize()
            Initializer.initialized = True
    
    # Initializes the cache:
    def initialize_cache(self):
        
        # Saves start time(s):
        if __name__ == '__main__':
            print(f"\n{__file__.split("\\")[-1]} ran succesfully. \n")
            clock_start_time = time.time()
            exec_start_time = time.process_time()
        
        # Sets global cache directory to "Cache"
        cache_dir = "Cache"
        os.makedirs(cache_dir, exist_ok=True) # Creates the cache folder if it doesn't exist
        ff1.Cache.enable_cache(cache_dir)     # Enables the cache on "Cache"
                
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

