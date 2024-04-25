
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
        
print(res) 