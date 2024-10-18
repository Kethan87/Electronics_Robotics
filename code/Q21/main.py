import boot

# Setup UART2
uart2 = UART(2, baudrate=115200, bits=8, parity=None, stop=1)

BUZZER = Pin(22, Pin.OUT)

# Define the pins for switches
SWITCH_1 = Pin(32, Pin.IN, Pin.PULL_UP)
SWITCH_2 = Pin(33, Pin.IN, Pin.PULL_UP)

# Initial values for LEDs and buzzer
red_state = 0
green_state = 0
blue_state = 0
buzzer_state = 0

# Bytearray for receiving data
input_buffer = bytearray(10)

while True:
    # Read from UART2
    if uart2.any():
        uart2.readinto(input_buffer)
        char = chr(input_buffer[0])

        # Handle received character
        if char == 'R':
            red_state = not red_state
            RED_LED.value(red_state)
            print("Red LED toggled")

        elif char == 'G':
            green_state = not green_state
            GREEN_LED.value(green_state)
            print("Green LED toggled")

        elif char == 'B':
            blue_state = not blue_state
            BLUE_LED.value(blue_state)
            print("Blue LED toggled")

#         elif char == 'A':
#             buzzer_state = not buzzer_state
#             if buzzer_state:
#                 BUZZER.freq(500)  # Set frequency to 500Hz
#             BUZZER.value(buzzer_state)
#             print("Buzzer toggled")

#     # Check switches and send messages
#     if not SWITCH_1.value():
#         uart2.write("Switch 1 is pressed\n")
#         print("Switch 1 is pressed")
#         time.sleep(0.5)  # Debounce delay
# 
#     if not SWITCH_2.value():
#         uart2.write("Switch 2 is pressed\n")
#         print("Switch 2 is pressed")
#         time.sleep(0.5)  # Debounce delay

