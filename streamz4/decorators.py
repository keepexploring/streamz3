import functools
import pandas as pd


def package_stream(function):
    @functools.wraps(function)
    def wrapper(*argsa, **kwargs):
        data = argsa[0]['data']
        result = function(data=data)
        if isinstance(result, pd.DataFrame):
            result = result.reset_index().values
        result = { 'data': result }
        result['_id_'] = argsa[0]['_id_']
        return result
    return wrapper