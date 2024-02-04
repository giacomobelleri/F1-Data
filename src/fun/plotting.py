import fastf1 as ff1
import fastf1.plotting as ff1plt
import matplotlib.pyplot as plt
import numpy as np

def quali_results_hist(drivers, laps):
    ''' Plots the fastest lap of each driver relative to pole lap.'''
    
    # Creates the figure on which reults will be plotted
    plt.figure(figsize=(10, 6))
    
    # Creates array of driver colors
    color_arr = np.zeros(shape=(len(drivers), 1), dtype=object)
    for index, driver in enumerate(drivers):
        driver_color = ff1plt.driver_color(driver)
        print(f"Driver: {driver}, Color: {driver_color}")
        color_arr[index] = driver_color
    
    # Plots the fastest lap of each driver relative to pole lap
    plt.bar(x=drivers,
            height=laps,
            color=color_arr,
            orientation='horizontal')
    plt.show()
    return