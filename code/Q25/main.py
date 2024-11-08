import boot
import HighLevelController
import MPU6050_studentversion
import time

BUZZER = PWM(Pin(4,Pin.OUT), freq=440, duty=0)
STATE = 0
DUTY_CYCLE = 0

pin13 = Pin(13, Pin.OUT)
pin13.on()


def buzzer_on():
    BUZZER.duty(520)
    BUZZER.freq(500)

def buzzer_off():
    BUZZER.duty(0)

def stateOff():
    global DUTY_CYCLE
    DUTY_CYCLE = 0
    motorControl()

def stateTest():
    pin25.duty(HighLevelController.reg[22])
    pin26.duty(HighLevelController.reg[23])

def stateControl():
    global DUTY_CYCLE
    goalRPM = HighLevelController.reg[10]
    limitTorque = HighLevelController.reg[11]
    currentRPM = HighLevelController.reg[7]
    currentTorque = HighLevelController.reg[8]
    
    ki = 3
    error = goalRPM - currentRPM
    timeSample = 0.2 #the sleep time in the main loop times 2
    
    deltaDC = int(ki * error * timeSample) 
    
    if (currentTorque < limitTorque or limitTorque == 0):
        DUTY_CYCLE += deltaDC
    else:
        DUTY_CYCLE -= deltaDC
        
    motorControl()

def tiltControl():
    if HighLevelController.reg[20] != 0:
        if abs(HighLevelController.reg[imu.reg_tilt_angle]) < HighLevelController.reg[20]:
            RED_LED.value(0)
            GREEN_LED.value(1)
        else:
            RED_LED.value(1)
            GREEN_LED.value(0)
        
    
    if HighLevelController.reg[21] != 0:
        if abs(HighLevelController.reg[imu.reg_tilt_angle]) < HighLevelController.reg[21]:
            RED_LED.value(0)
            GREEN_LED.value(1)
            buzzer_off()
        else:
            RED_LED.value(1)
            GREEN_LED.value(0)
            buzzer_on()
            DUTY_CYCLE = 0

def configureHighLevelDriver():
    i0 = -3.266 #milliamp from question 18
    c2 = 1.918 #slope from question 18
    
    HighLevelController.reg[0] = int(4.8017 * (ADC_VS.read_uv() / 1000))
    HighLevelController.reg[1] = int(i0 + c2 * (ADC_CS.read_uv() / 10000))
    HighLevelController.reg[2] = Encoder.GetFrequency()
    HighLevelController.reg[7] = int(HighLevelController.reg[2] / HighLevelController.reg[13]) #Encoder frequency / Encoder pulses
    HighLevelController.reg[8] = int(HighLevelController.reg[1] * 0.00990217) # from Question 18

def motorControl():
    global DUTY_CYCLE

    tiltControl()
    if abs(DUTY_CYCLE) <= 950 :
        if DUTY_CYCLE > 0 :
            pin25.duty(DUTY_CYCLE)
            pin26.duty(0)
        else:
            pin25.duty(0)
            pin26.duty(DUTY_CYCLE * -1)
    
    
    

while True:
    state = tcp.getState()
    highLevelController.readFromUart()
    imu.TiltAngle()
    configureHighLevelDriver()
    highLevelController.readFromTCP()
    
    if HighLevelController.reg[9] == 1:
        stateTest()
    elif HighLevelController.reg[9] == 2:
        stateControl()
    else:
        stateOff()
            
    
    time.sleep(0.1)






