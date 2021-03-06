import json
from event import Event

class Events:
    def __init__(self, filepath):
        self.filepath = filepath
        self.events = self.load_events()

    def load_events(self):
        try:
            with open(self.filepath,'r') as f:
                events = json.load(f)
                result = []
                for event in events:
                    #Need to update result to event details.
                    levent = Event(event['id'],int(event['creator']),event['chan'],event['event_name'],event['start_date'],event['end_date'],int(event['max']),event['description'],int(event['status']),event['players'])
                    result.append(levent)
                return result
        except(IOError,IndexError):
            print('Failed to load event data.')

    def save_events(self):
        with open(self.filepath,'w') as f:
            nevents = []
            for event in self.events:
                event_dict = event.__dict__
                nevents.append(event_dict)
            json.dump(nevents,f)


    def add_event(self,ctx,name,start_date,end_date,max=None,description=""):
        new_event = Event(len(self.events),ctx.author.id,ctx.channel.id,name,start_date,end_date,max,description)
        self.events.append(new_event)
        self.save_events()
        return new_event.id

    def join_event(self,event_id,player):
        event = self.find_event(event_id)
        if event.status < 2:
            if len(event.players) < event.max:
                if player not in event.players:
                    event.players.append(player)
                    self.save_events()
                    return True
                else:
                    print('Player was in event players')
                    return False
            else:
                print('Event at max capacity.')
                return False
        else:
            print(str(event.status)+' status.')


    def finish_event(self, event_id):
        event = self.find_event(event_id)
        event.finish_event()
        self.save_events()

    def leave_event(self,event_id,player):
        event = self.find_event(event_id)
        if player in event.players:
            event.players.remove(player)
            self.save_events()

    #Helper function to select event in list.
    def find_event(self,event_id):
        for event in self.events:
            if event.id == event_id:
                return event

    
    
  
    