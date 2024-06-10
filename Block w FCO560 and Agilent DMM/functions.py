from initialise import serial_connections, device
from CS043_Click import take_cs043_reading
import time
import csv
from datetime import datetime, timedelta
import serial

csv_file_path = ""
step = 1
avg_ISOTECH_1 = 0
avg_ISOTECH_2 = 0
avg_ISOTECH_3 = 0
avg_ISOTECH_4 = 0

avg_WS504_1 = 0
avg_WS504_2 = 0
avg_WS504_3 = 0
avg_WS504_4 = 0

avg_EUT_Ohm_1 = 0
avg_EUT_Ohm_2 = 0 
avg_EUT_Ohm_3 = 0
avg_EUT_Ohm_4 = 0

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
    global step

    generate_csv_headers()

    venus_send_command(temperature)

    
    
    elapsed_time_check_seconds = time_to_seconds(elapsed_time_check)
    while True:

        


        # WS504_T = fur_send_enquiry(7, 'Temp', '\x0401L002\x05z')
        WS504_T = fur_send_enquiry(3, 'Temp', '01L002')
        print(WS504_T)

        # EUT_mA = fur_send_enquiry(7, 'mA','\x0401L002\x05z')
        EUT_Ohm = agilent_send_enquiry()
        if response is None:
            print ("failed to get a valid response from instrument check serial connection")
        print (EUT_Ohm)

        ISOTECH_T = tt10_send_enquiry()
        print(ISOTECH_T)

        current_time = datetime.now()
        elapsed_time = current_time - start_time
        current_time = current_time.strftime("%H:%M:%S")

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_time, elapsed_time, ISOTECH_T, WS504_T,EUT_Ohm])
        
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
    global avg_EUT_Ohm_1, avg_EUT_Ohm_2, avg_EUT_Ohm_3, avg_EUT_Ohm_4, avg_EUT_Ohm_5, avg_EUT_Ohm_6, avg_EUT_Ohm_7
    global avg_ISOTECH_1, avg_ISOTECH_2, avg_ISOTECH_3, avg_ISOTECH_4, avg_ISOTECH_5, avg_ISOTECH_6, avg_ISOTECH_7
    global avg_WS504_1, avg_WS504_2, avg_WS504_3, avg_WS504_4, avg_WS504_5, avg_WS504_6, avg_WS504_7
    global diff_1, diff_2, diff_3, diff_4, diff_5, diff_6, diff_7
    global condition_1, condition_2, condition_3, condition_4, condition_5, condition_6, condition_7

    sum_ISOTECH = 0
    sum_WS504_T = 0
    sum_EUT_Ohm = 0

    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([])
        writer.writerow(["End Point Readings:"])

    for i in range (20):    
        ISOTECH_T = float(tt10_send_enquiry())
        sum_ISOTECH = sum_ISOTECH + ISOTECH_T
        print (sum_ISOTECH)
        
        WS504_T = float(fur_send_enquiry(3, 'Temp', '01L002'))
        sum_WS504_T = sum_WS504_T + WS504_T
        print (sum_WS504_T)

        EUT_Ohm = agilent_send_enquiry()
        sum_EUT_Ohm = sum_EUT_Ohm + EUT_Ohm
        print (sum_EUT_Ohm)


        current_time = datetime.now()
        elapsed_time = current_time - start_time
        current_time = current_time.strftime("%H:%M:%S")  

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_time, elapsed_time, ISOTECH_T, WS504_T,EUT_Ohm])  
     

    avg_ISOTECH_T = round(sum_ISOTECH/20, 3)
    print (avg_ISOTECH_T)

    avg_WS504_T = round(sum_WS504_T/20, 3)
    print (WS504_T)

    avg_EUT_Ohm = round(sum_EUT_Ohm/20, 3)
    print (EUT_Ohm)

    diff = round(abs( avg_ISOTECH_T - avg_WS504_T), 3)
    print(diff)

    sum_ISOTECH = 0
    sum_WS504_T = 0
    sum_EUT_Ohm = 0

    # store averags based on step value
    if step == 1:
        avg_ISOTECH_1 = avg_ISOTECH_T
        avg_WS504_1 = avg_WS504_T
        avg_EUT_Ohm_1 = avg_EUT_Ohm
        diff_1 = diff
        if diff_1 > 0.1:
            condition_1 = "Fail"
        else:
            condition_1 = "Pass"
        step += 1
        return avg_ISOTECH_1, avg_WS504_1, avg_EUT_Ohm_1, diff_1, condition_1, step       

    elif step == 2:
        avg_ISOTECH_2 = avg_ISOTECH_T
        avg_WS504_2 = avg_WS504_T
        avg_EUT_Ohm_2 = avg_EUT_Ohm  
        diff_2 = diff
        if diff_2 > 0.1:
            condition_2 = "Fail"
        else:
            condition_2 = "Pass"
        step += 1
        return avg_ISOTECH_2, avg_WS504_2, avg_EUT_Ohm_2, diff_2, condition_2, step
    
    elif step == 3:
        avg_ISOTECH_3 = avg_ISOTECH_T
        avg_WS504_3 = avg_WS504_T
        avg_EUT_Ohm_3 = avg_EUT_Ohm
        diff_3 = diff
        if diff_3 > 0.1:
            condition_3 = "Fail"
        else:
            condition_3 = "Pass"
        step += 1
        return avg_ISOTECH_3, avg_WS504_3, avg_EUT_Ohm_3, diff_3, condition_3, step
    
    elif step == 4:
        avg_ISOTECH_4 = avg_ISOTECH_T
        avg_WS504_4 = avg_WS504_T
        avg_EUT_Ohm_4 = avg_EUT_Ohm
        diff_4 = diff
        if diff_4 > 0.1:
            condition_4 = "Fail"
        else:
            condition_4 = "Pass"
        step += 1
        return avg_ISOTECH_4, avg_WS504_4, avg_EUT_Ohm_4, diff_4, condition_4, step

    elif step == 5:
        avg_ISOTECH_5 = avg_ISOTECH_T
        avg_WS504_5 = avg_WS504_T
        avg_EUT_Ohm_5 = avg_EUT_Ohm
        diff_5 = diff
        if diff_5 > 0.1:
            condition_5 = "Fail"
        else:
            condition_5 = "Pass"
        step += 1
        return avg_ISOTECH_5, avg_WS504_5, avg_EUT_Ohm_5, diff_5, condition_5, step    

    elif step == 6:
        avg_ISOTECH_6 = avg_ISOTECH_T
        avg_WS504_6 = avg_WS504_T
        avg_EUT_Ohm_6 = avg_EUT_Ohm
        diff_6 = diff
        if diff_6 > 0.1:
            condition_6 = "Fail"
        else:
            condition_6 = "Pass"
        step += 1
        return avg_ISOTECH_6, avg_WS504_6, avg_EUT_Ohm_6, diff_6, condition_6, step   

    elif step == 7:
        avg_ISOTECH_7 = avg_ISOTECH_T
        avg_WS504_7 = avg_WS504_T
        avg_EUT_Ohm_7 = avg_EUT_Ohm
        diff_7 = diff
        if diff_7 > 0.1:
            condition_7 = "Fail"
        else:
            condition_7 = "Pass"
        step += 1
        return avg_ISOTECH_7, avg_WS504_7, avg_EUT_Ohm_7, diff_7, condition_7, step   

    # else:
    #     with open(csv_file_path, mode='a', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow([])
    #         writer.writerow(["Average RS80 Temp", "Aveage WS504 Temp", "Average EUTOhm", "Check Difference", "Pass/Fail"])
    #         writer.writerow([avg_ISOTECH_1, avg_WS504_1, avg_EUT_Ohm_1, diff_1, condition_1])
    #         writer.writerow([avg_ISOTECH_2, avg_WS504_2, avg_EUT_Ohm_2, diff_2, condition_2])
    #         writer.writerow([avg_ISOTECH_3, avg_WS504_3, avg_EUT_Ohm_3, diff_3, condition_3])
    #         writer.writerow([avg_ISOTECH_4, avg_WS504_4, avg_EUT_Ohm_4, diff_4, condition_4]) 

    # return    



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
    elif device == 3:
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
    ser = serial_connections[14] 
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

