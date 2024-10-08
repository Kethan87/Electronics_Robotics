import esp
import boot
import time
esp.osdebug(None)
from machine import Pin

while True:
    print((ADC_VS.read_uv() / 1000))
    time.sleep(0.5)

