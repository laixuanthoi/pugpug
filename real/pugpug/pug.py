import numpy as np
from kinematic import Kinematic
from control.trotting import Trotting
from control.gait import Gait
from enum import Enum

class BehaviorState(Enum):
    DEACTIVATED = -1
    REST = 0
    TROT = 1
    HOP = 2
    FINISHHOP = 3

class State:
    def __init__(self):
        self.horizontal_velocity = np.array([0.0, 0.0])
        self.yaw_rate = 0.0
        self.height = -0.16
        self.pitch = 0.0
        self.roll = 0.0
        self.activation = 0
        self.behavior_state = BehaviorState.REST
        self.foot_locations = np.zeros((3, 4))
        self.joint_angles = np.zeros((3, 4))

class Pugpug:
    def __init__(self):
        self.state = State()
        self.ik = Kinematic(self.cfg)
        self.trotting = Trotting(self.cfg)
        self.gait = Gait(self.cfg)


    def runByCommand(self, cmd):
        pass
    
        

    



