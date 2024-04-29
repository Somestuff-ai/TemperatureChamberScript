
import serial
# ser = serial.Serial ('COM3',9600)

# enq = bytearray('\x0401M200\x05{', 'ascii') #Oven Temperature a-b
# vals = []
# ser.write(enq)
# res = ''
# response = ser.read_until(b'\x03')  # Read until <ETX> character (ASCII code 3) is encountered#
# res += response.decode('ascii')
# if res.endswith('\x03'):
#     start_index = res.find('a') + 1
#     end_index = res.find('b',start_index)
#     substr = res[start_index:end_index]
#     substr = float(substr)
#     vals.append(substr)       
#     response = vals
#     print (response)
#     vals = [] 
        
   

# ser = serial.Serial ('COM11',9600)

# vals = []

# enq = bytearray('\x0401L002\x05z', 'ascii') #WS504 Temp Reading k-l and EUT mA reading n-o
# vals = []
# ser.write(enq)
# res = ''
# response = ser.read_until(b'\x03')  # Read until <ETX> character (ASCII code 3) is encountered#
# res += response.decode('ascii')
# if res.endswith('\x03'):
#     start_index = res.find('k', res.find('j')) + 1
#     end_index = res.find('l',start_index)
#     substr = res[start_index:end_index]
#     substr = float(substr)
#     vals.append(substr)       
#     response = vals
#     print (response)
#     vals = [] 



# ser = serial.Serial ('COM11',9600)

# enq = bytearray('\x0401L002\x05z', 'ascii') #WS504 Temp Reading k-l and EUT mA reading n-o
# vals = []
# ser.write(enq)
# res = ''
# response = ser.read_until(b'\x03')  # Read until <ETX> character (ASCII code 3) is encountered#
# res += response.decode('ascii')
# if res.endswith('\x03'):
#     start_index = res.find('n', res.find('l')) + 1
#     end_index = res.find('o', start_index)
#     substr = res[start_index:end_index]
#     substr = float(substr)
#     vals.append(substr)       
#     response = vals
#     print (response)
#     vals = [] 




ser = serial.Serial ('COM14',9600)

enq = b'\xFC ' #WS504 Temp Reading k-l and EUT mA reading n-o

last_response = ""

while True:
    ser.write(enq)  # Assuming this is the equivalent of '\ü ' in Python
    
    res = b''
    while True:
        byte = ser.read()
        if byte:
            res += byte
        else:
            break
    
    last_response = res  # Save the last response
    
    isotech = res[2:8]  # Extracting from the 3rd character to the next 6 characters
    print(isotech)


