import numpy as np 

class Trotting:
    def __init__(self):
        self.t0 = 30
        self.t1 = 45
        self.t2 = 15
        self.t3 = 30
        self.P0 = (-25, 250, 0)

        self.Sl = 160 #step length
        self.Sh = 80 #step height
        self.Sw = 0 #step width
    
    def calLegs(self, t):
        P1 = (self.P0[0] - self.Sl/2,    self.P0[1],     0)
        P2 = (P1[0] + self.Sl,           P1[1] - self.Sh,     0)
        P3 = (P2[0],                P2[1] + self.Sh,     0)
        if t < self.t0:#P0 -> P1 for t0
            tp = 1/(self.t0/t)
            return (self.P0[0] - (self.Sl/2)*tp, self.P0[1], 0)

        elif t < self.t0 + self.t1:#P1->P2 for t1
            td = t - self.t0
            tp = 1/(self.t1/td)
            return (P1[0] + self.Sl*tp, P1[1] - self.Sh * tp, 0)

        elif t < self.t0 + self.t1 + self.t2:#P2->P3 for t2
            td = t - (self.t0 + self.t1)
            tp = 1/(self.t2/td)
            return (P2[0], P2[1] + self.Sh * tp)
            
        elif t < self.t0 + self.t1 + self.t2 + self.t3:#P3 ->P0 for t3
            td = t - (self.t0 + self.t1 + self.t2 + self.t3)
            tp = 1/(self.t3/td)
            return (P3[0] - self.Sl/2*tp, P3[1], 0)


    
