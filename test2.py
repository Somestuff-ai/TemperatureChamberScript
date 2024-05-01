import serial
import time

# Define serial port parameters for each device
SERIAL_PORTS = {
    1: {'port': 'COM3', 'baudrate': 9600},
    7: {'port': 'COM11', 'baudrate': 9600},
    14: {'port': 'COM14', 'baudrate': 9600}
}

# Initialize serial connections for each device
serial_connections = {} 
for device, params in SERIAL_PORTS.items():
    serial_connections[device] = serial.Serial(params['port'], params['baudrate'], timeout=1)

# Define functions for script commands

def send_command(device, command):
    # Send command over serial for specified device
    serial_connections[device].write(command.encode(encoding = "ascii"))

def read_response(device):
    # Read response from serial for specified device
    response = serial_connections[device].readline().decode().strip()
    return response

# Function to read response from the relevant comport
def fur_send_command(device, baudrate, reading, command):
    enq = bytearray(command, 'ascii')
    ser = serial.Serial (device, baudrate)
    #serial_connections[device].write(command.encode(encoding = "ascii"))
    vals = []
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
    vals.append(substr)       
    response = vals
    print (response)
    vals = []     



def set_temp(temperature, elapsed_time, log_delay):
    # Send command to set temperature
    command = f"\x0401v000a{temperature}\x03$"
    send_command(1, command)
    

    # Wait for specified elapsed time
    #delay(elapsed_time)


def main():
    
    #Call set_temp subroutine for each temperature setting
    set_temp(10, 10, 10)  # Temperature: 10, Elapsed time: 10 seconds, Log delay: 10 seconds
    fur_send_command(1,9600,'Temp','\x0401M200\x05{' )
    #set_temp(20, 20, 10)  # Temperature: 20, Elapsed time: 20 seconds, Log delay: 10 seconds
   # set_temp(30, 30, 10)  # Temperature: 30, Elapsed time: 30 seconds, Log delay: 10 seconds
    #set_temp(20, 40, 10)  # Temperature: 20,



    # Example script commands for device 1 (oven)
    #send_command(1, "CMD c")  # Replace 'c' with your Fbus command for device 1
    #response = read_response(1)
    #print("Response from device 1:", response)

    # Delay for 1 second

    # Example script commands for device 7 (microcalibrator)
    #send_command(7, "CMD c")  # Replace 'c' with your Fbus command for device 7
    #response = read_response(7)
    #print("Response from device 7:", response)

    # Continue with other script commands for different devices...


if __name__ == "__main__":
    main()