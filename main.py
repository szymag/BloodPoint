from Patient import Patient
from BloodBank import blood_bank
from Donor import Donor
from BloodUnit import BloodUnit
from EmergencyBlood import EmergencyBlood
from Blood import Blood


class Main():
    def __init__(self):
        self.blood_bank = blood_bank()
        self.Patient = Patient(self.blood_bank).Activate(1.0)
        self.Donor = Donor(self.blood_bank).Activate(1.0)

        # self.Patient.Activate(1.0)
        # try:
        #     self.stepMode=int(input('Przeprowadzic symulacje krokowo(1) czy ciagle(2):'))
        # except ValueError:
        #     print("Zla odpowiedz")

        self.stepMode = 0
        self.unitsOfBloodAfterInitalyPhase = 0
        self.subsidiaryFlag = True

    def main_loop(self):
        while(Patient.patient_counter < 2000):
            if(self.blood_bank.SystemTime > 9999 and self.subsidiaryFlag == True):
                self.unitsOfBloodAfterInitalyPhase = BloodUnit._BloodId
                self.subsidiaryFlag = False
            self.currentProcess = self.blood_bank.Schedule.GetFirstEvent().process
            self.blood_bank.SystemTime = self.currentProcess.ProcessEvent.EventTime
            print("Czas " + str(self.blood_bank.SystemTime))
            self.currentProcess.Execute()
            if(len(self.blood_bank.PatientQueue) != 0 and self.blood_bank.busyFlag == False):
                job = self.blood_bank.PatientQueue.popleft()
                job.Activate(0.0)
            print("Nowe zdarzenie \r \n \t")
            self.blood_bank.Schedule.Print()

            if(self.stepMode == True):
                try:
                    input("Press enter to continue")
                except SyntaxError:
                    pass
        print("Czas na fazę początkową = " +
              str(self.blood_bank.InitialPhase))
        print("Obsluzono " + str(Patient.patient_counter) + " pacjentow")
        print("Obsluzono " + str(Donor._DonorID) + " dawcow")
        print("Przez symulacje bylo " +
              str(BloodUnit._BloodId) + " różnych jednostek krwi")
        print("Az, " + str(self.blood_bank.UtilizedBlood) +
              " zostało zutylizowanych")
        print("Krew zamowiono awaryjnie " + str(EmergencyBlood._AmoutOfemergency) +
              " razy, a standardowo " + str(Blood._AmountOfStandardOrders))
        print("Grupa A:" + str(BloodUnit._BloodA) +
              " Grupa B: " + str(BloodUnit._BloodB))
        print("Zarejestrowano " + str(Patient._PatientA) +
              " pacjetow o grupie A i " + str(Patient._PatientB) + " o grupie B.")


run = Main()
run.main_loop()
