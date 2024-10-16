import boot
import HighLevelController
import MPU6050_studentversion


while True:
    imu.TiltAngle()
    tilt = HighLevelController.reg[imu.reg_tilt_angle]
    
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
        else:
            RED_LED.value(1)
            GREEN_LED.value(0)
            #ADD BUZZZEERR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


