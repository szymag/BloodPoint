from collections import deque
from Schedule import Schedule
from Generators import Generators


class BloodDonationPoint():

    def __init__(self):
        self.initial_phase = 40000
        self.system_time = 0.0
        self.schedule = Schedule()
        self.patient_queue = deque()
        self.blood_list_a = []
        self.blood_list_b = []
        self.EnFlag = False
        self.TbLevel = 30
        self.Tutime = 300
        self.N = 15
        self.MinimalBlood = 70
        self.Q = 11
        self.UtilizedBlood = 0
        self.BloodForScience = 0
        self.Generators = Generators()

        self.returned_blood_A = 0
        self.returned_blood_B = 0

        self.UnitOnScience = 0

        self.EnVariable = 0
        self.busy_flag = 0

    def getBloodKey(self, time):
        return int(time.expiration_date)

    def add_blood(self, blood):
        if(blood.blood_type == "A"):
            self.blood_list_a.append(blood)
            self.blood_list_a = sorted(self.blood_list_a, key=self.getBloodKey)
        else:
            self.blood_list_b.append(blood)
            self.blood_list_b = sorted(self.blood_list_b, key=self.getBloodKey)

    def remove_blood(self, blood_type):
        if(blood_type == "A"):
            print("Usunieto jednostke krwi grupy A o id: ",
                  self.blood_list_a[0].id)
            if(self.system_time > self.initial_phase):
                self.UtilizedBlood += 1
            del(self.blood_list_a[0])
            self.blood_list_a = sorted(self.blood_list_a, key=self.getBloodKey)
        else:
            print("Usunieto jednostke krwi grupy B o id: ",
                  self.blood_list_b[0].id)
            if(self.system_time > self.initial_phase):
                self.UtilizedBlood += 1
            del(self.blood_list_b[0])
            self.blood_list_b = sorted(self.blood_list_b, key=self.getBloodKey)
