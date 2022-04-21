from periphery import GPIO
import time


led_pin = 6
gpio = GPIO(led_pin, "out")

try:
    while 1:
        print("turn on led")
        gpio.write(True)
        time.sleep(2)
        print("turn off led")
        gpio.write(False)
        time.sleep(2)

except KeyboardInterrupt:
    gpio.write(False)
    gpio.close()

print(" ")
print("done")
