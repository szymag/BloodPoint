import Event


class Schedule():
    def __init__(self):
        self.schedule = []

    def getKey(self, time):
        return int(time.event_time)

    def Insert(self, event):
        self.schedule.append(event)
        self.schedule = sorted(self.schedule, key=self.getKey)

    def print_schedule(self):
        for value in self.schedule:
            print(value.process.ToString())

    def get_first_event(self):
        a = self.schedule[0]
        del(self.schedule[0])
        return(a)
