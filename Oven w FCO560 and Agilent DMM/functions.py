from initialise import csv_file_path, serial_connections, device
from CS043_Click import take_cs043_reading
import time
import csv
from datetime import datetime, timedelta

step = 1
avg_ISOTECH_1 = 0
avg_ISOTECH_2 = 0
avg_ISOTECH_3 = 0
avg_ISOTECH_4 = 0

avg_WS504_1 = 0
avg_WS504_2 = 0
avg_WS504_3 = 0
avg_WS504_4 = 0

avg_EUT_mA_1 = 0
avg_EUT_mA_2 = 0 
avg_EUT_mA_3 = 0
avg_EUT_mA_4 = 0

diff_1 = 0
diff_2 = 0
diff_3 = 0
diff_4 = 0

condition_1 = 0
condition_2 = 0
condition_3 = 0
condition_4 = 0
start_time = datetime.now()

# Define functions for script commands

def run_temperature_test(temperature, elapsed_time_check, sleep_seconds):
    global start_time

    generate_csv_headers()

    fur_send_command(1, f'01v000a{temperature}')

    #set_temp(temperature)  # Temperature: 10, Elapsed time: 10 seconds, Log delay: 10 seconds
    
    elapsed_time_check_seconds = time_to_seconds(elapsed_time_check)
    while True:

        # Oven_T = fur_send_command(1,'Temp','\x0401M200\x05{' )
        Oven_T = fur_send_enquiry(1,'Temp','01M200' )
        print (Oven_T)

        # WS504_T = fur_send_enquiry(7, 'Temp', '\x0401L002\x05z')
        WS504_T = fur_send_enquiry(7, 'Temp', '01L002')
        print(WS504_T)

        # EUT_mA = fur_send_enquiry(7, 'mA','\x0401L002\x05z')
        EUT_mA = fur_send_enquiry(7, 'mA','01L002')
        print (EUT_mA)

        ISOTECH_T = tt10_send_enquiry()
        print(ISOTECH_T)

        current_time = datetime.now()
        elapsed_time = current_time - start_time
        current_time = current_time.strftime("%H:%M:%S")

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_time, elapsed_time, ISOTECH_T, WS504_T,EUT_mA, Oven_T])
        
        if elapsed_time >= timedelta(seconds=elapsed_time_check_seconds):
            break

        time.sleep(sleep_seconds)    

    take_cs043_reading()
    end_point_20rdgs(temperature)
    
    return

def time_to_seconds(time_str):
     # Convert time string in HH:MM:SS format to seconds
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s   


def end_point_20rdgs(temperature):
    global step
    global avg_EUT_mA_1, avg_EUT_mA_2, avg_EUT_mA_3, avg_EUT_mA_4
    global avg_ISOTECH_1, avg_ISOTECH_2, avg_ISOTECH_3, avg_ISOTECH_4
    global avg_WS504_1, avg_WS504_2, avg_WS504_3, avg_WS504_4
    global diff_1, diff_2, diff_3, diff_4
    global condition_1, condition_2, condition_3, condition_4

    sum_ISOTECH = 0
    sum_WS504_T = 0
    sum_EUT_mA = 0

    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([])
        writer.writerow(["End Point Readings:"])

    for i in range (20):    
        ISOTECH_T = float(tt10_send_enquiry())
        sum_ISOTECH = sum_ISOTECH + ISOTECH_T
        print (sum_ISOTECH)
        
        WS504_T = float(fur_send_enquiry(7, 'Temp', '01L002'))
        sum_WS504_T = sum_WS504_T + WS504_T
        print (sum_WS504_T)

        EUT_mA = float(fur_send_enquiry(7, 'mA','01L002'))
        sum_EUT_mA = sum_EUT_mA + EUT_mA
        print (sum_EUT_mA)

        Oven_T = fur_send_enquiry(1,'Temp','01M200' )
        print (Oven_T)

        current_time = datetime.now()
        elapsed_time = current_time - start_time
        current_time = current_time.strftime("%H:%M:%S")  

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_time, elapsed_time, ISOTECH_T, WS504_T,EUT_mA, Oven_T])  
     

    avg_ISOTECH_T = round(sum_ISOTECH/20, 3)
    print (avg_ISOTECH_T)

    avg_WS504_T = round(sum_WS504_T/20, 3)
    print (WS504_T)

    avg_EUT_mA = round(sum_EUT_mA/20, 3)
    print (EUT_mA)

    diff = round(abs( avg_ISOTECH_T - avg_WS504_T), 3)
    print(diff)

    sum_ISOTECH = 0
    sum_WS504_T = 0
    sum_EUT_mA = 0

    # store averags based on step value
    if step == 1:
        avg_ISOTECH_1 = avg_ISOTECH_T
        avg_WS504_1 = avg_WS504_T
        avg_EUT_mA_1 = avg_EUT_mA
        diff_1 = diff
        if diff_1 > 0.1:
            condition_1 = "Fail"
        else:
            condition_1 = "Pass"
        step += 1
        return avg_ISOTECH_1, avg_WS504_1, avg_EUT_mA_1, diff_1, condition_1, step       

    elif step == 2:
        avg_ISOTECH_2 = avg_ISOTECH_T
        avg_WS504_2 = avg_WS504_T
        avg_EUT_mA_2 = avg_EUT_mA  
        diff_2 = diff
        if diff_2 > 0.1:
            condition_2 = "Fail"
        else:
            condition_2 = "Pass"
        step += 1
        return avg_ISOTECH_2, avg_WS504_2, avg_EUT_mA_2, diff_2, condition_2, step
    
    elif step == 3:
        avg_ISOTECH_3 = avg_ISOTECH_T
        avg_WS504_3 = avg_WS504_T
        avg_EUT_mA_3 = avg_EUT_mA
        diff_3 = diff
        if diff_3 > 0.1:
            condition_3 = "Fail"
        else:
            condition_3 = "Pass"
        step += 1
        return avg_ISOTECH_3, avg_WS504_3, avg_EUT_mA_3, diff_3, condition_3, step
    
    elif step == 4:
        avg_ISOTECH_4 = avg_ISOTECH_T
        avg_WS504_4 = avg_WS504_T
        avg_EUT_mA_4 = avg_EUT_mA
        diff_4 = diff
        if diff_4 > 0.1:
            condition_4 = "Fail"
        else:
            condition_4 = "Pass"

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([])
            writer.writerow(["Average RS80 Temp", "Aveage WS504 Temp", "Average EUTmA", "Check Difference", "Pass/Fail"])
            writer.writerow([avg_ISOTECH_1, avg_WS504_1, avg_EUT_mA_1, diff_1, condition_1])
            writer.writerow([avg_ISOTECH_2, avg_WS504_2, avg_EUT_mA_2, diff_2, condition_2])
            writer.writerow([avg_ISOTECH_3, avg_WS504_3, avg_EUT_mA_3, diff_3, condition_3])
            writer.writerow([avg_ISOTECH_4, avg_WS504_4, avg_EUT_mA_4, diff_4, condition_4]) 

    return    



