<<<<<<< HEAD
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Sche dule
from collections import deque


class BloodDonationPoint:

    def __init__(self):
        self.InitalPhase=400000
        self.SystemTime=0.0
        self.Schedule=Schedule.Schedule()
=======
from Schedule import Schedule
from collections import deque

class BloodDonationPoint():

    def __init__(self):
        self.InitialPhase=40000
        self.SystemTime=0.0
        self.Schedule=Schedule()
>>>>>>> origin/master
        self.PatientQueue = deque()
        self.BloodList = []
        self.EnFlag=False
        self.TbLevel=30
        self.TuTime=300
        self.N=15
        self.MinimalBlood=70
        self.Q=11
        self.UtilizedBlood=0
        self.BloodForScience=0

<<<<<<< HEAD
=======

        self.EnVariable=0
        self.busyFlag=0

    def getBloodKey(self,time):
        return int(time.ExpirationDate)

    def AddBlood(self,blood):
        self.BloodList.append(blood)
        # self.BloodList.sort()
        sorted(self.BloodList, key=self.getBloodKey) 
    
    def RemoveBlood(self):
        print("Usunieto jednostke krwi o ID: ", self.BloodList[0].ID)
        if(self.SystemTime > self.InitialPhase):
            self.BloodForScience+=1
        self.BloodList.pop()
        sorted(self.BloodList, key=self.getBloodKey) 

    def RemoteBloodScience(self):
        print("Usunieteo jednostkwe krwi o ID: " + str(self.BloodList.pop().ID))
        if(self.SystemTime > self.InitialPhase):
            self.BloodForScience++
        del(self.BloodList[0])
        sorted(self.BloodList, key=self.getBloodKey)
>>>>>>> origin/master
