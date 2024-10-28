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
    
    if state == 2:
        received_data = tcp.receive()
        
        if received_data:
            try:
                number = float(received_data.decode().strip())
                squared_value = number ** 2
                response = f"{squared_value}"
            except ValueError:
                response = "No valid number"
            tcp.transmit(response)
    
    time.sleep(0.1)





