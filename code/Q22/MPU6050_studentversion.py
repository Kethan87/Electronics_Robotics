import math
import machine
import HighLevelController

# The function convert_to_int16(msb, lsb) converts 2 bytes to a signed integer.
# Argument msb is the most significant byte, argument lsb is the least significant byte
def convert_to_int16(msb, lsb):
    value = msb  * 256 + lsb						# unsigned value
    return value - 65536 if msb & 0x80 else value	# Return 2-complenents value if msbit is 1

# The class MPU6050 provides a simple interface to read data from the MPU6050 sensor
# The constructor initializes the MPU6050 sensor and defines attributes acc, yaw and T to store the sensor data
# The method readData() reads the raw sensor data and converts it units of [m/s^2/, [°/s] and [°C]

class MPU6050():

    # The constructor of the MPU6050 class has 2 arguments:
    # i2c: an object of the SoftI2C module.
    # address: the i2c address of the mpu6050 device
    def __init__(self, i2c, address):
        self.i2c = i2c
        self.write = 2 * address
        self.read = 2 * address + 1
        i2c.start() 
        i2c.write(bytearray([self.write, 107, 1]))	# What is this command doing?
        i2c.stop()
        self.acc = [0.0] * 3						# List of 3 elements to store accelaration in [m/s^2]
        self.buf1 = bytearray([self.write, 0x3B])	# 0x3B is first address of acceleration data
        self.buf2 = bytearray([self.read])			# Bytearray is transmitted to request accelaration
        self.readBuffer = bytearray([0]*6)			# Bytearray is used to store the acceleration data
        HighLevelController.reg[20] = 0
        HighLevelController.reg[21] = 0
        self.reg_acc_x = 3;
        self.reg_acc_y = 4;
        self.reg_acc_z = 5;
        self.reg_tilt_angle = 6;
        
    # The method readData() has no arguments and no return value. It reads the reads the acceleration and 
    # converts it into units of [m/s^2]. The acceleration is stored in list attribute acc
    def readData(self):
        self.i2c.start()							# Start bit
        self.i2c.write(self.buf1)					# Transmit write address + address of data
        self.i2c.start()							# Repeated start bit
        self.i2c.write(self.buf2)					# Transmit read address
        self.i2c.readinto(self.readBuffer)			# Read data
        self.i2c.stop()								# Stop bit
        for i in range(3):
            raw = convert_to_int16(self.readBuffer[i*2], self.readBuffer[i*2+1])	# Read raw accelaration data
            #self.acc[i] = raw * ...					# Enter the correct factor to convert the acceleration to [m/s2]
            self.acc[i] = raw / 16384 * 9.81 #2^15 / 2 = 16384 * 9.81(for gravitation to m/s2) 
        
    # The method tiltAngle() first reads the acceleration in the 3 directions.
    # Then it calculates the tilt angle in degrees and returns it
#     def tiltAngle(self):
#         self.readData()
#         tiltAngle = ...								# Enter here the formula(s) to calculate he tiltAngle in degrees
#         return tiltAngle
    def tiltAngle(self):
        self.readData()
        
        ax = self.acc[0]  # Acceleration in x direction [m/s^2]
        ay = self.acc[1]  # Acceleration in y direction [m/s^2]
        ay += 4.2
        az = self.acc[2]  # Acceleration in z direction [m/s^2]

        roll = math.atan2(ay, math.sqrt(ax**2 + az**2)) * (180 / math.pi)

        pitch = math.atan2(-ax, math.sqrt(ay**2 + az**2)) * (180 / math.pi) + 90
        
 

        return roll, pitch

    def TiltAngle(self):
        tiltAngles = self.tiltAngle()
        ax = self.acc[0]  # Acceleration in x direction [m/s^2]
        ay = self.acc[1]  # Acceleration in y direction [m/s^2]
        az = self.acc[2]  # Acceleration in z direction [m/s^2]
        HighLevelController.reg[self.reg_acc_x] = int(ax)
        HighLevelController.reg[self.reg_acc_y] = int(ay)
        HighLevelController.reg[self.reg_acc_z] = int(az)
        if abs(tiltAngles[0]) > abs(tiltAngles[1])	:
            HighLevelController.reg[self.reg_tilt_angle] = int(tiltAngles[0])
        else:
            HighLevelController.reg[self.reg_tilt_angle] = int(tiltAngles[1])
            
        
        
        






