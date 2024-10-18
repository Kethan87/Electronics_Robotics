import boot
import HighLevelController
import MPU6050_studentversion

# BUZZER.freq(1000)  # Set frequency to 1kHz
# BUZZER.duty(0)  # Start with 0 duty cycle (buzzer off)

BUZZER = PWM(Pin(4,Pin.OUT), freq=440, duty=0)


def buzzer_on():
    BUZZER.duty(520)
    BUZZER.freq(500)

def buzzer_off():
    BUZZER.duty(0)

while True:
    imu.TiltAngle()
    tilt = HighLevelController.reg[imu.reg_tilt_angle]
    print("TILT: ", tilt)
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
            print("BUZZER TIMEEEEEEEEEEE!!!!")
            #ADD BUZZZEERR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




