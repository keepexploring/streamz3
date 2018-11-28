from tinydb import TinyDB, Query

from streamz4.decorators import package_stream
import numpy as np
import pandas as pd
import pdb

def write_to_database(data):
    #pdb.set_trace()
    db = TinyDB('db1.json')
    db.insert({'id':data["id_"],'mean':data['mean']})
    
def rolling_mean(x): # we can inherit these functions maybe/import
    aa=[i['value'] for i in x] # this is what we need to
    rolling_mean=np.mean(aa)
    #pdb.set_trace()
    return {'mean':rolling_mean,'_id_':x[0]['_id_']}

def fpfunction(bb):
    #pdb.set_trace()
  
    data = hello['data']
    return {'_id_':bb['id_'], 'data':data['apples'].iloc[0]*data['mangos'].iloc[0]}


@package_stream
def analyse(data):
   
    print(data)
    return data

@package_stream
def save_data1(data): # e.g. this might be the mean or something
    #pdb.set_trace()
   
    db = TinyDB('db17.json')
    print(data)
    #db.insert({'_id_':cc["_id_"],'data':cc['data']})
