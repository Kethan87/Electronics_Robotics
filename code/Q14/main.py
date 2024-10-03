import esp
esp.osdebug(None)
from machine import Pin

PUSH_BUTTON1 = Pin(39, Pin.IN, Pin.PULL_UP)
PUSH_BUTTON2 = Pin(36, Pin.IN, Pin.PULL_UP)
PUSH_BUTTON3 = Pin(23, Pin.IN, Pin.PULL_UP)
RED_LED = Pin(18, Pin.OUT)
GREEN_LED = Pin(5, Pin.OUT)
BLUE_LED = Pin(19, Pin.OUT)

red_value = 0
green_value = 0
blue_value = 0

def button1_isr(pin):
    global red_value
    if pin.value() == 0:
        RED_LED.value(red_value)
        red_value = (red_value + 1) % 2

def button2_isr(pin):
    global green_value
    if pin.value() == 0:
        GREEN_LED.value(green_value)
        green_value = (green_value + 1) % 2

def button3_isr(pin):
    global blue_value
    if pin.value() == 0:
        BLUE_LED.value(blue_value)
        blue_value = (blue_value + 1) % 2

PUSH_BUTTON1.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=button1_isr)
PUSH_BUTTON2.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=button2_isr)
PUSH_BUTTON3.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=button3_isr)

while True:
    pass

