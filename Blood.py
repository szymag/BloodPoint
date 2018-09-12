from Process import Process
from Distributions import Distributions
from BloodUnit import BloodUnit

class Blood(Process):

    _AmountOfStandardOrders=0
    # Time=0
    _active=False
    def __init__(self, system):
        super().__init__(system)        
        self.Time=800
    
    def Execute(self):
        # self._active=True
        self._active=True
        while(self._active):
            
            if(self.Phase==0):
                self.Phase0()
            elif(self.Phase==1):
                self.Phase1()

    def Phase0(self):
        self.Activate(Distributions().GetExponential(1700))
        self.Phase=1
        self._active=0
        print("Zamowiono krew standardowo.")
        if(self.BDPoint.SystemTime > self.BDPoint.InitialPhase):
            Blood._AmountOfStandardOrders+=1
        
    def Phase1(self):
        for i in range(self.BDPoint.N):
            self.BDPoint.AddBlood(BloodUnit(self.BDPoint.SystemTime + self.Time))
        self._active=False
        print("Dostarczono standardowe zamowinie)")

    def ToString(self):
        return("Standardowe zamowienie | czas: " + str(self.ProcessEvent.EventTime))