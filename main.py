import serial

# Opens serial port
ser = serial.Serial ('COM3',9600) 


command = bytearray('\x0401v000a10\x03$', 'ascii') #uses XOR checksum 
ser.write(command)




