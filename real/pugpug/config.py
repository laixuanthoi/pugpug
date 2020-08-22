import numpy as np 

class ServoParams:
    def __init__(self):
        self.pins = [
            [1,5,9],
            [2,6,10],
            [3,7,11],
            [4,8,12],
        ]

        self.directions = [[0,0,0] * 4]

        self.rangePWMs = [
            [2000, 3000],
            [2000, 3000],
            [2000, 3000],
            [2000, 3000],
        ]

        self.rangeAngles = [
            [0, 100],
            [0, 100],
            [0, 100],
            [0, 100],
        ]

class KinematicParams:
    def __init__(self):
        self.body_length = 20
        self.body_width  = 60 #width body of the dog
        self.leg_length_1 = 10
        self.leg_length_2 = 10
        self.leg_length_3 = 10

