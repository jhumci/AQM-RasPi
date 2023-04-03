from bluepy import btle
import time
import sys

scanner = btle.Scanner()
devices = scanner.scan(10.0)

for device in devices:
    print("Found: {}".format(device.rssi))

device_id = devices[0]
reference_value = 400

if (reference_value < 350 or reference_value > 900):
    print("Error: Reference value must be set between 350 and 900 ppm!")
    sys.exit()

# BLE Service & Characteristic UUIDs - Do NOT Change Anything
MEASUREMENTS_SERVICE_UUID = btle.UUID("2a13dada-295d-f7af-064f-28eac027639f")
CO2_DATA_CHARACTERISTIC_UUID = btle.UUID("4ef31e63-93b4-eca8-3846-84684719c484")
        
Config_CalibrationReferenceValueCharacteristic = btle.UUID("6f8afe94-a93d-cfb2-1b47-da0f98d9bfa1")
Config_EnableSensorCalibrationCharacteristic   = btle.UUID("e64d0510-07f3-ac96-9c4d-5af82839425c")

# SETTINGS_SERVICE_UUID = btle.UUID("2119458a-f72c-269b-4d4d-2df0319121dd")


for device in devices:
    print("Found: {}".format(device.rssi))

    print("Try to start calibration on Device {}".format(device_id))

    # Connect sensorboard by ID
    XENSIV_BLE_Adapter = btle.Peripheral(device_id)
    Measurements_Service = XENSIV_BLE_Adapter.getServiceByUUID(MEASUREMENTS_SERVICE_UUID)

    # Get characteristics from service
    CO2_Data_Characteristic = Measurements_Service.getCharacteristics(CO2_DATA_CHARACTERISTIC_UUID)[0]

    print("- current reading: {} \n - new reference: {}".format(CO2_Data_Characteristic,reference_value))

    # reset_device
    # wait

    # connect_to_device

    # Returns the specified 16-bit signed integer value as an array of bytes.
    bytes_refData = reference_value.to_bytes(2, 'little')

    #Config_CalibrationReferenceValueCharacteristic
    XENSIV_BLE_Adapter.writeCharacteristic(Config_CalibrationReferenceValueCharacteristic, bytes_refData, withResponse=False)

    # Config_EnableSensorCalibrationCharacteristic
    x = 1
    bytes_calibTrue = x.to_bytes(1, 'little')
    XENSIV_BLE_Adapter.writeCharacteristic(Config_EnableSensorCalibrationCharacteristic, bytes_calibTrue, withResponse=False)


