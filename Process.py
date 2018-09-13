from Event import Event


class Process():

    def __init__(self, bdp):
        self.phase = 0
        self.bdp = bdp
        self.proces_event = Event(self)

    def activate(self, time):
        self.proces_event.event_time = self.bdp.system_time+time
        self.bdp.schedule.insert(self.proces_event)
