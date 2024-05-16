#main function to start temperature calibration using Oven, Oven Controller, FCO56 and WS504

from datetime import datetime, timedelta
from functions import run_temperature_test

def main():
    run_temperature_test(10, "00:02:00", 1)
    run_temperature_test(20, "00:04:00", 1)
    run_temperature_test(30, "00:06:00", 1)
    run_temperature_test(20, "00:08:00", 1)

if __name__ == "__main__":
    main()