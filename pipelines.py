from streamz3 import Stream
from analysis_functions1 import *
from scheduler import Scheduler
from streamz3.create_filter import StreamingFilter
import pdb

class Streaming(StreamingFilter):
    def __init__(self):
        super().__init__()

    def add_data(self,x):
        #pdb.set_trace()
        ss = self.create_filter(x)
        if ss == True: # if there id is new, i.e. data is coming from a new source
            #self.filters[x["id_"]].sliding_window(3).map(rolling_mean).sink(write_to_database)
            #self.filters[x["id_"]].sliding_window_pandas(3,3,headings=['index','apples','mangos']).map(fp)
            #self.filters[x["id_"]].sliding_time_window_pandas(batch_time=2, window_size=4, interval=1, headings=['index','apples','mangos']).map(fp).sink(save_data1)
            self.filters[x["id_"]].sliding_time_window_pandas_scheduled( schedule=Scheduler().every().minute.at('0:0:0'), headings=['index','apples','mangos']).map(fp).sink(save_data1)
            #self.filters[x["id_"]].sliding_time_window_pandas_scheduled( schedule=Scheduler().every(30).seconds.startingat('0:0:20'), headings=['index','apples','mangos']).map(fp).sink(save_data1)
            # for ref batch_time is the same as window_length in apache spark streaming, and interval is the same as interval (and is how much the overlap is in what we send), window_size here is the size of the store that we buffer in memory - useful when lots of data is arriving a bulk load
            # if the interval is set to 0 then then data will be sent in blocks - e.g. a 60 minute block, followed by the next 60 minute block.
        self.source.emit(x)


