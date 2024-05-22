#main function to start temperature calibration using Oven, Oven Controller, FCO56 and WS504


import json
from functions import run_temperature_test, output_avgs

def load_config(config.json):
    with open(config.json, 'r') as file:
        config = json.load(config.json)
    return config





def main():
    config = load_config('config.json')

    for test in config['tests']:
        temperature = test[temperature]
        time_elapsed = test[time_elapsed]
        sleep_time = test[sleep_time]

        run_temperature_test(temperature, time_elapsed, sleep_time)

    # run_temperature_test(0, "00:00:10", 1)
    # run_temperature_test(10, "00:00:20", 1)
    # run_temperature_test(20, "00:00:30", 1)
    # run_temperature_test(35, "00:00:40", 1)
    # run_temperature_test(50, "00:00:50", 1)
    # run_temperature_test(20, "00:01:00", 1)
    output_avgs()

if __name__ == "__main__":
    main()