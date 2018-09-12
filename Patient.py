from Process import Process
import time
# from Distributions import Distributions
from Enlargment import Enlargment
from EmergencyBlood import EmergencyBlood
from Blood import Blood

class Patient(Process):
    _PatientID=0
    # active=False
    # ID=0
    def __init__(self, system):
        super().__init__(system)
        self.name="Pacjet"
        self.BrithTime = self.BDPoint.SystemTime
        self.BloodNeeded = self.BDPoint.Distributions.GetGeometric()
        if(self.BloodNeeded==0):
            self.BloodNeeded = 1
        # Patient._PatientID=self.BDPoint.PatientNumber
        self.ID=Patient._PatientID
        print("Patien number " + str(Patient._PatientID))
        if(self.BDPoint.SystemTime > self.BDPoint.InitialPhase):
            Patient._PatientID +=1
        # self.
    
    def Execute(self):
        self.active=True
        while(self.active):
            
            if(self.Phase==0):
                self.Phase0()
            elif(self.Phase==1):
                self.Phase1()
            elif(self.Phase==2):
                self.Phase2()
            elif(self.Phase==3):
                self.Phase3()
            elif(self.Phase==4):
                self.Phase4()

    def Phase0(self):
        run=Patient(self.BDPoint)
        run.Activate(self.BDPoint.Distributions.GetExponential(250))
        self.BDPoint.PatientQueue.append(self)
        print("dodatno do kolejki pacjenta ",self.ID)
        self.Phase=1
        self.active=False
    
    def Phase1(self):
        if(len(self.BDPoint.BloodList) != 0):
            while(self.BDPoint.BloodList[0].ExpirationDate < self.BDPoint.SystemTime):
                self.BDPoint.RemoveBlood()
                if(len(self.BDPoint.BloodList) == 0):
                    break       
        if(len(self.BDPoint.BloodList) > self.BDPoint.TbLevel and self.BDPoint.EnFlag == False):
            self.BDPoint.EnVariable = Enlargment(self.BDPoint)
        if(self.BDPoint.EnVariable != 0):
            self.BDPoint.EnVariable.Execute()
        
        if(len(self.BDPoint.BloodList) < self.BDPoint.MinimalBlood):
            temp_run=Blood(self.BDPoint)
            temp_run.Activate(0.0)
            pass

        self.Phase=2

    def Phase2(self):
        if(len(self.BDPoint.BloodList)< self.BloodNeeded):
            temp_run=EmergencyBlood(self,self.BDPoint)
            temp_run.Activate(0.0)
            self.active=False
            print("Zamowiono awaryjnie krew dla pacjenta o nr ID: " + str(Patient._PatientID) + " Potrzebna krew : " + str(self.BloodNeeded) + " | Czas: " + str(self.BDPoint.SystemTime))
        self.Phase=3
    
    def Phase3(self):
        if(self.BloodNeeded < len(self.BDPoint.BloodList)):
            print("Pacjent od nr ID" + str(self.ID) + "otrzymal " + str(self.BloodNeeded) + " jednostek krwi" )
            for i in range(self.BloodNeeded):
                del(self.BDPoint.BloodList[0])
            print("Pacjent o nr ID " + str(self.ID) + " wyszedl.")
            self.BDPoint.busyFlag = 0
            self.active=False
            self.Phase=4
        else:
            temp_run=EmergencyBlood(self,self.BDPoint)
            temp_run.Activate(0.0)
            self.active=False
            print("Zamowiono awaryjnie krew dla Pacjenta o nr ID" + str(self.ID) + " | Potrzebna krew: "+ str(self.BloodNeeded) + " | czas: " + str(self.BDPoint.SystemTime))

    def Phase4(self):
        self.BDPoint.busyFlag=False
        if(len(self.BDPoint.PatientQueue) != 0):
            self.active=True  
        else:
            self.active=False

    def ToString(self):
        return("Pacjent od nr ID : " + str(self.ID) +  " | czas: " + str(self.ProcessEvent.EventTime))





# Pat=Patient()