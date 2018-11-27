from streamz3 import Stream
import pipelines as pl
from tornado.ioloop import IOLoop

import numpy as np


s = pl.Streaming()


async def fill_pipeline():
    while True:
        await s.add_data({'_id_':'testing', 'data':np.array([1,2,3])})


if __name__ == '__main__':
    IOLoop.current().run_sync(fill_pipeline)