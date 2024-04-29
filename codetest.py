
import serial
# ser = serial.Serial ('COM3',9600)

# enq = bytearray('\x0401M200a\x05{', 'ascii') #Oven Temperature a-b

# while True:
#     ser.write(enq)
#     res = ''
    

#     while True:
#         byte = ser.read()
#         if byte:
#             res += byte.decode('ascii')
#         else:
#             break
        
# print(res)    

ser = serial.Serial ('COM11',9600)

vals = []

enq = bytearray('\x0401L002\x05z', 'ascii') #WS504 Temp Reading k-l and EUT mA reading n-o

while True:
    ser.write(enq)
    res = ''
    

    while True:
        byte = ser.read()
        if byte:
            res += byte.decode('ascii')
        else:
            break
    start_index = res.find('k') + 1
    end_index = res.find('l')
    substr = res[start_index:end_index]
    substr = float(substr)
    vals.append(substr)       
    response = vals
    vals = []    
print(res) 



ser = serial.Serial ('COM11',9600)

vals = []

enq = bytearray('\x0401L002\x05z', 'ascii') #WS504 Temp Reading k-l and EUT mA reading n-o

while True:
    ser.write(enq)
    res = ''
    

    while True:
        byte = ser.read()
        if byte:
            res += byte.decode('ascii')
        else:
            break
    start_index = res.find('n') + 1
    end_index = res.find('o')
    substr = res[start_index:end_index]
    substr = float(substr)
    vals.append(substr)       
    response = vals
    vals = []    
print(res) 



ser = serial.Serial ('COM14',9600)

vals = []

enq = bytearray('\ü ') #WS504 Temp Reading k-l and EUT mA reading n-o

while True:
    ser.write(enq)
    res = ''
    

    while True:
        byte = ser.read()
        if byte:
            res += byte.decode('ascii')
        else:
            break

    isotech = res[2:8]  # Extracting from the 3rd character to the next 6 characters
    print(isotech)




#some call to function fur_comm()