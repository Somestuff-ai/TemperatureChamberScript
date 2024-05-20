import serial
from datetime import datetime, timedelta
import time
from initialise import csv_file_path, serial_connections, device

# char = "\ü"
# hex_representation = char.encode("utf-8").hex()
# print(hex_representation)

# serial_command = "^A^P€^D^@^B^D^@^@^@^@“š"
# hex_bytes = bytes(serial_command.encode('utf-8'))

# print(hex_bytes.hex())



def tt10_send_enquiry():
    ser = serial_connections[2]
    command = b'\x01\x10\x80\x04\x00\x02\x04\x41\x20\x00\x00\x86\x6C'
    if not ser.is_open:
        ser.open()

    ser.write(command)

    time.sleep(1)
    response = ser.read_all()

    substr = response.decode('utf-8')
    response = substr[2:8]

    ser.close()

    return response
tt10_send_enquiry()