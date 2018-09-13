from Process import Process
from UnitOfBlood import UnitOfBlood


class Donor(Process):
    counter_donor = 0
    counter_donor_a = 0
    counter_donor_b = 0

    def __init__(self, system):
        super().__init__(system)
        self.name = "Donor"
        self.blood_type = self.bdp.Generators.get_blood_type()
        if(self.blood_type == "A"):
            Donor.counter_donor_a += 1
        else:
            Donor.counter_donor_b += 1
        self.time = 1000
        self.donorID = Donor.counter_donor

    def execute(self):
        activate = True
        while(activate):
            if(self.bdp.system_time > self.bdp.initial_phase):
                Donor.counter_donor += 1
            print("Pojawienie sie dawcy nr " + str(self.donorID) +
                  " o grupie krwi " + str(self.blood_type) + "w systemie.")

            Donor(self.bdp).activate(self.bdp.Generators.get_exponential(950))
            self.bdp.add_blood(UnitOfBlood(
                self.bdp, self.bdp.system_time + self.time, self.blood_type, "Standard"))

            print("Aktualny stan jednostek krwi: " +
                  str(len(self.bdp.blood_list_a)+len(self.bdp.blood_list_b)))
            activate = False

    def ToString(self):
        return("Dawca od nr ID: " + str(self.name) + " " + str(self.donorID) + " | czas: " + str(self.proces_event.event_time))
