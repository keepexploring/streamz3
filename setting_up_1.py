%load_ext autoreload
%autoreload 2
from streamz3 import Stream
import pipelines as AF
s = AF.Streaming()
# s.add_data({'id_':'testing','value':4})
# s.add_data({'id_':'testing1','value':3})
# s.add_data({'id_':'testing','value':2})
# s.add_data({'id_':'testing1','value':6})
# s.add_data({'id_':'testing1','value':6})
# s.add_data({'id_':'testing','value':10})
# s.add_data({'id_':'testing','value':5})

s.add_data({'id_':'testing', 'data':np.array([1,2,3])})  # seed with initial values, where the index is the first value in seconds
s.add_data({'id_':'testing', 'data':np.array([20,2,3])})
s.add_data({'id_':'testing', 'data':np.array([30,5,3])})
s.add_data({'id_':'testing', 'data':np.array([40,8,3])})
s.add_data({'id_':'testing', 'data':np.array([50,2,9])})
s.add_data({'id_':'testing', 'data':np.array([60,4,11])})
s.add_data({'id_':'testing', 'data':np.array([70,4,11])})
s.add_data({'id_':'testing', 'data':np.array([80,4,11])})
s.add_data({'id_':'testing', 'data':np.array([90,4,11])})
s.add_data({'id_':'testing', 'data':np.array([100,4,11])})
s.add_data({'id_':'testing', 'data':np.array([110,4,11])})
s.add_data({'id_':'testing', 'data':np.array([120,4,11])})
s.add_data({'id_':'testing', 'data':np.array([130,4,11])})
s.add_data({'id_':'testing', 'data':np.array([140,4,14])})
s.add_data({'id_':'testing', 'data':np.array([150,43,11])})
s.add_data({'id_':'testing', 'data':np.array([160,11,12])})
s.add_data({'id_':'testing', 'data':np.array([170,156,14])})
s.add_data({'id_':'testing', 'data':np.array([180,164,17])})
s.add_data({'id_':'testing', 'data':np.array([190,103,17])})