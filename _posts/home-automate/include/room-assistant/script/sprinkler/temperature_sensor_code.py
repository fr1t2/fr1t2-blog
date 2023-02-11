
# Temp DS180b20 reading into F result on raspi
#
# https://pimylifeup.com/raspberry-pi-temperature-sensor/
# Modified from
#   - git clone https://github.com/pimylifeup/temperature_sensor.git

import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    lines = []
    i = 0
    # try to read the file 20 times, return the result
    while not lines and (i < 19):
        try:
            f = open(device_file, 'r')
            lines = f.readlines()
            i += 1
        except NameError:
            time.sleep(1)
        else:
            if not lines:
                f.close()
            else:
                f.close()
                return lines

def read_temp():
    lines = read_temp_raw()
    if lines[0].strip()[-3:] != 'YES':
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f

# print to reduced decimal place
print('{0:06.3f}'.format(read_temp()))


