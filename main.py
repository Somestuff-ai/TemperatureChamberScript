#main function to start temperature calibration using Oven, Oven Controller, FCO56 and WS504

from datetime import datetime, timedelta
from functions import run_temperature_test

def main():
    #step = 1
    run_temperature_test(10, "00:00:10", 1)
    run_temperature_test(20, "00:00:20", 1)
    run_temperature_test(30, "00:00:30", 1)
    run_temperature_test(20, "00:00:40", 1)

if __name__ == "__main__":
    main()