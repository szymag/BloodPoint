from collections import deque
from Schedule import Schedule
from Distributions import Distributions


class BloodDonationPoint():

    def __init__(self):
        self.initial_phase = 40000
        self.system_time = 0.0
        self.schedule = Schedule()
        self.patient_queue = deque()
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
        self.busy_flag = 0

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
            if(self.system_time > self.initial_phase):
                self.UtilizedBlood += 1
            del(self.BloodListA[0])
            self.BloodListA = sorted(self.BloodListA, key=self.getBloodKey)
        else:
            print("Usunieto jednostke krwi grupy B o ID: ",
                  self.BloodListB[0].ID)
            if(self.system_time > self.initial_phase):
                self.UtilizedBlood += 1
            del(self.BloodListB[0])
            self.BloodListB = sorted(self.BloodListB, key=self.getBloodKey)