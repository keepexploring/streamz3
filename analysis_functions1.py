from tinydb import TinyDB, Query
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
    return {'mean':rolling_mean,'id_':x[0]['id_']}

def fp(bb):
    #pdb.set_trace()
    data = bb['data']
    return {'id_':bb['id_'], 'data':data['apples'].iloc[0]*data['mangos'].iloc[0]}


def save_data1(cc): # e.g. this might be the mean or something
    #pdb.set_trace()
    db = TinyDB('db17.json')
   
    db.insert({'id_':cc["id_"],'data':cc['data']})
