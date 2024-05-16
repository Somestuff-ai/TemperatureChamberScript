#main function to start temperature calibration using Oven, Oven Controller, FCO56 and WS504

import tkinter as tk
from tkinter import simpledialog
from functions import run_temperature_test
from datetime import datetime, timedelta
from functions import run_temperature_test

def get_user_inputs():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    inputs = []
    for i in range(1,4):
        temperature = simpledialog.askinteger("Input", f"Enter temperature for measurement {i}:")
        time_elapsed = simpledialog.askstring("Input", f"Enter time elapsed for measurement {i} (HH:MM:SS format):")
        sleep_time = simpledialog.askinteger("Input", f"Enter sleep time for measurement {i} (in seconds):")
        inputs.append((temperature, time_elapsed, sleep_time))

    return inputs


def main():
    measurements = get_user_inputs()
    for temperature, time_elapsed, sleep_time in measurements:
        run_temperature_test(temperature, time_elapsed, sleep_time)    

    # run_temperature_test(10, "00:02:00", 1)
    # run_temperature_test(20, "00:04:00", 1)
    # run_temperature_test(30, "00:06:00", 1)
    # run_temperature_test(20, "00:08:00", 1)

if __name__ == "__main__":
    main()