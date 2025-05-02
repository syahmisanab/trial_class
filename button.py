from gpiozero import Button, OutputDevice, LED, PWMOutputDevice
import time

# Define components 
buzzer = PWMOutputDevice(17)  
led = LED(14)
row = Button(13, pull_up=True)
column = OutputDevice(24, initial_value=True)

def check_button():
    column.off()  # Activate column
    time.sleep(0.05)

    if row.is_pressed:
        print("Button Pressed! Turning ON device")
        buzzer.value = 0.5  # Change to led.on() to use LED instead
    else:
        buzzer.off()  # Change to led.off() to use LED instead

    column.on()  # Deactivate column

while True:
    check_button()
    time.sleep(0.1)  # Prevent accidental multiple detections
