from collections import deque
from Schedule import Schedule
from Distributions import Distributions


class BloodDonationPoint():

    def __init__(self):
        self.InitialPhase = 40000
        self.SystemTime = 0.0
        self.Schedule = Schedule()
        self.PatientQueue = deque()
        self.BloodListA = []
        self.BloodListB = []
        self.EnFlag = False
        self.TbLevel = 30
        self.TuTime = 300
        self.N = 15
        self.MinimalBlood = 70
        self.Q = 11
        self.UtilizedBlood = 0
        self.BloodForScience = 0
        self.Distributions = Distributions()

        self.ReturnedBloodA = 0
        self.ReturnedBloodB = 0

        self.UnitOnScience = 0

        self.EnVariable = 0
        self.busyFlag = 0

    def getBloodKey(self, time):
        return int(time.ExpirationDate)

    def AddBlood(self, blood):
        if(blood.BloodType == "A"):
            self.BloodListA.append(blood)
            self.BloodListA = sorted(self.BloodListA, key=self.getBloodKey)
        else:
            self.BloodListB.append(blood)
            self.BloodListB = sorted(self.BloodListB, key=self.getBloodKey)

    def RemoveBlood(self, BloodType):
        if(BloodType == "A"):
            print("Usunieto jednostke krwi grupy A o ID: ",
                  self.BloodListA[0].ID)
            if(self.SystemTime > self.InitialPhase):
                self.UtilizedBlood += 1
            del(self.BloodListA[0])
            self.BloodListA = sorted(self.BloodListA, key=self.getBloodKey)
        else:
            print("Usunieto jednostke krwi grupy B o ID: ",
                  self.BloodListB[0].ID)
            if(self.SystemTime > self.InitialPhase):
                self.UtilizedBlood += 1
            del(self.BloodListB[0])
            self.BloodListB = sorted(self.BloodListB, key=self.getBloodKey)

    def RemoveBloodScience(self):
        print("Usunieto SCIENCE jednostkwe krwi o ID: " +
              str(self.BloodList[0]._BloodId))
        if(self.SystemTime > self.InitialPhase):
            self.BloodForScience += 1
        del(self.BloodList[0])
        self.BloodList = sorted(self.BloodList, key=self.getBloodKey)
