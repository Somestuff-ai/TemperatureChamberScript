import serial
from datetime import datetime, timedelta
import time
from initialise import csv_file_path, serial_connections, device

# char = "\ü"
# hex_representation = char.encode("utf-8").hex()
# print(hex_representation)

serial_command = "^A^P€^D^@^B^D^@^@^@^@“š"
hex_bytes = bytes(serial_command.encode('utf-8'))

print(hex_bytes.hex())



def tt10_send_enquiry():
    ser = serial_connections[device]
    enq = b'\x5c\xfc'
    if not ser.is_open:
        ser.open()

    ser.write(enq)

    time.sleep(1)
    response = ser.read_all()

    substr = response.decode('utf-8')
    response = substr[2:8]

    ser.close()

    return response