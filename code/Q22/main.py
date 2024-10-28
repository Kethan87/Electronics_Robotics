import boot
import HighLevelController
import MPU6050_studentversion

BUZZER = PWM(Pin(4,Pin.OUT), freq=440, duty=0)


def buzzer_on():
    BUZZER.duty(520)
    BUZZER.freq(500)

def buzzer_off():
    BUZZER.duty(0)

while True:
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






