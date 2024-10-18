from machine import Pin, UART, PWM
import time

RED_LED = Pin(18, Pin.OUT)
GREEN_LED = Pin(5, Pin.OUT)
BLUE_LED = Pin(19, Pin.OUT)

# Initialize UART2 with the required settings
uart2 = UART(2, baudrate=115200, bits=8, parity=None, stop=1)

# UART2 is now configured for communication.