#BCC Check Sum Calculations
def command_check_sum(command):
    ETX = 3
    EOT = 4

    CommsCommand = command + chr(ETX)

    # Calculate the checksum BCC for CommsCommand
    BCC = 0
    for char in CommsCommand:
        BCC ^= ord(char)

    # The final string comprises an <EOT> character, the command then the BCC
    CommsCommand = chr(EOT) + CommsCommand + chr(BCC)
    return CommsCommand
   

def enquiry_check_sum(enquiry):
    ENQ = 5
    EOT = 4

    CommsEnquiry = enquiry + chr(ENQ)

    # Calculate the checksum BCC for CommsCommand
    BCC = 0
    for char in CommsEnquiry:
        BCC ^= ord(char)

    # The final string comprises an <EOT> character, the command then the BCC
    CommsEnquiry = chr(EOT) + CommsEnquiry + chr(BCC)
    return CommsEnquiry
        

# Functions to send enquiries and read responses 
def fur_send_enquiry(device, reading, enquiry):
    global response
    enquiry = enquiry_check_sum(enquiry)
    ser = serial_connections[device]
    if not ser.is_open:
        ser.open()
    enq = bytearray(enquiry, 'ascii')
    ser.write(enq)
    res = ''
    response = ser.read_until(b'\x03')  # Read until <ETX> character (ASCII code 3) is encountered#
    res += response.decode('ascii')

    if device == 1:
        if reading == 'Temp':
            start_index = res.rfind('a') + 1
            end_index = res.find('b',start_index)            
    elif device == 7:
        if reading == 'Temp':
            start_index = res.find('k', res.find('Aux. Press.')) + 1
            end_index = res.find('l',start_index)
        elif reading == 'mA':
            start_index = res.find('n', res.find('EUT mA')) + 1
            end_index = res.find('o', start_index)

    substr = res[start_index:end_index]
    substr = float(substr)
    response = substr

    ser.close()

    return response

def tt10_send_enquiry():
    ser = serial_connections[device]
    enq = b'\x5c\xfc'
    if not ser.is_open:
        ser.open()

    ser.write(enq)

    time.sleep(1)
    response = ser.read_all()

    substr = response.decode('utf-8')
    response = substr[2:8]

    ser.close()

    return response
 
# Functions to send commands
def fur_send_command(device, command):
    command = command_check_sum(command)
    ser = serial_connections[device]
    if not ser.is_open:
        ser.open()

    comm  = bytearray(command, 'ascii')
    ser.write(comm)

    ser.close()

    return

def generate_csv_headers():
    headers = ["Time", "Elapsed", "RS80 Temp", "WS504 Temp", "EUT mA", "Oven T"]
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([])
        writer.writerow(headers)

   

    





