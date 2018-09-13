from Process import Process
from EmergencyBlood import EmergencyBlood
from Blood import Blood


class Patient(Process):
    _PatientCounter = 0
    _PatientA = 0
    _PatientB = 0

    def __init__(self, system):
        super().__init__(system)
        self.name = "Pacjet"
        self.BrithTime = self.BDPoint.SystemTime
        self.BloodType = self.BDPoint.Distributions.GetBloodType()
        if(self.BloodType == "A"):
            Patient._PatientA += 1
        else:
            Patient._PatientB += 1
        self.BloodNeeded = self.BDPoint.Distributions.GetGeometric()
        if(self.BloodNeeded == 0):
            self.BloodNeeded = 1
        self.ID = Patient._PatientCounter
        print("Do bazy dodano nowego pacjenta numer " +
              str(self.ID) + " o grupie krwi: " + str(self.BloodType))
        if(self.BDPoint.SystemTime > self.BDPoint.InitialPhase):
            Patient._PatientCounter += 1

    def Execute(self):
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
        Patient(self.BDPoint).Activate(
            self.BDPoint.Distributions.GetExponential(250))
        self.BDPoint.PatientQueue.append(self)
        print("dodatno do kolejki pacjenta ", self.ID)
        self.Phase = 1
        self.active = False

    def Phase1(self):
        if(len(self.BDPoint.BloodListA) != 0):
            # USUWANIE PRZETERMINOWANEJ KRWI Beg
            while(self.BDPoint.BloodListA[0].ExpirationDate < self.BDPoint.SystemTime):
                self.BDPoint.RemoveBlood("A")
                if(len(self.BDPoint.BloodListA) == 0):
                    break
            deletelist = []
            for blood in self.BDPoint.BloodListA:
                # a=self.BDPoint.Distributions.GetBLoodReturnTime()
                if(blood.OrderType == "Emergency"):
                    a = blood.BloodTime
                    b = (self.BDPoint.Distributions.GetBLoodReturnTime())
                    if(a+b <= + self.BDPoint.SystemTime):
                        deletelist.append(blood)
                        print("Zwrocono krew grupy " + blood.BloodType +
                              " z zamowienia awaryjnego o ID:" + str(blood.ID))
                        self.BDPoint.ReturnedBloodA += 1
            for blood in deletelist:
                self.BDPoint.BloodListA.remove(blood)
                # del(self.BDPoint.BloodListA[blood_i])

        if(len(self.BDPoint.BloodListB) != 0):
            while(self.BDPoint.BloodListB[0].ExpirationDate < self.BDPoint.SystemTime):
                self.BDPoint.RemoveBlood("B")
                if(len(self.BDPoint.BloodListB) == 0):
                    break
            deletelist = []
            for blood in self.BDPoint.BloodListB:
                    # a=self.BDPoint.Distributions.GetBLoodReturnTime()
                if(blood.OrderType == "Emergency"):
                    a = blood.BloodTime
                    b = (self.BDPoint.Distributions.GetBLoodReturnTime())
                    if(a+b <= + self.BDPoint.SystemTime):
                        deletelist.append(blood)
                        print("Zwrocono krew grupy " + blood.BloodType +
                              " z zamowienia awaryjnego o ID:" + str(blood.ID))
                        self.BDPoint.ReturnedBloodB += 1
            for blood in deletelist:
                self.BDPoint.BloodListB.remove(blood)
            # USUWANIE PRZETERMINOWANEJ KRWI End

        if(len(self.BDPoint.BloodListA) < self.BDPoint.MinimalBlood):
            temp_run = Blood(self.BDPoint, "A")
            temp_run.Activate(0.0)
            pass

        if(len(self.BDPoint.BloodListB) < self.BDPoint.MinimalBlood):
            temp_run = Blood(self.BDPoint, "B")
            temp_run.Activate(0.0)
            pass

        self.Phase = 2

    def Phase2(self):
        if(self.BloodType == "A" and len(self.BDPoint.BloodListA) < self.BloodNeeded):
            temp_run = EmergencyBlood(self, self.BDPoint, self.BloodType)
            temp_run.Activate(0.0)
            self.active = False
            print("Zamowiono awaryjnie krew grupy A dla pacjenta o nr ID: " + str(self.ID) +
                  ". Potrzebna liczba jednostek krwi:" + str(self.BloodNeeded) + " | Czas: " + str(self.BDPoint.SystemTime))

        if(self.BloodType == "B" and len(self.BDPoint.BloodListB) < self.BloodNeeded):
            temp_run = EmergencyBlood(self, self.BDPoint, self.BloodType)
            temp_run.Activate(0.0)
            self.active = False
            print("Zamowiono awaryjnie krew grupy B dla pacjenta o nr ID: " + str(self.ID) +
                  ". Potrzebna liczba jednostek krwi: " + str(self.BloodNeeded) + " | Czas: " + str(self.BDPoint.SystemTime))

        self.Phase = 3

    def Phase3(self):
        if(self.BloodType == "A" and self.BloodNeeded < len(self.BDPoint.BloodListA)):
            print("Pacjent od nr ID" + str(self.ID) + "otrzymal " +
                  str(self.BloodNeeded) + " jednostek grupy typu A")
            for i in range(self.BloodNeeded):
                del(self.BDPoint.BloodListA[0])
            print("Pacjent o nr ID " + str(self.ID) + " wyszedl.")
            self.BDPoint.busyFlag = 0
            self.active = False
            self.Phase = 4

        elif(self.BloodType == "B" and self.BloodNeeded < len(self.BDPoint.BloodListB)):
            print("Pacjent od nr ID" + str(self.ID) + "otrzymal " +
                  str(self.BloodNeeded) + " jednostek krwi typu B")
            for i in range(self.BloodNeeded):
                del(self.BDPoint.BloodListB[0])
            print("Pacjent o nr ID " + str(self.ID) + " wyszedl.")
            self.BDPoint.busyFlag = 0
            self.active = False
            self.Phase = 4

        else:
            temp_run = EmergencyBlood(self, self.BDPoint, self.BloodType)
            temp_run.Activate(0.0)
            self.active = False
            print("Zamowiono awaryjnie krew grupy" + self.BloodType + "dla Pacjenta o nr ID" + str(self.ID) +
                  " | Potrzeba " + str(self.BloodNeeded) + " jednostek krwi. | Czas zdarzenia : " + str(self.BDPoint.SystemTime))

    def Phase4(self):
        self.BDPoint.busyFlag = False
        if(len(self.BDPoint.PatientQueue) != 0):
            self.active = True
        else:
            self.active = False

    def ToString(self):
        return("Pacjent od nr ID : " + str(self.ID) + " | czas: " + str(self.ProcessEvent.EventTime))


# Pat=Patient()
