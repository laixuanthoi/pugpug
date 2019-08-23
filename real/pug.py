from mx64 import Mx64
from kinematic import Kinematic
from math import *
from time import *

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
    
    def doichieudongco(self, z):
        mx.setNTorqueEnable(self.legID, [[0,0],[0,0],[0,0],[0,0]])
        mx.setDriveMode(RC_1, z)
        mx.setDriveMode(RC_3, z)
        mx.setDriveMode(RC_5, z)
        mx.setDriveMode(RC_7, z)
        mx.setDriveMode(RC_0, not z)
        mx.setDriveMode(RC_2, not z)
        mx.setDriveMode(RC_4, not z)
        mx.setDriveMode(RC_6, not z)
        mx.setNTorqueEnable(self.legID, [[1,1],[1,1],[1,1],[1,1]])

    def setup(self):
        #------doi chieu dong co---------
        self.doichieudongco(False)
        
    def standing(self):
        mx.setNTorqueEnable(self.legID, [[1,1],[1,1],[1,1],[1,1]])
        P0 = (0, 220, 0)
        theta2, theta3 = kinematic.legIK2dof(P0)
        arrAngle = [   [theta2, theta3],
            [theta2, theta3],
            [theta2, theta3],
            [theta2, theta3]]
        mx.setNGoalAngle(self.legID, arrAngle)
        # mx.setGoalAngle(self.legID[1][0], theta2)
        # mx.setGoalAngle(self.legID[1][1], theta3)
    
    def trotting(self):
        mx.setNTorqueEnable(self.legID, [[1,1],[1,1],[1,1],[1,1]])
        from control.trotting import Trotting
        tt = Trotting()
        rTime = time()*1000
        while time()*1000 - rTime < 3000:
            diff = time()*1000 - rTime
            dt1 = diff % tt.sumT
            dt2 = (diff - (tt.t1 + tt.t2)) % tt.sumT
            
            arrAngle = [    kinematic.legIK2dof(tt.calLegs(dt1)),
            kinematic.legIK2dof(tt.calLegs(dt2)),
            kinematic.legIK2dof(tt.calLegs(dt1)),
            kinematic.legIK2dof(tt.calLegs(dt2))]
            mx.setNGoalAngle(self.legID, arrAngle)
            sleep(0.001)
            

pug = Pug()
# pug.setup()
# pug.standing()

pug.trotting()

        