from threading import Thread, Lock
import joy
import time
import kinematic

#joystick process
# joy.setup()
stop_threading = 0
rTime = time.time()
mutex = Lock()

#JOYSTICK
thread_joy = Thread(target=joy.loop, args=(lambda:stop_threading,mutex))
thread_joy.start()

#SIMULATOR


while time.time() - rTime < 5:
    time.sleep(0.01)

print("STOP")
stop_threading = 1
thread_joy.join()
