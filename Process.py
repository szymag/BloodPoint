from BloodBank import blood_bank
from Event import Event


class Process():

    def __init__(self, system):
        self.Phase = 0
        self.BDPoint = system
        self.ProcessEvent = Event(self)

    def Activate(self, time):
        self.ProcessEvent.EventTime = self.BDPoint.SystemTime+time
        self.BDPoint.Schedule.Insert(self.ProcessEvent)
