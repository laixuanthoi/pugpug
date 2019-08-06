from mx64 import Mx64
from control.trotting import Trotting
from kinematic import Kinematic
from math import *

RC_0 = 7
RC_1 = 8
RC_2 = 5
RC_3 = 6
RC_4 = 3
RC_5 = 4
RC_6 = 1
RC_7 = 2

UPPER_ANGLE_RANGE = [105, 255] #90+15, 90+165
LOWER_ANGLE_RANGE = [70, 290]

mx = Mx64('COM5')
kinematic = Kinematic()

class Pug:
    def __init__(self):
        
        #-------ID---------
        self.legID =[   (RC_0, RC_1), #leg0
                        (RC_2, RC_3), #leg1
                        (RC_4, RC_5), #leg2
                        (RC_6, RC_7)] #leg3

        #-------XYZ value-----
        self.legPoint = [   (0,0,0), # x-y-z
                            (0,0,0),
                            (0,0,0),
                            (0,0,0)]
        
    def setup(self):
        #------doi chieu dong co---------
        mx.setDriveMode(RC_1, True)
        mx.setDriveMode(RC_3, False)
        mx.setDriveMode(RC_5, False)
        mx.setDriveMode(RC_7, False)
        
    def standing(self):
        mx.setNTorqueEnable(self.legID, [[1,1],[1,1],[1,1],[1,1]])
        P0 = (-45, 260, 0)
        rad1, rad2, rad3 = kinematic.legIK(P0)

        angle1, angle2, angle3 = (abs(degrees(rad1)), 180 - abs(degrees(rad2)), 180 - abs(degrees(rad3)))
        arrAngle = [[angle2, angle3],
                    [angle2, angle3],
                    [angle2, angle3],
                    [angle2, angle3]]
        
        print(degrees(rad1),degrees(rad2), degrees(rad3))
        # mx.setNGoalAngle(self.legID, arrAngle)
        # mx.setGoalAngle()
        # mx.setNGoalAngle([self.legID[0]], [[angle2, angle3]])
        # mx.setGoalAngle(7, 250)

pug = Pug()
pug.setup()
pug.standing()

        