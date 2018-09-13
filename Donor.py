from Process import Process
from BloodUnit import BloodUnit


class Donor(Process):
    _DonorID = 0
    _DonorA = 0
    _DonorB = 0

    def __init__(self, system):
        super().__init__(system)
        self.name = "Donor"
        self.BloodType = self.bdp.Distributions.GetBloodType()
        if(self.BloodType == "A"):
            Donor._DonorA += 1
        else:
            Donor._DonorB += 1
        self.Time = 1000
        self.donorID = Donor._DonorID

    def execute()(self):
        activate = True
        while(activate):
            if(self.bdp.system_time > self.bdp.initial_phase):
                Donor._DonorID += 1
            print("Pojawienie sie dawcy nr " + str(self.donorID) +
                  " o grupie krwi " + str(self.BloodType) + "w systemie.")

            newDonor = Donor(self.bdp)
            newDonor.activate(self.bdp.Distributions.get_exponential(950))
            self.bdp.AddBlood(BloodUnit(
                self.bdp, self.bdp.system_time + self.Time, self.BloodType, "Standard"))

            print("Aktualny stan jednostek krwi: " +
                  str(len(self.bdp.BloodListA)+len(self.bdp.BloodListB)))
            activate = False

    def ToString(self):
        return("Dawca od nr ID: " + str(self.name) + " " + str(self.donorID) + " | czas: " + str(self.proces_event.event_time))
