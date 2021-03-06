from datetime import datetime
from dateutil.relativedelta import relativedelta

class Event:
    def __init__(self,id,creator,chan,name,start_date,end_date,max=None,description="",status=0,players=None):
        self.id = id
        self.creator = creator
        self.chan = chan
        self.event_name = name
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.max = max
        self.status = status #0=reigstered, 1=ready, 2=started 3=complete 4=committed, -1 = cancelled.
        self.players = players
        if players == None:
            self.players = []
              
    def ready_event(self):
        self.status = 1
    
    def start_event(self):
        self.status = 2

    def finish_event(self):
        self.status = 3

    def commit_event(self):
        self.status = 4
    
    def cancel_event(self):
        self.status = -1

    def get_players(self):
        return self.players

    def starting_in(self):
        dto = datetime.strptime(self.start_date, '%Y-%m-%d %H:%M:%S')
        timeleft = self.time_left(dto)
        return str(timeleft)

    def ending_in(self):
        dto = datetime.strptime(self.end_date, '%Y-%m-%d %H:%M:%S')
        timeleft = self.time_left(dto)
        return str(timeleft)
    

    #Returns the given amount of time left in D/H/M/S.
    def time_left(self,datetime_obj):
        '''
        Returns the amount of time remaining on the datetime obj.
        '''
        now = datetime.now()
        rd = relativedelta(now, datetime_obj)
        seconds = rd.seconds * -1
        minutes = rd.minutes * -1
        hours = rd.hours * -1
        days = rd.days * -1
        out = "{}d, {}h, {}m, {}s".format(days, hours, minutes, seconds)
        return(out)


