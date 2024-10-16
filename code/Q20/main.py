import math
import time
import boot

# Main loop

while True:
    input("Press Enter to read sensor data...")  # Wait for user to press enter
    
    # Read data from MPU6050
    imu.readData()
    ax, ay, az = imu.acc  # Acceleration in x, y, z directions
    ay += 4.2
    roll, pitch = imu.tiltAngle()  # Tilt angle in roll and pitch

    # Print acceleration data
    print(f"Acceleration (m/s^2): X = {ax:.2f}, Y = {ay:.2f}, Z = {az:.2f}")
    
    # Print tilt angles
    print(f"Tilt angles: Roll = {roll:.2f}°, Pitch = {pitch:.2f}°")
    print("")
    print("")
    
    time.sleep(0.5)  # Delay to avoid flooding the console

