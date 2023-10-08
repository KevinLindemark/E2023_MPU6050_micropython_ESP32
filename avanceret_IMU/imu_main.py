from imu import MPU6050  # https://github.com/micropython-IMU/micropython-mpu9x50
import time
from machine import Pin, I2C

i2c = I2C(0)
imu = MPU6050(i2c)

# Temperature display
print("Temperature: ", round(imu.temperature,2), "°C")

while True:
    # reading values
    acceleration = imu.accel
    gyroscope = imu.gyro  
    print ("Acceleration x: ", round(acceleration.x,2), " y:", round(acceleration.y,2),
           "z: ", round(acceleration.z,2))

    print ("gyroscope x: ", round(gyroscope.x,2), " y:", round(gyroscope.y,2),
           "z: ", round(gyroscope.z,2))

# data interpretation (accelerometer)

    if abs(acceleration.x) > 0.8:
        if (acceleration.x > 0):
            print("The x axis points upwards")
        else:
            print("The x axis points downwards")

    if abs(acceleration.y) > 0.8:
        if (acceleration.y > 0):
            print("The y axis points upwards")
        else:
            print("The y axis points downwards")

    if abs(acceleration.z) > 0.8:
        if (acceleration.z > 0):
            print("The z axis points upwards")
        else:
            print("The z axis points downwards")

# data interpretation (gyroscope)

    if abs(gyroscope.x) > 20:
        print("Rotation around the x axis")

    if abs(gyroscope.y) > 20:
        print("Rotation around the y axis")

    if abs(gyroscope.z) > 20:
        print("Rotation around the z axis")
    
    time.sleep(0.2)