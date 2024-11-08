import boot
import HighLevelController
import MPU6050_studentversion
import time

BUZZER = PWM(Pin(4,Pin.OUT), freq=440, duty=0)


def buzzer_on():
    BUZZER.duty(520)
    BUZZER.freq(500)

def buzzer_off():
    BUZZER.duty(0)

while True:
    state = tcp.getState()
    highLevelController.readFromUart()
    imu.TiltAngle()
    tilt = HighLevelController.reg[imu.reg_tilt_angle]
    dc = HighLevelController.reg[22]
    
    
    if HighLevelController.reg[20] != 0:
        if abs(tilt) < HighLevelController.reg[20]:
            RED_LED.value(0)
            GREEN_LED.value(1)
        else:
            RED_LED.value(1)
            GREEN_LED.value(0)
        
    
    if HighLevelController.reg[21] != 0:
        if abs(tilt) < HighLevelController.reg[21]:
            RED_LED.value(0)
            GREEN_LED.value(1)
            buzzer_off()
        else:
            RED_LED.value(1)
            GREEN_LED.value(0)
#             buzzer_on()
    
    i0 = -2966 #milliamp from question 18
    c2 = 1.918 #slope from question 18
    
    HighLevelController.reg[0] = int(4.8017 * (ADC_VS.read_uv() / 1000))
    HighLevelController.reg[1] = int(i0 + c2 * (ADC_CS.read_uv() / 1000))
    HighLevelController.reg[2] = Encoder.GetFrequency()
    HighLevelController.reg[7] = int((HighLevelController.reg[2] * 60 / (HighLevelController.reg[14] / 1000)) / HighLevelController.reg[13]) #Encoder frequency / Encoder pulses
    HighLevelController.reg[8] = int(((HighLevelController.reg[1] - HighLevelController.reg[18]) * 0.00990217) * (HighLevelController.reg[14] / 1000)) # from Question 18
   
    highLevelController.readFromTCP()
    if abs(dc) <= 950 :
        volt = (ADC_VS.read_uv() / 1000000)
        if dc > 0 :
            HighLevelController.reg[22] = dc
            pin25.duty(dc)
            pin26.duty(0)
        else:
            HighLevelController.reg[23] = dc
            pin25.duty(0)
            pin26.duty(dc * -1)
    
    time.sleep(0.1)





