import BloodDonationPoint

class Process(BloodDonationPoint.BloodDonationPoint):
    def __init__(self):
        self.Phase = 0
        self.BdPoint = BloodDonationPoint.BloodDonationPoint()
        self.ProcessEvent = Event(self)

    def Activate(self,time):
        self.ProcessEvent = self.BdPoint.SystemTime + time
        self.BdPoint.Schedule.Insert(self.ProcessEvent)
