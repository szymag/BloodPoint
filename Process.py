# from BloodDonationPoint import *
from bdp import BloodDonationPoint
import Event

class Process(BloodDonationPoint):
    # BDPoint=0
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