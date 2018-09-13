from Process import Process
from Generators import Generators
from UnitOfBlood import UnitOfBlood


class Blood(Process):

    counter_standard_order = 0
    active = False

    def __init__(self, system, blood_type):
        super().__init__(system)
        self.time = 800
        self.blood_type_order = blood_type

    def execute(self):
        self.active = True
        while(self.active):

            if(self.phase == 0):
                self.phase0()
            elif(self.phase == 1):
                self.phase1()

    def phase0(self):
        self.activate(Generators().get_exponential(1700))
        self.phase = 1
        self.active = 0
        print("Zamowiono krew grupy " +
              self.blood_type_order + " metoda standardowa.")
        if(self.bdp.system_time > self.bdp.initial_phase):
            Blood.counter_standard_order += 1

    def phase1(self):
        for _i in range(self.bdp.N):
            self.bdp.add_blood(UnitOfBlood(
                self.bdp, self.bdp.system_time + self.time, self.blood_type_order, "Standard"))
            print("Zamawiam krew grupy " +
                  self.blood_type_order + " w trybie standardowym.")
        self.active = False
        print("Dostarczono standardowe zamowinie na krew grupy " +
              self.blood_type_order + ".")

    def ToString(self):
        return("Standardowe zamowienie | czas: " + str(self.proces_event.event_time))
