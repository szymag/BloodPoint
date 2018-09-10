<<<<<<< HEAD
# from BloodDonationPoint import *
from bdp import BloodDonationPoint
import Event

class Process(BloodDonationPoint):
    BDPoint=0
    def __init__(self,system):
        self.Phase = 0
        self.BDPoint = system
        self.ProcessEvent = Event.Event(self)
        # print('asd')

    def Activate(self,time):
        # pass
        self.ProcessEvent.EventTime = self.BDPoint.SystemTime+time
        self.BDPoint.Schedule.Insert(self.ProcessEvent)

# a=Process()
=======
import BloodDonationPoint

class Process(BloodDonationPoint.BloodDonationPoint):
    def __init__(self):
        self.Phase = 0
        self.BdPoint = BloodDonationPoint.BloodDonationPoint()
        self.ProcessEvent = Event(self)

    def Activate(self,time):
        self.ProcessEvent = self.BdPoint.SystemTime + time
        self.BdPoint.Schedule.Insert(self.ProcessEvent)
>>>>>>> 4f4fc14c96e7c6c9d79354c4f43045ef07401993
