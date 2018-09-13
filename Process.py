# from BloodDonationPoint import *
from BloodDonationPoint import BloodDonationPoint
from Event import Event
# import Event


class Process():
    # BDPoint=0
    def __init__(self, system):
        self.Phase = 0
        self.BDPoint = system
        self.ProcessEvent = Event(self)
        # print('asd')

    def Activate(self, time):
        # pass
        self.ProcessEvent.EventTime = self.BDPoint.SystemTime+time
        self.BDPoint.Schedule.Insert(self.ProcessEvent)

# a=Process()
