# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from machine import Pin, ADC, PWM, I2C, SoftI2C, UART
import Encoder
import MPU6050_studentversion
import HighLevelController
import TCPHandler
pin13 = Pin(13, Pin.OUT)
pin13.value(0)
RED_LED = Pin(18, Pin.OUT)
GREEN_LED = Pin(5, Pin.OUT)
BLUE_LED = Pin(19, Pin.OUT)

tone = 5000

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
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
imu = MPU6050_studentversion.MPU6050(i2c, 0x68)
uart2 = UART(2, baudrate=115200, bits=8, parity=None, stop=1)
tcp = TCPHandler.TCPHandler("6g toren", "letterlijkhetwachtwoord", 12345, Pin(2))
highLevelController = HighLevelController.HighLevelController(uart2, tcp)







