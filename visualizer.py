import serial #used to access arduino device
import time
import matplotlib as plt #visualizer
from collections import deque

# replace with your arduino's serial port and baud rate
arduino_port = "/dev/tty.usbmodem21401"
baud_rate = 9600

# initialize deque used to store arduino data (last 100 data elements )
data_buffer = deque( maxlen = 100 )

#create plot for data 
plt.ion()   #turns on interactive mode to update the plot dynamically
fig, ax = plt.subplots()
line, = ax.plots ([],[], label = "Sensor Data")

ax.set_xlim(0, 100) #Display the last 100 points on the x-axis
ax.set_ylim(0, 1024) #asuming the sound sensor ranges from 0-1024

ax.set_xlabel('time')
ax.set_ylabel('sensor value')
ax.legend()


try:
    #establish serial connection 
    arduino = serial.Serial(arduino_port, baud_rate, timeout = 1)
    time.sleep(2)   #waiting for the arduino to intialize

    print("Connected to Arduino YIPPIEEE")

    while True :
        # Read a line of input from the arduino
        data = arduino.readline().decode('utf-8').strip()

        #case in which data is being read
        if data:
            print(f"Received: {data}")

            try:
                sensor_value = int(data) #convert data to int value
                data_buffer.append(sensor_value)
            except ValueError:
                continue #skip non integer data
            
            #update plot
            line.set_xdata(range(len(data_buffer))) #update x values (times)
            line.set_ydata(list(data_buffer)) #updat y values (sensor values)
            plt.draw() #redraw the plot
            plt.pause(0.1) # pause to allow the plot to update


except serial.SerialException as e: 
    print(f"Error connecting to {arduino_port}: {e}")
except KeyboardInterrupt:
    print("Exiting Program.")

finally: 
    if 'arduino' in locals() and arduino.is_open:
        arduino.close()

# no manual way to end execution