def venus_send_command(temperature):

    if temperature == 0:
        ser = serial_connections[2]
        command = b'\x01\x10\x80\x04\x00\x02\x04\x00\x00\x00\x00\x93\x9A'# Command for 0°C set point
        if not ser.is_open:
            ser.open()

        ser.write(command)


        ser.close()        

    elif temperature == 10:
        ser = serial_connections[2]
        command = b'\x01\x10\x80\x04\x00\x02\x04\x41\x20\x00\x00\x86\x6C' # Command for 10°C set point
        if not ser.is_open:
            ser.open()

        ser.write(command)


        ser.close()

    elif temperature == 20:
        ser = serial_connections[2]
        command = b'\x01\x10\x80\x04\x00\x02\x04\x41\xA0\x00\x00\x87\x84' #Command for 20°C set point
        if not ser.is_open:
            ser.open()

        ser.write(command)


        ser.close()

    elif temperature == 35:
        ser = serial_connections[2]
        command = b'\x01\x10\x80\x04\x00\x02\x04\x42\x0C\x00\x00\x47\xE1' #Command for 35°C set point
        if not ser.is_open:
            ser.open()

        ser.write(command)


        ser.close()    

    elif temperature == 50:
        ser = serial_connections[2]
        command = b'\x01\x10\x80\x04\x00\x02\x04\x42\x48\x00\x00\x07\xF4' #Command for 50°C set point
        if not ser.is_open:
            ser.open()

        ser.write(command)


        ser.close()  

