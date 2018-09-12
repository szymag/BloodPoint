from Process import Process
from Distributions import Distributions
from BloodUnit import BloodUnit

class EmergencyBlood(Process):
    
    _AmoutOfemergency=0

    def __init__(self,orderedPatient,system,BloodType):
        super().__init__(system)
        self.OrderedPatient=orderedPatient
        self.BloodTypeOrder=BloodType
        self.Time=800
        self._active=0

    def Execute(self):
        self._active=True
        while(self._active):
            
            if(self.Phase==0):
                self.Phase0()
            elif(self.Phase==1):
                self.Phase1()

    def Phase0(self):
        self.Activate(Distributions().GetNormal())
        self.Phase=1
        self._active=0
        print("Zamówiono krew awaryjnie")
        if(self.BDPoint.SystemTime > self.BDPoint.InitialPhase):
            EmergencyBlood._AmoutOfemergency+=1
        
    def Phase1(self):
        for i in range(self.BDPoint.Q):
            self.BDPoint.AddBlood(BloodUnit(self.BDPoint,self.BDPoint.SystemTime + self.Time,self.BloodTypeOrder))
        temp_run=self.OrderedPatient
        temp_run.Activate(0.0)
        self._active=0

        print("Dojechalo zamowienie awaryjne dla pacjenta nr " + str(self.OrderedPatient.ID) + ".")

    def ToString(self):
        return("Awaryjne zamowienie dla pacjetna o ID: " +str(self.OrderedPatient.ID) + "| czas: " + str(self.ProcessEvent.EventTime))

