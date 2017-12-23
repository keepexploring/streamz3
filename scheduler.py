import datetime
import pdb

class Scheduler(object):
    """A function for creating an object to collect the schedule for running the analysis at regular intervals
    example of use:
    SS=Scheduler()
    SS.every().hour.at('0:0:0') # in the at command you put in 'hour:minute:second' when you want the command to repeatedly run e.g. if it was every().day.at('4:0:0') for a system you want to run at the 4th hour of everyday
    SS.get_interval() # to get the schedule that has been set to use it within an application.
    
    This does not do the running for you, it is just a way to create a scheduler object that can be used in another application
    """
    def __init__(self):
        pass
    
    def every(self,interval=1):
        job = Job(interval)
        return job
    
    
class Job(object):
    def __init__(self, interval):
        self.unit = None
        self.at_time = None
        self.starting_at =None
        self.interval = interval
    
    @property
    def day(self):
        self.unit = 'day'
        return self
    
    @property
    def minute(self):
        self.unit = 'minute'
        return self
    
    @property
    def hour(self):
        self.unit = 'hour'
        return self
        
    @property
    def seconds(self):
        self.unit = 'seconds'
        self.at_time = datetime.time(second = self.interval)
        return self
        
        
    def startingat(self, time_str):
        hour, minute, second = time_str.split(':')
        hour = int(hour)
        minute = int(minute)
        second = int(second)
        self.starting_at = datetime.time(hour=hour,minute=minute,second=second)
        
        return self
    
    def at(self, time_str):
        
        hour, minute, second = time_str.split(':')
        if self.unit == 'day':
            hour = int(hour)
            minute = int(minute)
            self.at_time=datetime.time(hour,minute)
            
        elif self.unit == 'hour':
            minute = int(minute)
            self.at_time=datetime.time(minute=minute)
            
        elif self.unit == 'minute':
            second = int(second)
            self.at_time=datetime.time(second=second)
        
        return self
        
    
    def get_interval(self):
        return (self.unit,self.at_time,self.starting_at)
            
        