def agilent_send_enquiry():
    ser = serial_connections[7]
    commands = [
    b'SYST:REMOTE\r\n',
    b'*CLS\r\n',
    b'func "FRES"\r\n',
    b'conf:FRES DEF,DEF\r\n',
    b'READ?\r\n'
] 
    try:
        if not ser.is_open:
            ser.open()

        for command in commands:
            ser.write(command)
            time.sleep(0.1)

        response_str = ''
        while True:
            time.sleep(0.1)
            response_bytes = ser.read(1000)
            response_str = response_bytes.decode().strip()

            if response_str:  # Continue only if response is not empty
                try:
                    response = float(response_str)
                    break  # Break the loop if a valid numeric response is received
                except ValueError:
                    print(f"Error: Received a non-numeric response: {response_str}")
                    response_str = ''  # Reset response_str to continue the loop

    except serial.SerialException as e:
        print(f"Serial communication error: {e}")
        response = None

    finally:
        if ser.is_open:
            ser.close()

    return response


    # if not ser.is_open:
    #     ser.open()

    # for command in commands:
    #     ser.write(command)  
    #     time.sleep(0.1)

    #     response_str = ''
    #     while True:
    #         time.sleep(0.1)
    #         response_bytes = ser.read(1000)
    #         response_str = response_bytes.decode().strip()

    #         if response_str:  # Continue only if response is not empty
    #             try:
    #                 response = float(response_str)
    #                 break  # Break the loop if a valid numeric response is received
    #             except ValueError:
    #                 print(f"Error: Received a non-numeric response: {response_str}")
    #                 response_str = ''  # Reset response_str to continue the loop    

      
    # # time.sleep(0.1)
    # # response_str = ser.read(1000)
    # # response_str = response_str.decode().strip()
    # # response = float(response_str)
    # # ser.close()

    # return response
 
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




def set_csv_file_path(path):
    global csv_file_path
    csv_file_path = path

def generate_csv_headers():
    headers = ["Time", "Elapsed", "RS80 Temp", "WS504 Temp", "EUT Ohm"]
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([])
        writer.writerow(headers)

def output_avgs():
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([])
        writer.writerow(["Average RS80 Temp", "Aveage WS504 Temp", "Average EUTOhm", "Check Difference", "Pass/Fail"])
        writer.writerow([avg_ISOTECH_1, avg_WS504_1, avg_EUT_Ohm_1, diff_1, condition_1])
        writer.writerow([avg_ISOTECH_2, avg_WS504_2, avg_EUT_Ohm_2, diff_2, condition_2])
        writer.writerow([avg_ISOTECH_3, avg_WS504_3, avg_EUT_Ohm_3, diff_3, condition_3])
        writer.writerow([avg_ISOTECH_4, avg_WS504_4, avg_EUT_Ohm_4, diff_4, condition_4])
        writer.writerow([avg_ISOTECH_5, avg_WS504_5, avg_EUT_Ohm_5, diff_5, condition_5])
        writer.writerow([avg_ISOTECH_6, avg_WS504_6, avg_EUT_Ohm_6, diff_6, condition_6])
        writer.writerow([avg_ISOTECH_7, avg_WS504_7, avg_EUT_Ohm_7, diff_7, condition_7])
   

    





