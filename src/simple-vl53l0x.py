import time

import adafruit_vl53l0x
import board
import busio

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

while True:
    print('Range: {0}mm'.format(vl53.range))
    time.sleep(.2)
