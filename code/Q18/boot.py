# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from machine import Pin, ADC, PWM, I2C
import Encoder
pin13 = Pin(13, Pin.OUT)
pin13.value(0)

encA = 34
encB = 35

ADC_CS = ADC(32)
ADC_VS = ADC(33)

pin25 = PWM(Pin(25), freq=50000, duty=0)
pin26 = PWM(Pin(26), freq=50000, duty=0)

ADC_CS.atten(ADC.ATTN_11DB)
ADC_VS.atten(ADC.ATTN_11DB)


ADC_CS.width(ADC.WIDTH_12BIT)
ADC_VS.width(ADC.WIDTH_12BIT)

Encoder.InitEncoder(encA, encB)
