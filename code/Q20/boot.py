# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from machine import Pin, ADC, I2C

pin13 = Pin(13, Pin.OUT)
pin13.value(0)


ADC_CS = ADC(32)
ADC_VS = ADC(33)

ADC_CS.atten(ADC.ATTN_11DB)
ADC_VS.atten(ADC.ATTN_11DB)


ADC_CS.width(ADC.WIDTH_12BIT)
ADC_VS.width(ADC.WIDTH_12BIT)

i2c = I2C(0, scl=14, SDA=11, freq=400000)



