import numpy
from Patient import Patient
from bdp import BloodDonationPoint
from Donor import Donor
from Enlargment import Enlargment
from BloodUnit import BloodUnit
from EmergencyBlood import EmergencyBlood
from Blood import Blood

class Program(object):
    empCount = 0

    def __init__(self):
        self.bloodDonationPoint = BloodDonationPoint()
        self.Patient=Patient(self.bloodDonationPoint)
        self.Patient.Activate(1.0)

        self.Donor=Donor(self.bloodDonationPoint)
        self.Donor.Activate(1.0)

        # self.Patient.Activate(1.0)
        # try:
        #     stepMode=int(input('Przeprowadzic symulacje krokowo(1) czy ciagle(2):'))
        # except ValueError:
        #     print("Zla odpowiedz")

        stepMode=0
        unitsOfBloodAfterInitalyPhase = 0
        subsidiaryFlag = True
        #PAtientID -> patientNumber

        while(Patient._PatientID < 5000):

            if(Patient._PatientID==10):
                print("dupa")
            if(self.bloodDonationPoint.SystemTime > 9999 and subsidiaryFlag == True):
                unitsOfBloodAfterInitalyPhase=BloodUnit._BloodId
                subsidiaryFlag=False
            # a=
            self.currentProcess=self.bloodDonationPoint.Schedule.GetFirstEvent().process
            self.bloodDonationPoint.SystemTime=self.currentProcess.ProcessEvent.EventTime
            # print("Sadas")
            print("Czas " + str(self.bloodDonationPoint.SystemTime))

            self.currentProcess.Execute()

            if(len(self.bloodDonationPoint.PatientQueue) != 0 and self.bloodDonationPoint.busyFlag == False):
                job=self.bloodDonationPoint.PatientQueue.popleft()
                job.Activate(0.0)
            print("\n Kolejne:")
            self.bloodDonationPoint.Schedule.Print()

            if(stepMode==True):
                try:
                    input("Press enter to continue")
                except SyntaxError:
                    pass
        print("Czas na fazę początkową = " +  str(self.bloodDonationPoint.InitialPhase))
        print("Krew na badania naukowe oddano " + str(self.bloodDonationPoint.EnlargmentNumber) + ", w sumie na badania oddano " + str(self.bloodDonationPoint.BloodForScience) + " jednostek krwi.")
        print("Obsluzono " + str(Patient._PatientID) + " pacjentow")
        print("Obsluzono " + str(Donor._DonorID) + " dawcow")
        print("Przez symulacje bylo " + str(BloodUnit._BloodId - unitsOfBloodAfterInitalyPhase) + " różnych jednostek krwi")
        print("Az, " + str(self.bloodDonationPoint.UtilizedBlood) + " zostało zutylizowanych")
        print("Krew zamowiono awaryjnie " + str(EmergencyBlood._AmoutOfemergency) + " razy, a standardowo " + str(Blood._AmountOfStandardOrders))
        print("Cos")
        print("Cos2")
        
run=Program()