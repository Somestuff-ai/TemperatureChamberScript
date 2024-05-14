#Initialise comports and assigns them device numbers 

import csv
import serial

csv_file_path = "data.csv"
headers = ["Time", "Elapsed", "RS80 Temp", "WS504 Temp", "EUT mA", "Oven T"]
with open(csv_file_path, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)


# Define serial port parameters for each device
SERIAL_PORTS = {
    1: {'port': 'COM3', 'baudrate': 9600},
    7: {'port': 'COM11', 'baudrate': 9600},
    14: {'port': 'COM14', 'baudrate': 2400}
}

# Initialize serial connections for each device
serial_connections = {} 
for device, params in SERIAL_PORTS.items():
    serial_connections[device] = serial.Serial(params['port'], params['baudrate'], timeout=1)
