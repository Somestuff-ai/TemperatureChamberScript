#Initialise comports and assigns them device numbers 


import serial
import csv

# csv_file_path = ""

# def set_csv_file_path(path):
#     global csv_file_path
#     csv_file_path = path



# Define serial port parameters for each device
SERIAL_PORTS = {
    1: {'port': 'COM3', 'baudrate': 9600},
    2: {'port': 'COM4', 'baudrate': 9600},
    3: {'port': 'COM15', 'baudrate': 9600},
    7: {'port': 'COM11', 'baudrate': 9600},
    14: {'port': 'COM14', 'baudrate': 2400}
}

# Initialize serial connections for each device
serial_connections = {} 
for device, params in SERIAL_PORTS.items():
    serial_connections[device] = serial.Serial(params['port'], params['baudrate'], timeout=1)
