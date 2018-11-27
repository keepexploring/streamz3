import numpy as np
import pandas as pd
import pdb

class Ndeque():
    def __init__(self,maxlen=None,elements=2,headings=None):
        """ The headings should be a list, one for each element, not including the index"""
        self.maxlen=maxlen
        self.elements=elements
        self.n_array=np.zeros(self.elements)
        self.headings=headings
        if self.headings!=None:
            self.headings=headings
        else:
            self.headings=[""]*self.elements


    def starting_array(self,array):
        self.n_array=array

    def append(self,array):
        self.n_array=np.vstack((array,self.n_array))
        if self.maxlen !=None:
            self.n_array=self.n_array[0:self.maxlen]


    def __str__(self):
        return 'Ndeque({})'.format(self.n_array)

    def __len__(self):
        return len(self.n_array)

    def array(self):
        return self.n_array

    def dataframe(self):
        pdb.set_trace()
        for el in range(0,self.elements):
            if self.headings is not None:
                if self.headings[0] == 'index':
                    data={hd:self.n_array[0:,i+1] for i,hd in  enumerate(self.headings[1:]) }
                else:
                    data={hd:self.n_array[0:,i+1] for i,hd in  enumerate(self.headings) }



        return pd.DataFrame(index=self.n_array[0:,0],data=data)
