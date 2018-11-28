import os,sys,inspect
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) ))

from streamz4 import Stream


class StreamingFilter():
    def __init__(self):
        self.source = Stream(asynchronous=True)
        self.filters={}
        self.function_chains=[]
        self.functions = []

    
    def create_filter(self,data):
        #pdb.set_trace()
        try:
            if data["_id_"] not in self.filters.keys():
                self.filters[data["_id_"]]=self.source.filter(lambda x: x["_id_"]==data["_id_"])
                return True
            else:
                return False
        except KeyError as ex:
            print(ex)
            raise KeyError("the data must contain an id key in the form '_id_' ")
        


            # the other functions we want to carryout as part of the analysis will go after the filter function
            # This allow us to carry out the same analysis for multiple sensors
            # We should include the timestamp in the data and after this prototype write it so that it works as a numpy array