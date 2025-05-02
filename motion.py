#!/usr/bin/python3
from gpiozero import MotionSensor, LED
import time
# Initialize the PIR sensor and LED
pir = MotionSensor(27)  # PIR sensor on GPIO 27
led = LED(17)  # LED on GPIO 17
print("Waiting for motion...")
try:
    while True:
        pir.wait_for_motion()
        print("Motion detected! Turning on LED...")
        led.on()
        time.sleep(3)  # Keep LED on for 3 seconds
        led.off()
        print("LED turned off. Waiting for next motion...")
except KeyboardInterrupt:
    print("\nProgram stopped.")
