import boot

# Setup UART2
uart2 = UART(2, baudrate=115200, bits=8, parity=None, stop=1)

BUZZER = PWM(Pin(4,Pin.OUT), freq=440, duty=0)

def buzzer_on():
    BUZZER.duty(520)
    BUZZER.freq(500)

def buzzer_off():
    BUZZER.duty(0)

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

        elif char == 'A':
            buzzer_state = not buzzer_state
            if buzzer_state:
                buzzer_on()  # Set frequency to 500Hz
            else:   
                buzzer_off()
            print("Buzzer toggled")


