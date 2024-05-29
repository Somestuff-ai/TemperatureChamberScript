#main function to start temperature calibration using Oven, Oven Controller, FCO56 and WS504

import sys
import json
from functions import run_temperature_test, output_avgs, set_csv_file_path


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <config_file> <csv_file_path>")
        sys.exit(1)

    config_file = sys.argv[1]
    csv_file_path = sys.argv[2]

    # Set the CSV file path
    set_csv_file_path(csv_file_path)

    # Read the config file
    with open(config_file, 'r') as f:
        config_data = json.load(f)

    # Run temperature tests based on config data
    for test in config_data['tests']:
        run_temperature_test(test['temperature'], test['time_elapsed'], test['sleep_time'])
        
    output_avgs()

if __name__ == "__main__":
    main()