import serial

# Opens serial port
ser = serial.Serial ('COM3',9600, 8, 'n', 1) 
ser.open()

command = bytearray('\x04V000a10\x03', 'ascii')
ser.write(command)

ser.close()


