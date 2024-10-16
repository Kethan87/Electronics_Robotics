import boot


while True:
    imu.TiltAngle()
    roll = mem32[imu.reg_tilt_angle][0]
    pitch = mem32[imu.reg_tilt_angle][1]
    print("Roll: ", tiltangle[0])
    print("Pitch: ", tiltangle[1])
    
    if machine.mem8[0x14] != 0:
        if abs(roll) < machine.mem8[0x14] and abs(pitch) < machine.mem8[0x14]:
            #green led on red ledd off
            
        else:
            #red led on green led off
    
    if machine.mem8[0x15] != 0:
        if abs(roll) < machine.mem8[0x15] and abs(pitch) < machine.mem8[0x15]:
            #green led on red ledd off
            
        else:
            #red led on green led off