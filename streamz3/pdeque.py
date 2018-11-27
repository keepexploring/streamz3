import numpy as np
import pandas as pd
from datetime import datetime, time, timedelta
import pdb

class Pdeque():
    def __init__(self,window_size=60,batch_time=20,interval=30,schedule=-1, headings=None):
        """ The headings should be a list, one for each element, not including the index
        window size is the size of the complete window that is stored, batch size is how often that window is pushed to be analysed"""
        self.window_size=window_size
        self.batch_time=batch_time
        self.interval=interval # this is the sliding interval, and describes how much the dataframes overlap
        self.headings=headings
        self.elements = len(self.headings) # a heading must be provided for each column of data that is being sent to be analysed, including the index
        self.n_array=np.zeros(self.elements) # create an empty array
        self.state = False
        self.next_time = 0
        
        if (window_size == -1):
            self.schedule = schedule.get_interval()
        #if self.headings!=None:
        #    self.headings=headings
        #else:
        #    self.headings=[""]*self.elements

    def starting_array(self,array):
        self.n_array=array

    def append(self,array):
        #pdb.set_trace()
        self.n_array=np.vstack((array,self.n_array))
        #pdb.set_trace()
        if (self.n_array[-1][0]==0): # if there is a zero element from the intialisation remove it
            self.n_array = self.n_array[:-1]
        #if self.maxlen !=None:
            #self.n_array=self.n_array[0:self.maxlen]

    @staticmethod
    def find_nearest(array,value):
        idx = (np.abs(array-value)).argmin()
        return idx

    def push_scheduler(self):
        index=self.n_array[0:,0]
        time_now = datetime.fromtimestamp(index[0])
        pdb.set_trace()
       
        if (self.schedule[0] == 'day'):
            if (self.next_time == 0):
                self.next_time = datetime(year=time_now.year,month=time_now.month,day=time_now.day+1,hour=self.schedule[1].hour,minute=self.schedule[1].minute,second=self.schedule[1].second)

            if (time_now >= self.next_time):
                self.next_time = datetime(year=time_now.year,month=time_now.month,day=time_now.day+1,hour=self.schedule[1].hour,minute=self.schedule[1].minute,second=self.schedule[1].second)
                self.to_return = self.n_array[0:-1]
                self.n_array =  self.n_array[-1]
                return True
            else:
                return False

        elif (self.schedule[0] == 'hour'):
            if (self.next_time == 0):
                self.next_time = datetime(year=time_now.year,month=time_now.month,day=time_now.day,hour=time_now.hour+1,minute=self.schedule[1].minute,second=self.schedule[1].second)

            if (time_now >= self.next_time):
                self.next_time = datetime(year=time_now.year,month=time_now.month,day=time_now.day,hour=time_now.hour+1,minute=self.schedule[1].minute,second=self.schedule[1].second)
                self.to_return = self.n_array[0:-1]
                self.n_array =  self.n_array[-1]
                return True
            else:
                return False
            
        elif (self.schedule[0] == 'minute'):
            if (self.next_time == 0):
                self.next_time = datetime(year=time_now.year,month=time_now.month,day=time_now.day,hour=time_now.hour,minute=time_now.minute+1,second=self.schedule[1].second)

            if (time_now >= self.next_time):
                self.next_time = datetime(year=time_now.year,month=time_now.month,day=time_now.day,hour=time_now.hour,minute=time_now.minute+1,second=self.schedule[1].second)
                self.to_return = self.n_array[0:-1]
                self.n_array =  self.n_array[-1]
                return True
            else:
                return False
        elif (self.schedule[0] == 'seconds'): # this runs every specified number of seconds
            
            if (self.next_time == 0):
                self.next_time=datetime(year=time_now.year,month=time_now.month,day=time_now.day,hour=time_now.hour,minute=time_now.minute,second=time_now.second) + timedelta(seconds=self.schedule[1].second)

            if (time_now >= self.next_time):
                self.next_time=datetime(year=time_now.year,month=time_now.month,day=time_now.day,hour=time_now.hour,minute=time_now.minute,second=time_now.second) + timedelta(seconds=self.schedule[1].second)
                #self.next_cut_time = seconds_now + self.schedule[1].second
                self.to_return = self.n_array[0:-1]
                self.n_array =  self.n_array[-1]
                return True
            else:
                return False


    def push(self):
        """Returns True or False depending on if the 'slide' time had been reached or not"""
        #pdb.set_trace()
        index=self.n_array[0:,0]
        old_time = index[-1]
        new_time = index[0]
        if (new_time-old_time >= self.window_size):
            time_to_find = old_time + self.batch_time
            ind = self.find_nearest(index,time_to_find)
            self.to_return = self.n_array[ind+1:]
            to_keep = time_to_find - self.interval
            kp = self.find_nearest(index,to_keep)
           # pdb.set_trace()
            self.n_array = self.n_array[0:kp+1] # now we keep the first part and keep adding data, yeah!
            return True
        else:
            return False

    def send(self):
        #pdb.set_trace()
        for el in range(0,self.elements):
            if self.headings is not None:
                if self.headings[0] == 'index':
                    data={hd:self.to_return[0:,i+1] for i,hd in  enumerate(self.headings[1:]) }
                else:
                    data={hd:self.to_return[0:,i+1] for i,hd in  enumerate(self.headings) }

        return pd.DataFrame(index=self.to_return[0:,0],data=data)


    def __str__(self):
        return 'Ndeque({})'.format(self.n_array)

    def __len__(self):
        return len(self.n_array)

    def array(self):
        return self.n_array

    def dataframe(self):
        #pdb.set_trace()
        for el in range(0,self.elements):
            if self.headings is not None:
                if self.headings[0] == 'index':
                    data={hd:self.n_array[0:,i+1] for i,hd in  enumerate(self.headings[1:]) }
                else:
                    data={hd:self.n_array[0:,i+1] for i,hd in  enumerate(self.headings) }



        return pd.DataFrame(index=self.n_array[0:,0],data=data)
