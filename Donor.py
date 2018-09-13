from Process import Process
from BloodUnit import BloodUnit


class Donor(Process):
    _DonorID = 0
    _DonorA = 0
    _DonorB = 0

    def __init__(self, system):
        super().__init__(system)
        self.name = "Donor"
        self.BloodType = self.BDPoint.Distributions.GetBloodType()
        if(self.BloodType == "A"):
            Donor._DonorA += 1
        else:
            Donor._DonorB += 1
        self.Time = 1000
        self.DonorID = Donor._DonorID

    def Execute(self):
        activate = True
        while(activate):
            if(self.BDPoint.SystemTime > self.BDPoint.InitialPhase):
                Donor._DonorID += 1
            print("Pojawienie sie dawcy nr " + str(self.DonorID) +
                  " o grupie krwi " + str(self.BloodType) + "w systemie.")

            newDonor = Donor(self.BDPoint)
            newDonor.Activate(self.BDPoint.Distributions.get_exponential(950))
            self.BDPoint.AddBlood(BloodUnit(
                self.BDPoint, self.BDPoint.SystemTime + self.Time, self.BloodType, "Standard"))

            print("Aktualny stan jednostek krwi: " +
                  str(len(self.BDPoint.BloodListA)+len(self.BDPoint.BloodListB)))
            activate = False

    def ToString(self):
        return("Dawca od nr ID: " + str(self.name) + " " + str(self.DonorID) + " | czas: " + str(self.ProcessEvent.EventTime))
