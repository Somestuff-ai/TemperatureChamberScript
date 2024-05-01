import serial
import time
import csv
from datetime import datetime

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

# Define functions for script commands

def send_command(device, command):
    # Send command over serial for specified device
    serial_connections[device].write(command.encode(encoding = "ascii"))



# Function to read response from the relevant furness comport
def fur_send_command(device, reading, command):
    global response
    ser = serial_connections[device]
    enq = bytearray(command, 'ascii')
    ser.write(enq)
    res = ''
    response = ser.read_until(b'\x03')  # Read until <ETX> character (ASCII code 3) is encountered#
    res += response.decode('ascii')

    if device == 1:
        if reading == 'Temp':
            start_index = res.find('a') + 1
            end_index = res.find('b',start_index)            
    elif device == 7:
        if reading == 'Temp':
            start_index = res.find('k', res.find('j')) + 1
            end_index = res.find('l',start_index)
        elif reading == 'mA':
            start_index = res.find('n', res.find('l')) + 1
            end_index = res.find('o', start_index)

    substr = res[start_index:end_index]
    substr = float(substr)
    response = substr
    return response

def tt10_send_command():
    ser = serial_connections[device]
    enq = b'\x5c\xfc'
    ser.write(enq)

    time.sleep(1)
    response = ser.read_all()

    substr = response.decode('utf-8')
    response = substr[2:8]

    return response
    

def set_temp(temperature):
    # Send command to set temperature
    command = f"\x0401v000a{temperature}\x03$"
    send_command(1, command)
    

    # Wait for specified elapsed time
    #delay(elapsed_time)


def main():
    
    #Create CSV file with headers
    csv_file_path = "data.csv"
    headers = ["Time", "Elapsed", "RS80 Temp", "WS504 Temp", "EUT mA", "Oven T"]
    
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    
    set_temp(10)  # Temperature: 10, Elapsed time: 10 seconds, Log delay: 10 seconds
    
    start_time = datetime.now()
    while True:

        fur_send_command(1,'Temp','\x0401M200\x05{' )
        Oven_T= response
        print (Oven_T)

        fur_send_command(7, 'Temp', '\x0401L002\x05z')
        WS504_T = response
        print(WS504_T)

        fur_send_command(7, 'mA','\x0401L002\x05z')
        EUT_mA = response
        print (EUT_mA)

        tt10_send_command()
        ISOTECH_T = response
        print(ISOTECH_T)

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elapsed_time = current_time - start_time

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_time, elapsed_time, Oven_T, WS504_T,EUT_mA,ISOTECH_T])
        
        if elapsed_time >= 10:
            break



    #set_temp(20, 20, 10)  # Temperature: 20, Elapsed time: 20 seconds, Log delay: 10 seconds
   # set_temp(30, 30, 10)  # Temperature: 30, Elapsed time: 30 seconds, Log delay: 10 seconds
    #set_temp(20, 40, 10)  # Temperature: 20,


if __name__ == "__main__":
    main()