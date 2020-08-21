from mx64 import Mx64
import numpy as np
from time import sleep

PORT = '/dev/ttyS0'
legPair = np.array([
    [1,5,9], #tren giua duoi
    [2,6,10],
    [3,7,11],
    [4,8,12],
], np.int32)


def main():
    servo.setNTorqueEnable(legPair.flatten(),np.zeros(12, np.int32))
    servo.setNTorqueEnable(legPair.flatten(), np.ones(12, np.int32))
    print(servo.getNPresentPosition(legPair.flatten()))
    
    servo.setGoalPosition(legPair[0][2], 2100)

if __name__ == "__main__":
    
    servo = Mx64(PORT)
    try:
        main()
        print("spinning")
        while True:
            sleep(1)
    except Exception as e:
        print(e)
        pass
    finally:
        servo.end()
        print("Port Closing")
        sleep(1)
   