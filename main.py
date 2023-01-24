# %% packages to load

import logging

# Config file
import config

# Custom functions
from helpers import loop_through_sensors

# %% 
# Read description of sensors in this room,
sensors = config.SENSORS



# %%
# Loop through all sensors in the config file
## see https://stackoverflow.com/questions/27033317/a-function-that-polls-on-intervals-and-yields-infinitely


import threading
import time
def poll(sensors, time_interval):
    '''A function that polls data from all the sensors in a given time interval'''

    while True:
        loop_through_sensors(sensors)
        print(sensors)
        time.sleep(time_interval)
        

poll(sensors, 5)

