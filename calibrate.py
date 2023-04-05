# must run as sudo!
from bluepy import btle
import time
import sys

scanner = btle.Scanner()
devices = scanner.scan(10.0)

sensors = []
for device in devices:
    if  device.getValueText(9) == "BLE_CO2_SensNet":
    #if  True:
        #print("Found: {}".format(device.getValueText(3)))
        #print("Found: {}".format(device.getValueText(9)))        
        sensors.append(device.addr)
        #print(sensors)

if sensors:
    print("Found: {}".format(sensors))
else:
    print("No sensors found. Disconnect power-supply!")
    sys.exit()

device_id = sensors[0]



#reference_value = 400
reference_value = input("What is the reference value (in ppm) You want to set the sensors to?")
reference_value = int(reference_value)

if (reference_value < 350 or reference_value > 900):
    print("Error: Reference value must be set between 350 and 900 ppm!")
    sys.exit()

# BLE Service & Characteristic UUIDs - Do NOT Change Anything
MEASUREMENTS_SERVICE_UUID = btle.UUID("2a13dada-295d-f7af-064f-28eac027639f")
CO2_DATA_CHARACTERISTIC_UUID = btle.UUID("4ef31e63-93b4-eca8-3846-84684719c484")
        


SETTINGS_SERVICE_UUID = btle.UUID("2119458a-f72c-269b-4d4d-2df0319121dd")

for device_id in sensors:
#for device in devices:
    print("Try to start calibration on Device {}".format(device_id))

    # Connect sensorboard by ID
    XENSIV_BLE_Adapter = btle.Peripheral(device_id)
    Measurements_Service = XENSIV_BLE_Adapter.getServiceByUUID(MEASUREMENTS_SERVICE_UUID)
    Settings_Service = XENSIV_BLE_Adapter.getServiceByUUID(SETTINGS_SERVICE_UUID)


    # Get characteristics from service
    CO2_Data_Characteristic = Measurements_Service.getCharacteristics(CO2_DATA_CHARACTERISTIC_UUID)[0]
    CO2_Reading = CO2_Data_Characteristic.read()
    CO2_Raw = (CO2_Reading[1] << 8) + CO2_Reading[0]

    print("- current reading: {} \n- new reference: {}".format(CO2_Raw,reference_value))

    # reset_device
    # wait

    # connect_to_device


    # Returns the specified 16-bit signed integer value as an array of bytes.
    bytes_refData = reference_value.to_bytes(3, 'little')

    Config_CalibrationReferenceValueCharacteristic_UUID = btle.UUID("6f8afe94-a93d-cfb2-1b47-da0f98d9bfa1")
    Config_CalibrationReferenceValueCharacteristic = Settings_Service.getCharacteristics(Config_CalibrationReferenceValueCharacteristic_UUID)[0]
    
    print(Config_CalibrationReferenceValueCharacteristic.read())
    time.sleep(1)
    print(Config_CalibrationReferenceValueCharacteristic.write(bytes_refData, withResponse=True))
    time.sleep(1)
    print(Config_CalibrationReferenceValueCharacteristic.read())
    time.sleep(1)

    # Config_EnableSensorCalibrationCharacteristic
    Config_EnableSensorCalibrationCharacteristic_UUID   = btle.UUID("e64d0510-07f3-ac96-9c4d-5af82839425c")
    Config_EnableSensorCalibrationCharacteristic =Settings_Service.getCharacteristics(Config_EnableSensorCalibrationCharacteristic_UUID)[0]
    
    print(Config_EnableSensorCalibrationCharacteristic.read())
    x = 1
    bytes_calibTrue = x.to_bytes(1, 'little')



    time.sleep(1)
    print(Config_EnableSensorCalibrationCharacteristic.write((1).to_bytes(1, 'big'), withResponse=True))
    time.sleep(1)
    print(Config_EnableSensorCalibrationCharacteristic.read())

    XENSIV_BLE_Adapter.disconnect()
    time.sleep(1)
    
print("Wait till all sensors stopped blinking (red, yellow,green). After that, interrupt power supply of the sensors.")

sys.exit()
    # https://stackoverflow.com/questions/59597223/how-to-write-decimal-value-1-from-bluepy-to-ble-device
    # Seems to work.
    # Add automatic logging