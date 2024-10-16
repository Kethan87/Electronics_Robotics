# import MPU6050_studentversion
# import boot
# 
# 
# if __name__ == "__main__":
#     # Assume you have i2c initialized properly, for example:
#     # i2c = SoftI2C(scl=Pin(22), sda=Pin(21))  # Define pins for your platform
#     
#     # Set up the MPU6050 with an example address (commonly 0x68)
#     mpu = MPU6050(i2c, 0x68)
# 
#     print("Press Enter to get sensor readings (Ctrl+C to exit).")
# 
#     try:
#         while True:
#             input("Press Enter...")  # Wait for user to press enter
#             mpu.readData()
#             roll, pitch = mpu.tiltAngle()
#             
#             print(f"Acceleration [m/s^2]: X = {mpu.acc[0]:.2f}, Y = {mpu.acc[1]:.2f}, Z = {mpu.acc[2]:.2f}")
#             print(f"Roll: {roll:.2f} degrees, Pitch: {pitch:.2f} degrees\n")
# 
#     except KeyboardInterrupt:
#         print("Program stopped.")
#     

while True:
    input("Press Enter to read sensor data...")  # Wait for user to press enter
    
    # Read data from MPU6050
    imu.readData()
    ax, ay, az = imu.acc  # Acceleration in x, y, z directions
    roll, pitch = imu.tiltAngle()  # Tilt angle in roll and pitch

    # Print acceleration data
    print(f"Acceleration (m/s^2): X = {ax:.2f}, Y = {ay:.2f}, Z = {az:.2f}")
    
    # Print tilt angles
    print(f"Tilt angles: Roll = {roll:.2f}°, Pitch = {pitch:.2f}°")