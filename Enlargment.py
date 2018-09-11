from Process import Process
from Distributions import Distributions

class Enlargment(Process):
    # _time=0
    # UnitsOnScience=0
    # IdEnlargment=0

    def __init__(self,system):
        super().__init__(system)
        # self.BDPoint=system 
        self.Activate(self.BDPoint.TuTime)
        self._time = self.BDPoint.SystemTime + self.BDPoint.TuTime
        self.UnitOnScience = Distributions().GetUniformToEnlagmnet()
        self.BDPoint.EnFlag = True

    def Execute(self):
        
        if(self.Phase==0):
            self.Phase0()
        elif(self.Phase==1):
            self.Phase1()
        

    def Phase0(self):
        if(len(self.BDPoint.BloodList) > self.BDPoint.TbLevel):
            self.BDPoint.EnFlag = True
            if((self.BDPoint.SystemTime - self._time)> self.BDPoint.TuTime):
                print("Oddanie krwi na cele naukowe (rozszerzesnie)")
                for i in range(int(self.BDPoint.UnitOnScience)):
                    self.BDPoint.RemoveBloodScience()
                if (self.BDPoint.SystemTime > self.BDPoint.InitialPhase):
                    self.IdEnlargment=self.BDPoint.EnlargmentNumber
                    self.BDPoint.EnlargmentNumber+=1
                self.Phase = 1
        else:
            self.Phase = 1


    def Phase1(self):
        self.BDPoint.EnFlag=False


    def ToString(self):
        return("Oddanie krwi na cele naukowe | czas: " + str(self.ProcessEvent.EventTime))
        