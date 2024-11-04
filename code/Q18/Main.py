import esp
import boot
import time
import Encoder
esp.osdebug(None)
from machine import Pin

pin13 = Pin(13, Pin.OUT)
pin13.on()



while True:
    #print((ADC_VS.read_uv() / 1000))
    dc = int(input("Input a duty cycle of between -950 and 950."))
    if abs(dc) <= 950 :
        volt = (ADC_VS.read_uv() / 1000000)
        
        print("Volt: ", volt)
        print("Encoder Frequency: ",Encoder.GetFrequency())
        if dc > 0 :
            pin25.duty(dc)
            pin26.duty(0)
        else:
            pin25.duty(0)
            pin26.duty(dc * -1)
    i0 = -3.266 #milliamp from question 18
    c2 = 1.918 #slope from question 18
    amp = (i0 + c2 * (ADC_CS.read_uv() / 1000)) / 1000
    print("AMP: ", amp)