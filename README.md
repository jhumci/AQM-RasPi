# Scripts for Validation and Calibration of Cypress Sensor Boards

- This allows to poll the MCI Cypress boards with BLE from a Linux system
- Skript `calibrate.py` allows to enter a reference value to the boards 
- Skript `main.py` starts a logging process (all 60 seconds) ans stores the readings an a csv file

## Requirements

### Install Bluepy
    - only works on Linux
    -  https://github.com/IanHarvey/bluepy

```
$ sudo apt-get install python-pip libglib2.0-dev
$ sudo pip3 install bluepy
```

---

### Connect RasPi to the Internet

- For valid time stamps the RasPi has to be connected to the internet while logging the readings


---

## Python Script for Calibration on Reference values

- `calibrate.py`
- finds all active boards in the bluetooth radius
- let's user enter reference value
- flashes all boards with reference value
- during calibration, the boards blink like a traffic light while they calibrate
- wait until they only alternate between blue and one of the colors (up to 120s)
- scanning only works running script as sudo

```
sudo python3 calibrate.py
```

## Run Python Script for logging during Test run

- `main.py` starts the logging process until interrupted with [Ctrl+C]
- finds all active boards in the bluetooth radius
- CSV-File with reads is created based on the time of start, e.g., `logs_2023-02-12 00:44:57.995186.csv`
- prints the values during execution

```
sudo python3 main.py
```



## Second Batch of Sensor Boards

- all 13 Sensor boards seem to work (5.4.2023)

- 'b8:27:eb:f7:65:ff'
- 'b8:27:eb:7b:d0:25'
- 'b8:27:eb:9d:ac:4e'
- 'b8:27:eb:85:93:4e'
- 'b8:27:eb:88:a7:3c'
- 'b8:27:eb:98:c2:6a'
- 'b8:27:eb:37:91:ce'
- 'b8:27:eb:76:18:5e'
- 'b8:27:eb:6d:d9:41'
- 'b8:27:eb:73:6a:48'
- 'b8:27:eb:f9:bd:10'
- 'b8:27:eb:fb:89:d3'
- 'b8:27:eb:ac:f5:32'

