#main function to start temperature calibration using Oven, Oven Controller, FCO56 and WS504

# import tkinter as tk
# from tkinter import simpledialog
from functions import run_temperature_test, output_avgs
from datetime import datetime, timedelta


# def get_user_inputs():
#     root = tk.Tk()
#     root.withdraw()  # Hide the main window

#     inputs = []
#     for i in range(1,4):
#         temperature = simpledialog.askinteger("Input", f"Enter temperature for measurement {i}:")
#         time_elapsed = simpledialog.askstring("Input", f"Enter time elapsed for measurement {i} (HH:MM:SS format):")
#         sleep_time = simpledialog.askinteger("Input", f"Enter sleep time for measurement {i} (in seconds):")
#         inputs.append((temperature, time_elapsed, sleep_time))

#     return inputs


def main():
    run_temperature_test(0, "00:00:10", 1)
    run_temperature_test(10, "00:00:20", 1)
    run_temperature_test(20, "00:00:30", 1)
    run_temperature_test(35, "00:00:40", 1)
    run_temperature_test(50, "00:00:50", 1)
    run_temperature_test(20, "00:01:00", 1)
    output_avgs()

if __name__ == "__main__":
    main()