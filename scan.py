import asyncio
import logging

from bleak import BleakScanner
from os import path as path

async def run():
    if not path.isfile("known_devices.txt"):
        #devices = await BleakScanner.discover(10.0)
        print("scan")
        async with BleakScanner() as scanner:
            await asyncio.sleep(5.0)
            devices = await scanner.get_discovered_devices()
        for d in devices:
            try:
                print(d)
                if d.name == "BLE_App_CO2":
                    f = open("known_devices.txt", "a+")
                    f.write(d.address + '\n')
                    print(d.address)
                    f.close()
            except:
                logging.error("Exception captured during scan", exc_info=True)
    else:
        logging.error("Please delete the File: known_devices.txt")



