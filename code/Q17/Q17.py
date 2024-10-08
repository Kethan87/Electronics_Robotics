import esp
import boot
import time
esp.osdebug(None)
from machine import Pin

pin13 = Pin(13, Pin.OUT)
pin13.on()

while True:
    #print((ADC_VS.read_uv() / 1000))
    dc = int(input("Input a duty cycle of between -950 and 950."))
    if abs(dc) <= 950 :
        if dc > 0 :
            pin25.duty(dc)
            pin26.duty(0)
        else:
            pin25.duty(0)
            pin26.duty(dc * -1)
