import serial
import csv

# Opens serial port
ser = serial.Serial ('COM3',9600) 


command = bytearray('\x0401v000a10\x03$', 'ascii') #uses XOR checksum sets temperature to 10
ser.write(command)

ser = serial.Serial ('COM 14', 9600, timeout = 1)

with open('serialnumnber_data.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile) # creates writer object
    writer.writerow(["Time", "Elpased", "RS80", "WS504", "EUT mA", "Oven T"])
    ISOTECH_command = '\ü'
    ser.write(ISOTECH_command)
    isotech_data = ser.readline()
    ISOTECH = float(isotech_data[2:8])

   
