import numpy
from Patient import Patient
from bdp import BloodDonationPoint
from Donor import Donor

class Program():
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

        while(self.bloodDonationPoint.PatientNumber < 5000):
            if(self.bloodDonationPoint.SystemTime > 9999 and subsidiaryFlag == True):
                unitsOfBloodAfterInitalyPhase=self.bloodDonationPoint.BloodNumber
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
                input()
        print("Czas na fazę początkową = " +  str(self.bloodDonationPoint.InitialPhase))
        print("Krew na badania naukowe oddano " + str(self.bloodDonationPoint.EnlargmentNumber) + ", w sumie na badania oddano " + str(self.bloodDonationPoint.BloodForScience) + " jednostek krwi.")
        print("Obsluzono " + str(self.bloodDonationPoint.PatientNumber) + " pacjentow")
        print("Obsluzono " + str(self.bloodDonationPoint.DonorNumber) + " dawcow")

run=Program()