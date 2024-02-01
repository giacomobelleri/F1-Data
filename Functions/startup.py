# Import all the necessary modules and set up the cache directory
import os
import time
import fastf1 as ff1 # Import fastf1

# Saves start time(s):
start_time = time.time()

# Sets global cache directory to "Cache"
cache_dir = "Cache"
os.makedirs(cache_dir, exist_ok=True) # Creates the cache folder if it doesn't exist
ff1.Cache.enable_cache(cache_dir)     # Enables the cache on "Cache"

# Saves end time(s):
end_time = time.time()

if __name__ == '__main__':
    print(f"\n{__file__.split("\\")[-1]} ran succesfully. \n")
    print("Cache created succesfully. \n" +
          f" -> Cache directory: {cache_dir} \n" +
          f" -> Cache creation time: {(end_time - start_time):.5f} s \n")