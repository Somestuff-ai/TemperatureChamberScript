
# import serial
# import time
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




# # Open serial port
# ser = serial.Serial('COM14', 2400)  

# # Define the communication string
# communication_string = b'\x5c\xfc'  # This includes the escape backslash

# # Send the communication string
# ser.write(communication_string)

# # Wait for 1000 ms (1 second)
# time.sleep(1)

# # Read response
# response = ser.read_all()

# response_str = response.decode('utf-8')
# numerical_value = response_str[2:8]


# print("Extracted value:", numerical_value)


# print("Response:", response)

# # Close the serial port
# ser.close()




# ser = serial.Serial ('COM14',2400, timeout= 1)

# enq = b'\\xfc ' 
# res = b''
# ser.write(enq)  # Assuming this is the equivalent of '\ü ' in Python
# print (enq)

# while True:
#     byte = ser.read()
#     if byte:
#         res += byte
#     else:
#         break


# ser = serial.Serial ('COM14',9600, timeout = 1)

# enq = b'\x5C\xFC' 
# res = b''


# while True:
#     ser.write(enq)  # Assuming this is the equivalent of '\ü ' in Python
    
#     while True:
#         byte = ser.read(1)
#         if byte:
#             res += byte
#             if len(res) >= 8:
#                 break
#             else:
#                 break
        
#     isotech = res[2:8]  # Extracting from the 3rd character to the next 6 characters
#     print(isotech)


import pyautogui

# Find the location of the button on the screen
button_location = pyautogui.locateOnScreen('button_image.png')

# If button not found, print an error message
if button_location is None:
    print("Button not found.")
else:
    # Click the button
    pyautogui.click(button_location)