import numpy as np
from math import *

# def _solve_triangle(a, b, c):
#     a,b,c = abs(a), abs(b), abs(c)
#     if a + b < c or a + c < b or b + c < a:
#         raise ValueError("Error triangle")
#     cos = float(a**2 + b**2 - c**2)/(2*a*b)
#     return acos(cos)

# def _length(a,b):
#     return sqrt(a**2 + b**2)

class Kinematic:
    def __init__(self):
        self.l1 = 0 #coxa
        self.l2 = 165 #femur
        self.l3 = 180 #tibia
        
        self.hip_offset = 0
        self.L = 140 
        self.W = 75

    def bodyIK(self,omega,phi,psi,xm,ym,zm):
        Rx = np.array([[1,0,0,0],
                    [0,np.cos(omega),-np.sin(omega),0],
                    [0,np.sin(omega),np.cos(omega),0],[0,0,0,1]])
        Ry = np.array([[np.cos(phi),0,np.sin(phi),0],
                    [0,1,0,0],
                    [-np.sin(phi),0,np.cos(phi),0],[0,0,0,1]])
        Rz = np.array([[np.cos(psi),-np.sin(psi),0,0],
                    [np.sin(psi),np.cos(psi),0,0],[0,0,1,0],[0,0,0,1]])
        Rxyz = Rx.dot(Ry.dot(Rz))

        T = np.array([[0,0,0,xm],[0,0,0,ym],[0,0,0,zm],[0,0,0,0]])
        Tm = T+Rxyz

        sHp=np.sin(pi/2)
        cHp=np.cos(pi/2)
        (L,W)=(self.L,self.W)

        return([Tm.dot(np.array([[cHp,0,sHp,L/2],[0,1,0,0],[-sHp,0,cHp,W/2],[0,0,0,1]])),
                Tm.dot(np.array([[cHp,0,sHp,L/2],[0,1,0,0],[-sHp,0,cHp,-W/2],[0,0,0,1]])),
                Tm.dot(np.array([[cHp,0,sHp,-L/2],[0,1,0,0],[-sHp,0,cHp,W/2],[0,0,0,1]])),
                Tm.dot(np.array([[cHp,0,sHp,-L/2],[0,1,0,0],[-sHp,0,cHp,-W/2],[0,0,0,1]]))])

    # def legIK(self,point): #inverse kinematic
    #     (x,y,z)=(point[0],point[1],point[2])
    #     (l1,l2,l3,l4)=(self.l1,self.l2,self.l3,self.l4)
    #     try:        
    #         F=sqrt(x**2+y**2-l1**2)
    #     except ValueError:
    #         print("Error in legIK with x {} y {} and l1 {}".format(x,y,l1))
    #         F=l1
    #     G=F-l2
    #     H=sqrt(G**2+z**2)
    #     theta1=-atan2(y,x)-atan2(F,-l1)
        
    #     D=(H**2-l3**2-l4**2)/(2*l3*l4)
    #     try:        
    #         theta3=acos(D) 
    #     except ValueError:
    #         print("Error in legIK with x {} y {} and D {}".format(x,y,D))
    #         theta3=0
    #     theta2=atan2(z,G)-atan2(l4*sin(theta3),l3+l4*cos(theta3))
        
    #     return (theta1,theta2,theta3)

    # def legIK(self, point):
    #     (x,y,z) = point
    #     (l1,l2,l3) = (self.l1,self.l2,self.l3)
    #     #Distance between the Coxa and Ground Contact 
    #     XZ = sqrt(x**2 + z**2)
    #     W = sqrt(XZ**2 + y**2)
    #     D1 = atan2(XZ - l1, y)
    #     D2 = acos(((l2**2 - l3**2) + W**2) / (2*l2*W))
    #     rad1 = atan2(z, x)
    #     rad2 = -(D1 + D2)
    #     rad3 = acos((l2**2+l3**2-W**2)/(2*l2*l3))

    #     theta1 = degrees(rad1)
    #     theta2 = degrees(rad2)
    #     theta3 = - (90 - degrees(rad3))

    #     return (theta1, theta2, theta3)
    
    # def legIK(self, point):
    #     (x,y,z) = point
    #     (coxa, femur, tibia) = (self.l1, self.l2, self.l3)
    #     f = _length(x,y) - coxa
    #     d = min(femur + tibia, _length(f, z))
    #     hip = atan2(z,y)
    #     knee = _solve_triangle(femur, d, tibia) - atan2(-z, f)
    #     ankle = _solve_triangle(femur, tibia, d)
    #     knee = -degrees(knee)
    #     ankle = degrees(ankle) - 90
    #     hip = degrees(hip) + self.hip_offset
    #     return (hip, knee, ankle)

    def legIK3dof(self, point):
        # Calculate hip angle (gamma)
        x,y,z = point
        coxa, femur, tibia = self.l1, self.l2, self.l3
        c = atan2(abs(x),z)
        d = sqrt(x**2 + z**2) - coxa
        D = sqrt(y**2 + d**2)
        b = acos((tibia**2 + femur**2 - D**2)/ (2*tibia*femur))
        #calculate kee angle
        a0 = atan2((sqrt(x**2 + z**2)-coxa), abs(y))
        a1 = acos((femur**2 + D**2 - tibia**2)/ (2*femur*D))

        _hip = degrees(c)
        _knee = 180 - degrees(a0) - degrees(a1)
        _ankle = 180 - degrees(b)

        return _hip, _knee, _ankle

    def legIK2dof(self, point):
        x,y,z = point
        x = -x
        L1,L2,L3 = self.l1,self.l2,self.l3
        K = sqrt(x**2 + y**2)
        if K > L2 + L3:
            K = L2 + L3
        A1 = acos((L2**2 + L3**2 - K**2)/(2*L2*L3))
        A2 = acos((K**2 + L2**2 - L3**2)/(2*K*L2))
        A3 = asin(x/K)
        A4 = (pi/2) - (A2 + A3)

        return 90+degrees(A4), 360-degrees(A1)
    # def legFK(self,angles): #forward kinematic
    #     (l1,l2,l3,l4)=(self.l1,self.l2,self.l3,self.l4)
    #     (theta1,theta2,theta3)=angles
    #     theta23=theta2+theta3

    #     T0=np.array([0,0,0,1])
    #     T1=T0+np.array([-l1*cos(theta1),l1*sin(theta1),0,0])
    #     T2=T1+np.array([-l2*sin(theta1),-l2*cos(theta1),0,0])
    #     T3=T2+np.array([-l3*sin(theta1)*cos(theta2),-l3*cos(theta1)*cos(theta2),l3*sin(theta2),0])
    #     T4=T3+np.array([-l4*sin(theta1)*cos(theta23),-l4*cos(theta1)*cos(theta23),l4*sin(theta23),0])
        
    #     return np.array([T0,T1,T2,T3,T4])

    # def calcIK(self,Lp,angles,center):
    #     (omega,phi,psi)=angles
    #     (xm,ym,zm)=center
        
    #     (Tlf,Trf,Tlb,Trb)= self.bodyIK(omega,phi,psi,xm,ym,zm)

    #     Ix=np.array([[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    #     return np.array([self.legIK(np.linalg.inv(Tlf).dot(Lp[0])),
    #     self.legIK(Ix.dot(np.linalg.inv(Trf).dot(Lp[1]))),
    #     self.legIK(np.linalg.inv(Tlb).dot(Lp[2])),
    #     self.legIK(Ix.dot(np.linalg.inv(Trb).dot(Lp[3])))])
