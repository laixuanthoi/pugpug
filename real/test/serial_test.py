import serial
import time
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 56700,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
        )

counter=0
          
      
while 1:
    print("write {}".format(counter))
    ser.write('Write counter: %d \n'%(counter))
    time.sleep(0.001)
    counter += 1