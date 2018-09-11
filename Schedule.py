import Event

class Schedule():
    def __init__(self):
        self.schedule = []

    def getKey(self,time):
        return int(time.EventTime)

    def Insert(self,event):
        # self.ev = event
        self.schedule.append(event)
        # print(self.schedule)
        sorted(self.schedule, key=self.getKey) 
        # print(self.schedule)

    def Print(self):
        for value in self.schedule:
            print(value.process.ToString())

    def GetFirstEvent(self):
        # self.temp=
        a=self.schedule[0]
        print(len(self.schedule))
        del(self.schedule[0])
        
        print(len(self.schedule))
        return(a)

# print("d")