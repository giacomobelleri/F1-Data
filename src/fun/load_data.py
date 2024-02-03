# Description: 
#  -> This file contains the functions to load the data from the F1 API
#  -> Saves the data in .csv format in the data folder

# Imports the relevant packages
import os
import os.path as op
import fastf1 as ff1
from src.cfg.directory import Directory

def check_validity(year, name):
    return

def save_session(session, year, type, name):
    '''Saves the session data in the data folder as .csv file.'''
    
    # Prints the start-of-saving message
    print(f"\nSaving {year} {type} '{name}' data...")
    
    # Creates the directory for the data
    data_dir = Directory.data
    rel_path = rf"\{year}\{name}\{type}"
    file_name = f"{year}_{name}_{type}"
    os.makedirs(data_dir+rel_path, exist_ok=True)
    print(f"--> Data directory: {data_dir+rel_path}")
    
    # Selects different aspects of the session data
    results = session.results
    laps = session.laps
    
    # Saves the data in .csv format
    results.to_csv(data_dir+rel_path+rf"\{file_name}_results.csv")
    print(f"--> Results saved as: {file_name}_results.csv")
    
    laps.to_csv(data_dir+rel_path+rf"\{file_name}_laps.csv")
    print(f"--> Laps saved as: {file_name}_laps.csv")
    
    # Prints the end-of-saving message
    print(f"{year} {type} '{name}' data saved\n")
    return None
    
# Loads the data from the F1 API
def load_session(year, type, name, save=True):
    
    # Prints the start-of-loading message
    print("Loading data through the FastF1 API...")
    
    # Loads the data through the FastF1 API
    session = ff1.get_session(year, type, name)
    session.load()
    
    # Prints the end-of-loading message
    print(f"Data from {year} {type} '{name}' loaded")
    
    if save==True:
        save_session(session, year, type, name)
    else:
        pass
    
    # Returns the session data
    return session

if __name__ == '__main__':
    
    # Checks the cache info
    cache_info = ff1.Cache.get_cache_info() # Prints the cache info
    print(f"Cache info: {cache_info} \n")
    
    # Testes the load_session function
    session_year = 2021
    session_type = 'R'                      
    session_name = 'Monaco Grand Prix'
    data = load_session(session_year, session_name, session_type)
    print(f"\n {data.laps.head()}")