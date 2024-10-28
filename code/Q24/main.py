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
    
    if HighLevelController.reg[20] != 0:
        if abs(tilt) < HighLevelController.reg[20]:
            RED_LED.value(0)
            GREEN_LED.value(1)
            buzzer_off()
        elif abs(tilt) < HighLevelController.reg[21]:
            RED_LED.value(1)
            GREEN_LED.value(0)
            buzzer_off()
    
    if HighLevelController.reg[21] != 0:
        if abs(tilt) < HighLevelController.reg[21]:
            RED_LED.value(0)
            GREEN_LED.value(1)
            buzzer_off()
        else:
            RED_LED.value(1)
            GREEN_LED.value(0)
            buzzer_on()
    
    i0 = -3.266 #Amp from question 18
    c2 = 1.918 #slope from question 18
    
    HighLevelController.reg[0] = int(i0 + c2 * ADC_VS.read_uv()) #Motor current
    HighLevelController.reg[1] = ADC_VS.read_uv()
    HighLevelController.reg[2] = Encoder.GetFrequency()
    HighLevelController.reg[7] = int(HighLevelController.reg[2] / HighLevelController.reg[13]) #Encoder frequency / Encoder pulses
    HighLevelController.reg[8] = int(HighLevelController.reg[0] * 0.00990217) # from Question 18
    
    highLevelController.readFromTCP()
    
    time.sleep(0.1)




