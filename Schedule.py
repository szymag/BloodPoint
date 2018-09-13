import Event

class Schedule():
    def __init__(self):
        self.schedule = []

    def get_key(self, time):
        return int(time.event_time)

    def insert(self, event):
        self.schedule.append(event)
        self.schedule = sorted(self.schedule, key=self.get_key)

    def print_schedule(self):
        for var_temp in self.schedule:
            print(var_temp.process.get_process_info())

    def get_first_event(self):
        var_temp = self.schedule.pop(0)
        return(var_temp)
