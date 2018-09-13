import Event


class Schedule():
    def __init__(self):
        self.schedule = []

    def getKey(self, time):
        return int(time.event_time)

    def insert(self, event):
        self.schedule.append(event)
        self.schedule = sorted(self.schedule, key=self.getKey)

    def print_schedule(self):
        for var in self.schedule:
            print(var.process.get_process_info())

    def get_first_event(self):
        a = self.schedule[0]
        del(self.schedule[0])
        return(a)
