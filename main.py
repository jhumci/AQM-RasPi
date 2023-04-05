# %% packages to load
from bluepy import btle
import time
import sys




# Custom functions
from helpers import loop_through_sensors

# %% 
# Find all current sensors

scanner = btle.Scanner()
devices = scanner.scan(10.0)

new_sensors = []
for device in devices:
    if  device.getValueText(9) == "BLE_CO2_SensNet":
    #if  True:
        #print("Found: {}".format(device.getValueText(3)))
        #print("Found: {}".format(device.getValueText(9)))        
        new_sensors.append(device.addr)
        #print(sensors)

if new_sensors:
    print("Found: {}".format(new_sensors))
else:
    print("No sensors found. Disconnect power-supply!")
    sys.exit()

#%%

from datetime import datetime
dt = datetime.now()

# Room-Name
ROOM_NAME = str(dt)
# RASPI_MAC = "" 
# Sensor
SENSORPOSITION = "Calibration"

new_sensors_with_meta_data = []

for sensor in new_sensors:

    new_sensors_with_meta_data.append({"BT_TARGET_ADDRESSES" : sensor, "Room" : ROOM_NAME, "Sensor_Position" : SENSORPOSITION})


# %%
# Loop through all sensors in the config file
## see https://stackoverflow.com/questions/27033317/a-function-that-polls-on-intervals-and-yields-infinitely


import threading
import time

def poll(sensors, time_interval):
    '''A function that polls data from all the sensors in a given time interval'''

    while True:
        loop_through_sensors(sensors)
        #print(sensors)
        time.sleep(time_interval)
        

poll(new_sensors_with_meta_data, 60)

