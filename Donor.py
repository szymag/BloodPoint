from Process import Process
# from BloodDonationPoint import BloodDonationPoint
# from Distributions import Distributions
from BloodUnit import BloodUnit
class Donor(Process):
    DonorID=0
    def __init__(self,system):
        super().__init__(system)
        self.name="Donor"
        self.Time=1000
        
        # self.BDPoint=system
        # self.

    def Execute(self):
        activate=True
        while(activate):
            if(self.BDPoint.SystemTime>self.BDPoint.InitialPhase):
                self.DonorID+=1
            print("Pojawienie sie dawcy nr " + str(self.DonorID) + " w systemie.")
            
            newDonor=Donor(self.BDPoint)
            newDonor.Activate(self.BDPoint.Distributions.GetExponential(950))
            self.BDPoint.AddBlood(BloodUnit(self,self.BDPoint.SystemTime + self.Time))

            print("Aktualny stan jednostek krwi: " + str(len(self.BDPoint.BloodList)))
            activate=False

    def ToString(self):
        return("Dawca od nr ID: " + str(self.name) + " "+ str(self.DonorID) + " | czas: " + str(self.ProcessEvent.EventTime) )