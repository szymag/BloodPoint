from Process import Process
from EmergencyBlood import EmergencyBlood
from Blood import Blood


class Patient(Process):
    patient_counter = 0
    _PatientA = 0
    _PatientB = 0

    def __init__(self, bdp):
        super().__init__(bdp)
        self.name = "Pacjet"
        self.BrithTime = self.bdp.system_time
        self.BloodType = self.bdp.Distributions.GetBloodType()
        if(self.BloodType == "A"):
            Patient._PatientA += 1
        else:
            Patient._PatientB += 1
        self.BloodNeeded = self.bdp.Distributions.GetGeometric()
        if(self.BloodNeeded == 0):
            self.BloodNeeded = 1
        self.ID = Patient.patient_counter
        print("Do bazy dodano nowego pacjenta numer " +
              str(self.ID) + " o grupie krwi: " + str(self.BloodType))
        if(self.bdp.system_time > self.bdp.initial_phase):
            Patient.patient_counter += 1

    def execute()(self):
        self.active = True
        while(self.active):

            if(self.Phase == 0):
                self.Phase0()
            elif(self.Phase == 1):
                self.Phase1()
            elif(self.Phase == 2):
                self.Phase2()
            elif(self.Phase == 3):
                self.Phase3()
            elif(self.Phase == 4):
                self.Phase4()

    def Phase0(self):
        Patient(self.bdp).activate(
            self.bdp.Distributions.get_exponential(250))
        self.bdp.patient_queue.append(self)
        print("dodatno do kolejki pacjenta ", self.ID)
        self.Phase = 1
        self.active = False

    def Phase1(self):
        if(len(self.bdp.BloodListA) != 0):
            # USUWANIE PRZETERMINOWANEJ KRWI Beg
            while(self.bdp.BloodListA[0].ExpirationDate < self.bdp.system_time):
                self.bdp.RemoveBlood("A")
                if(len(self.bdp.BloodListA) == 0):
                    break
            deletelist = []
            for blood in self.bdp.BloodListA:
                # a=self.bdp.Distributions.GetBLoodReturnTime()
                if(blood.OrderType == "Emergency"):
                    a = blood.BloodTime
                    b = (self.bdp.Distributions.GetBLoodReturnTime())
                    if(a+b <= + self.bdp.system_time):
                        deletelist.append(blood)
                        print("Zwrocono krew grupy " + blood.BloodType +
                              " z zamowienia awaryjnego o ID:" + str(blood.ID))
                        self.bdp.ReturnedBloodA += 1
            for blood in deletelist:
                self.bdp.BloodListA.remove(blood)
                # del(self.bdp.BloodListA[blood_i])

        if(len(self.bdp.BloodListB) != 0):
            while(self.bdp.BloodListB[0].ExpirationDate < self.bdp.system_time):
                self.bdp.RemoveBlood("B")
                if(len(self.bdp.BloodListB) == 0):
                    break
            deletelist = []
            for blood in self.bdp.BloodListB:
                    # a=self.bdp.Distributions.GetBLoodReturnTime()
                if(blood.OrderType == "Emergency"):
                    a = blood.BloodTime
                    b = (self.bdp.Distributions.GetBLoodReturnTime())
                    if(a+b <= + self.bdp.system_time):
                        deletelist.append(blood)
                        print("Zwrocono krew grupy " + blood.BloodType +
                              " z zamowienia awaryjnego o ID:" + str(blood.ID))
                        self.bdp.ReturnedBloodB += 1
            for blood in deletelist:
                self.bdp.BloodListB.remove(blood)
            # USUWANIE PRZETERMINOWANEJ KRWI End

        if(len(self.bdp.BloodListA) < self.bdp.MinimalBlood):
            temp_run = Blood(self.bdp, "A")
            temp_run.activate(0.0)
            pass

        if(len(self.bdp.BloodListB) < self.bdp.MinimalBlood):
            temp_run = Blood(self.bdp, "B")
            temp_run.activate(0.0)
            pass

        self.Phase = 2

    def Phase2(self):
        if(self.BloodType == "A" and len(self.bdp.BloodListA) < self.BloodNeeded):
            temp_run = EmergencyBlood(self, self.bdp, self.BloodType)
            temp_run.activate(0.0)
            self.active = False
            print("Zamowiono awaryjnie krew grupy A dla pacjenta o nr ID: " + str(self.ID) +
                  ". Potrzebna liczba jednostek krwi:" + str(self.BloodNeeded) + " | Czas: " + str(self.bdp.system_time))

        if(self.BloodType == "B" and len(self.bdp.BloodListB) < self.BloodNeeded):
            temp_run = EmergencyBlood(self, self.bdp, self.BloodType)
            temp_run.activate(0.0)
            self.active = False
            print("Zamowiono awaryjnie krew grupy B dla pacjenta o nr ID: " + str(self.ID) +
                  ". Potrzebna liczba jednostek krwi: " + str(self.BloodNeeded) + " | Czas: " + str(self.bdp.system_time))

        self.Phase = 3

    def Phase3(self):
        if(self.BloodType == "A" and self.BloodNeeded < len(self.bdp.BloodListA)):
            print("Pacjent od nr ID" + str(self.ID) + "otrzymal " +
                  str(self.BloodNeeded) + " jednostek grupy typu A")
            for _i in range(self.BloodNeeded):
                del(self.bdp.BloodListA[0])
            print("Pacjent o nr ID " + str(self.ID) + " wyszedl.")
            self.bdp.busy_flag = 0
            self.active = False
            self.Phase = 4

        elif(self.BloodType == "B" and self.BloodNeeded < len(self.bdp.BloodListB)):
            print("Pacjent od nr ID" + str(self.ID) + "otrzymal " +
                  str(self.BloodNeeded) + " jednostek krwi typu B")
            for _i in range(self.BloodNeeded):
                del(self.bdp.BloodListB[0])
            print("Pacjent o nr ID " + str(self.ID) + " wyszedl.")
            self.bdp.busy_flag = 0
            self.active = False
            self.Phase = 4

        else:
            temp_run = EmergencyBlood(self, self.bdp, self.BloodType)
            temp_run.activate(0.0)
            self.active = False
            print("Zamowiono awaryjnie krew grupy" + self.BloodType + "dla Pacjenta o nr ID" + str(self.ID) +
                  " | Potrzeba " + str(self.BloodNeeded) + " jednostek krwi. | Czas zdarzenia : " + str(self.bdp.system_time))

    def Phase4(self):
        self.bdp.busy_flag = False
        if(len(self.bdp.patient_queue) != 0):
            self.active = True
        else:
            self.active = False

    def ToString(self):
        return("Pacjent od nr ID : " + str(self.ID) + " | czas: " + str(self.proces_event.event_time))


