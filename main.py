from Patient import Patient
from BloodDonationPoint import BloodDonationPoint
from Donor import Donor
from UnitOfBlood import UnitOfBlood
from EmergencyBlood import EmergencyBlood
from Blood import Blood


class Main():
    def __init__(self):
        self.bdp = BloodDonationPoint()
        self.patient = Patient(self.bdp).activate(1.0)
        self.donor = Donor(self.bdp).activate(1.0)

        self.patient.activate(1.0)
        try:
            self.stepMode = int(
                input('Przeprowadzic symulacje krokowo(1) czy ciagle(2):'))
        except ValueError:
            print("Zla odpowiedz")

        self.units_of_blood_after_ini_phase = 0
        self.units_ofcounter_blood_id_a_after_ini_phase = 0
        self.units_ofcounter_blood_id_b_after_ini_phase = 0
        self.subsidiary_flag = True

    def main_loop(self):
        while(Patient.counter_patient < 2000):
            if(self.bdp.system_time > 9999 and self.subsidiary_flag == True):
                self.units_of_blood_after_ini_phase = UnitOfBlood.counter_blood_id
                self.units_ofcounter_blood_id_a_after_ini_phase = UnitOfBlood.counter_blood_id_a
                self.units_ofcounter_blood_id_b_after_ini_phase = UnitOfBlood.counter_blood_id_b
                self.subsidiary_flag = False
            self.current_process = self.bdp.schedule.get_first_event().process
            self.bdp.system_time = self.current_process.proces_event.event_time
            print("Czas " + str(self.bdp.system_time))
            self.current_process.execute()
            if(len(self.bdp.patient_queue) != 0 and self.bdp.busy_flag == False):
                self.bdp.patient_queue.popleft().activate(0.0)
            print("Nowe zdarzenie \r \n \t")
            self.bdp.schedule.print_schedule()

            if(self.stepMode == True):
                try:
                    input("Press enter to continue")
                except SyntaxError:
                    pass
        print("Czas na fazę początkową = " +
              str(self.bdp.initial_phase))
        print("Obsluzono " + str(Patient.counter_patient) + " pacjentow")
        print("Obsluzono " + str(Donor.counter_donor) + " dawcow")
        print("Przez symulacje bylo " +
              str(UnitOfBlood.counter_blood_id) + " różnych jednostek krwi")
        print("Az, " + str(self.bdp.utilized_blood) +
              " zostało zutylizowanych")
        print("Krew zamowiono awaryjnie " + str(EmergencyBlood.counter_emergency) +
              " razy, a standardowo " + str(Blood.counter_standard_order))
        print("Grupa A:" + str(UnitOfBlood.counter_blood_id_a) +
              " Grupa B: " + str(UnitOfBlood.counter_blood_id_b))
        print("Zarejestrowano " + str(Patient.counter_patient_a) +
              " pacjetow o grupie A i " + str(Patient.counter_patient_b) + " o grupie B.")


run = Main()
run.main_loop()
