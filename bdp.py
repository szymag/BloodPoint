import Schedule
from collections import deque
from Distributions import Distributions

class BloodDonationPoint():

    def __init__(self):
        self.InitialPhase=40000
        self.SystemTime=0.0
        self.Schedule=Schedule.Schedule()
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
        self.Distributions=Distributions()
        self.BloodNumber=0
        # self.PatientNumber=0
        # self.DonorNumber=0

        self.EnlargmentNumber=0
        self.UnitOnScience=0

        self.EnVariable=0
        self.busyFlag=0

    def getBloodKey(self,time):
        return int(time.ExpirationDate)

    def AddBlood(self,blood):
        self.BloodList.append(blood)
        # self.BloodList.sort()
        self.BloodList=sorted(self.BloodList, key=self.getBloodKey) 
    
    def RemoveBlood(self):
        print("Usunieto jednostke krwi o ID: ", self.BloodList[0].ID)
        if(self.SystemTime > self.InitialPhase):
            self.BloodForScience+=1
        del(self.BloodList[0])
        self.BloodList=sorted(self.BloodList, key=self.getBloodKey) 
        
    def RemoveBloodScience(self):
        print("Usunieto SCIENCE jednostkwe krwi o ID: " + str(self.BloodList[0].ID))
        if(self.SystemTime > self.InitialPhase):
            self.BloodForScience+=1
        del(self.BloodList[0])
        self.BloodList=sorted(self.BloodList, key=self.getBloodKey)