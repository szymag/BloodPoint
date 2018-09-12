import Event

class Schedule():
    def __init__(self):
        self.schedule = []

    def getKey(self,time):
        return int(time.EventTime)

    def Insert(self,event):
        self.schedule.append(event)
        self.schedule=sorted(self.schedule, key=self.getKey) 

    def Print(self):
        for value in self.schedule:
            print(value.process.ToString())

    def GetFirstEvent(self):
        a=self.schedule[0]
        del(self.schedule[0])
        return(a) 
