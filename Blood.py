from Process import Process
from Distributions import Distributions
from BloodUnit import BloodUnit


class Blood(Process):

    _AmountOfStandardOrders = 0
    _active = False

    def __init__(self, system, BloodType):
        super().__init__(system)
        self.Time = 800
        self.BloodTypeOrder = BloodType

    def execute()(self):
        self._active = True
        while(self._active):

            if(self.Phase == 0):
                self.Phase0()
            elif(self.Phase == 1):
                self.Phase1()

    def Phase0(self):
        self.activate(Distributions().get_exponential(1700))
        self.Phase = 1
        self._active = 0
        print("Zamowiono krew grupy " +
              self.BloodTypeOrder + " metoda standardowa.")
        if(self.bdp.system_time > self.bdp.initial_phase):
            Blood._AmountOfStandardOrders += 1

    def Phase1(self):
        for i in range(self.bdp.N):
            self.bdp.AddBlood(BloodUnit(
                self.bdp, self.bdp.system_time + self.Time, self.BloodTypeOrder, "Standard"))
            print("Zamawiam Standardowo krew nr " + str(i))
        self._active = False
        print("Dostarczono standardowe zamowinie na krew grupy " +
              self.BloodTypeOrder)

    def ToString(self):
        return("Standardowe zamowienie | czas: " + str(self.proces_event.event_time))
