from gpiozero import PWMOutputDevice
from time import sleep

buzzer = PWMOutputDevice(17)

# Define melody (list of duty cycle values for different tones)
melody = [0.1, 0.3, 0.5, 0.7, 0.9]  # Add at least 5 values (0.0 to 1.0)

try:
    for tone in melody:
        buzzer.value = tone  # Set the buzzer to the current tone
        sleep(0.5)  # Choose how long each note should last
    buzzer.off()
except KeyboardInterrupt:
    print("\nExiting program...")
