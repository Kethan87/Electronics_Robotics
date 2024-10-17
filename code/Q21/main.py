import boot
import HighLevelController
import MPU6050_studentversion

red_value = 0
green_value = 0
blue_value = 0
while True:
    character = highLevelController.readFromUart()
    if character  == "R":
        RED_LED.value(red_value)
        red_value = (red_value + 1) % 2
        print("RED")
    elif character  == "G":
        GREEN_LED.value(green_value)
        green_value = (green_value + 1) % 2
        print("GREEN")
    elif character  == "B":
        BLUE_LED.value(blue_value)
        blue_value = (blue_value + 1) % 2
        print("BLUE")

