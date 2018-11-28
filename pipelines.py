from streamz4 import Stream
from analysis_functions1 import *
from streamz4.scheduler import Scheduler
from streamz4.create_filter import StreamingFilter


import pdb

class Streaming(StreamingFilter):
    def __init__(self):
        super().__init__()

    async def add_data(self,x):
        ss = self.create_filter(x)
        if ss == True: # if there id is new, i.e. data is coming from a new source
            try:
                self.filters[x["_id_"]].bulk_load(headings=['index','apples','mangos']).map(analyse).sink(save_data1)
            
            except KeyError as ex:
                print(ex)
                raise KeyError("the data must contain an id key in the form '_id_' ")

        await self.source.emit(x)


