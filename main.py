from Patient import Patient
from BloodDonationPoint import BloodDonationPoint
from Donor import Donor
from BloodUnit import BloodUnit
from EmergencyBlood import EmergencyBlood
from Blood import Blood


class Main():
    def __init__(self):
        self.bdp = BloodDonationPoint()
        self.patient = Patient(self.bdp).activate(1.0)
        self.donor = Donor(self.bdp).activate(1.0)

        # self.patient.activate(1.0)
        # try:
        #     self.stepMode=int(input('Przeprowadzic symulacje krokowo(1) czy ciagle(2):'))
        # except ValueError:
        #     print("Zla odpowiedz")

        self.stepMode = 0

        self.units_of_blood_after_ini_phase = 0
        self.units_of_bloodA_after_ini_phase = 0
        self.units_of_bloodB_after_ini_phase = 0

        self.subsidiary_flag = True

    def main_loop(self):
        while(Patient.patient_counter < 2000):
            if(self.bdp.system_time > 9999 and self.subsidiary_flag == True):
                self.units_of_blood_after_ini_phase = BloodUnit._BloodId
                self.units_of_bloodA_after_ini_phase = BloodUnit._BloodA
                self.units_of_bloodB_after_ini_phase = BloodUnit._BloodB
                self.subsidiary_flag = False
            self.currentProcess = self.bdp.schedule.get_first_event().process
            self.bdp.system_time = self.currentProcess.proces_event.event_time
            print("Czas " + str(self.bdp.system_time))
            self.currentProcess.execute()
            if(len(self.bdp.patient_queue) != 0 and self.bdp.busy_flag == False):
                job = self.bdp.patient_queue.popleft()
                job.activate(0.0)
            print("Nowe zdarzenie \r \n \t")
            self.bdp.schedule.print_schedule()

            if(self.stepMode == True):
                try:
                    input("Press enter to continue")
                except SyntaxError:
                    pass
        print("Czas na fazę początkową = " +
              str(self.bdp.initial_phase))
        print("Obsluzono " + str(Patient.patient_counter) + " pacjentow")
        print("Obsluzono " + str(Donor._DonorID) + " dawcow")
        print("Przez symulacje bylo " +
              str(BloodUnit._BloodId) + " różnych jednostek krwi")
        print("Az, " + str(self.bdp.UtilizedBlood) +
              " zostało zutylizowanych")
        print("Krew zamowiono awaryjnie " + str(EmergencyBlood._AmoutOfemergency) +
              " razy, a standardowo " + str(Blood._AmountOfStandardOrders))
        print("Grupa A:" + str(BloodUnit._BloodA) +
              " Grupa B: " + str(BloodUnit._BloodB))
        print("Zarejestrowano " + str(Patient._PatientA) +
              " pacjetow o grupie A i " + str(Patient._PatientB) + " o grupie B.")


run = Main()
run.main_loop()
