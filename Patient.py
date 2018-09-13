from Process import Process
from EmergencyBlood import EmergencyBlood
from Blood import Blood


class Patient(Process):
    counter_patient = 0
    counter_patient_a = 0
    counter_patient_b = 0

    def __init__(self, bdp):
        super().__init__(bdp)
        self.name = "Pacjet"
        # self.Brithtime = self.bdp.system_time
        self.blood_type = self.bdp.Generators.get_blood_type()
        if(self.blood_type == "A"):
            Patient.counter_patient_a += 1
        else:
            Patient.counter_patient_b += 1
        self.blood_needed = self.bdp.Generators.get_geometric()
        if(self.blood_needed == 0):
            self.blood_needed = 1
        self.id = Patient.counter_patient
        print("Do bazy dodano nowego pacjenta numer " +
              str(self.id) + " o grupie krwi: " + str(self.blood_type))
        if(self.bdp.system_time > self.bdp.initial_phase):
            Patient.counter_patient += 1

    def execute(self):
        self.active = True
        while(self.active):

            if(self.phase == 0):
                self.phase0()
            elif(self.phase == 1):
                self.phase1()
            elif(self.phase == 2):
                self.phase2()
            elif(self.phase == 3):
                self.phase3()
            elif(self.phase == 4):
                self.phase4()

    def phase0(self):
        Patient(self.bdp).activate(
            self.bdp.Generators.get_exponential(250))
        self.bdp.patient_queue.append(self)
        print("dodatno do kolejki pacjenta ", self.id)
        self.phase = 1
        self.active = False

    def phase1(self):
        if(len(self.bdp.blood_list_a) != 0):
            # USUWANIE PRZETERMINOWANEJ KRWI Beg
            while(self.bdp.blood_list_a[0].expiration_date < self.bdp.system_time):
                self.bdp.remove_blood("A")
                if(len(self.bdp.blood_list_a) == 0):
                    break
            deletelist = []
            for blood in self.bdp.blood_list_a:
                # a=self.bdp.Generators.get_blood_returning_time()
                if(blood.order_type == "Emergency"):
                    a = blood.blood_time
                    b = (self.bdp.Generators.get_blood_returning_time())
                    if(a+b <= + self.bdp.system_time):
                        deletelist.append(blood)
                        print("Zwrocono krew grupy " + blood.blood_type +
                              " z zamowienia awaryjnego o ID:" + str(blood.id))
                        self.bdp.returned_blood_A += 1
            for blood in deletelist:
                self.bdp.blood_list_a.remove(blood)
                # del(self.bdp.blood_list_a[blood_i])

        if(len(self.bdp.blood_list_b) != 0):
            while(self.bdp.blood_list_b[0].expiration_date < self.bdp.system_time):
                self.bdp.remove_blood("B")
                if(len(self.bdp.blood_list_b) == 0):
                    break
            deletelist = []
            for blood in self.bdp.blood_list_b:
                    # a=self.bdp.Generators.get_blood_returning_time()
                if(blood.order_type == "Emergency"):
                    a = blood.blood_time
                    b = (self.bdp.Generators.get_blood_returning_time())
                    if(a+b <= + self.bdp.system_time):
                        deletelist.append(blood)
                        print("Zwrocono krew grupy " + blood.blood_type +
                              " z zamowienia awaryjnego o ID:" + str(blood.id))
                        self.bdp.returned_blood_B += 1
            for blood in deletelist:
                self.bdp.blood_list_b.remove(blood)
            # USUWANIE PRZETERMINOWANEJ KRWI End

        if(len(self.bdp.blood_list_a) < self.bdp.MinimalBlood):
            Blood(self.bdp, "A").activate(0.0)
            pass

        if(len(self.bdp.blood_list_b) < self.bdp.MinimalBlood):
            Blood(self.bdp, "B").activate(0.0)
            pass

        self.phase = 2

    def phase2(self):
        if(self.blood_type == "A" and len(self.bdp.blood_list_a) < self.blood_needed):
            EmergencyBlood(self, self.bdp, self.blood_type).activate(0.0)
            self.active = False
            print("Zamowiono awaryjnie krew grupy A dla pacjenta o nr ID: " + str(self.id) +
                  ". Potrzebna liczba jednostek krwi:" + str(self.blood_needed) + " | Czas: " + str(self.bdp.system_time))

        if(self.blood_type == "B" and len(self.bdp.blood_list_b) < self.blood_needed):
            EmergencyBlood(self, self.bdp, self.blood_type).activate(0.0)
            self.active = False
            print("Zamowiono awaryjnie krew grupy B dla pacjenta o nr ID: " + str(self.id) +
                  ". Potrzebna liczba jednostek krwi: " + str(self.blood_needed) + " | Czas: " + str(self.bdp.system_time))

        self.phase = 3

    def phase3(self):
        if(self.blood_type == "A" and self.blood_needed < len(self.bdp.blood_list_a)):
            print("Pacjent od nr ID" + str(self.id) + "otrzymal " +
                  str(self.blood_needed) + " jednostek grupy typu A")
            for _i in range(self.blood_needed):
                del(self.bdp.blood_list_a[0])
            print("Pacjent o nr ID " + str(self.id) + " wyszedl.")
            self.bdp.busy_flag = 0
            self.active = False
            self.phase = 4

        elif(self.blood_type == "B" and self.blood_needed < len(self.bdp.blood_list_b)):
            print("Pacjent od nr ID" + str(self.id) + "otrzymal " +
                  str(self.blood_needed) + " jednostek krwi typu B")
            for _i in range(self.blood_needed):
                del(self.bdp.blood_list_b[0])
            print("Pacjent o nr ID " + str(self.id) + " wyszedl.")
            self.bdp.busy_flag = 0
            self.active = False
            self.phase = 4

        else:
            temp_run = EmergencyBlood(self, self.bdp, self.blood_type)
            temp_run.activate(0.0)
            self.active = False
            print("Zamowiono awaryjnie krew grupy" + self.blood_type + "dla Pacjenta o nr ID" + str(self.id) +
                  " | Potrzeba " + str(self.blood_needed) + " jednostek krwi. | Czas zdarzenia : " + str(self.bdp.system_time))

    def phase4(self):
        self.bdp.busy_flag = False
        if(len(self.bdp.patient_queue) != 0):
            self.active = True
        else:
            self.active = False

    def ToString(self):
        return("Pacjent od nr ID : " + str(self.id) + " | czas: " + str(self.proces_event.event_time))
