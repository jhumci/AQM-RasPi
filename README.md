# Script to store data in a CSV

This allows to poll the MCI Cypress boards with BLE

## Install Bluepy

- only works on Linux
-  https://github.com/IanHarvey/bluepy

```
$ sudo apt-get install python-pip libglib2.0-dev
$ sudo pip3 install bluepy
```

---

## Change Device Address

in `config.py`


```
SENSORS = [{"BT_TARGET_ADDRESSES" : "C6:DA:C4:A8:1E:06",
            "Room" : ROOM_NAME,
            "Sensor_Position" : "2m"}]
```

---

## Run Python Script

```
python3 main.py
```

CSV-File with reads is created based in the ROOM_NAME in the config