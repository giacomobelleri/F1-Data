import fastf1 as ff1 # Import fastf1
import os

# Sets global cache directory to "Cache"
os.makedirs('Cache', exist_ok=True) # Creates the cache folder if it doesn't exist
ff1.Cache.enable_cache('Cache')     # Enables the cache on "Cache"

if __name__ == '__main__':
    print("Cache drirectory created. \n" +
          f"Cache directory: ", ff1.Cache.directory) 