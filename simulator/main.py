from threading import Thread, Lock
import joy
import time
import kinematic
import simulator
from pid_control import PID

#joystick process
# joy.setup()
stop_threading = 0
rTime = time.time()
mutex = Lock()

#JOYSTICK
thread_joy = Thread(target=joy.loop, args=(lambda:stop_threading,mutex))
thread_joy.start()

pitch_PID = PID(Kp=0.8,Ki=0.1,Kd=0.2,iMin=-0.1,iMax=0.1,anti_windup=True)
roll_PID = PID(Kp=0.8,Ki=0.1,Kd=0.2,iMin=-0.1,iMax=0.1,anti_windup=True)
yaw_PID = PID(Kp=0.8,Ki=0.1,Kd=0.2,iMin=-0.1,iMax=0.1,anti_windup=True)

def update_to_simulator(stop):
    while not stop():
        simulator.ROLL = pitch_PID.control(joy.joy_axis[0],reference=0.0)
        simulator.PITCH = pitch_PID.control(joy.joy_axis[1],reference=0.0)
        simulator.YAW = pitch_PID.control(joy.joy_axis[2 ],reference=0.0)
        print(simulator.ROLL, joy.joy_axis[0])

        # simulator.ROLL = joy.joy_axis[0]
        # simulator.PITCH = joy.joy_axis[1]
        # simulator.YAW = joy.joy_axis[2]
        time.sleep(0.01)

#SIMULATOR
thread_simulator = Thread(target=update_to_simulator,args=(lambda:stop_threading,))
thread_simulator.start()

simulator.plt.show()

stop_threading = 1
print("STOP")

thread_joy.join()
thread_simulator.join()
