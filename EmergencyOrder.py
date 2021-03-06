from Process import Process
from Generators import Generators
from UnitOfBlood import UnitOfBlood


class EmergencyOrder(Process):

    counter_emergency = 0

    def __init__(self, ordering_patient, bdp, blood_type):
        super().__init__(bdp)
        self.ordering_patient = ordering_patient
        self.blood_type_order = blood_type
        self.time = 800
        self.active = 0

    def execute(self):
        self.active = True
        while(self.active):

            if(self.phase == 0):
                self.phase0()
            elif(self.phase == 1):
                self.phase1()

    def phase0(self):
        self.activate(Generators().get_normal())
        self.phase = 1
        self.active = 0
        print("Zamowiono krew awaryjnie!")
        if(self.bdp.system_time > self.bdp.initial_phase):
            EmergencyOrder.counter_emergency += 1

    def phase1(self):
        for _i in range(self.bdp.q):
            self.bdp.add_blood(UnitOfBlood(
                self.bdp, self.bdp.system_time + self.time, self.blood_type_order, "Emergency"))
        self.ordering_patient.activate(0.0)
        self.active = 0

        print("Dojechalo zamowienie awaryjne dla pacjenta nr " +
              str(self.ordering_patient.id) + "!")

    def get_process_info(self):
        return("Uwaga! Awaryjne zamowienie dla pacjetna o ID: " + str(self.ordering_patient.id) + "! Czas systemu: " + str(self.proces_event.event_time))
