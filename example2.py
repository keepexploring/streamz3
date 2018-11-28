from streamz4 import Stream
import pipelines as pl
from tornado.ioloop import IOLoop

import numpy as np
from time import sleep


s = pl.Streaming()


async def fill_pipeline():
    while True:
        await s.add_data({'_id_':'testing', 'data':np.array([1,2,3])})
        sleep(2)
        print("data_added")


if __name__ == '__main__':
    #fill_pipeline()
    IOLoop().run_sync(fill_pipeline)