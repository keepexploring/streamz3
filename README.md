# streamz3

This is a modified version of https://github.com/mrocklin/streamz with some additional functions and scheduling capability.
________________________________________________

create functions in analysis_functions1.py

Add the analysis pipelines in the 'add_data' function in the analysis_framework file

The functions:
sliding_time_window_pandas
sliding_time_window_pandas_scheduled
output {"id_":"sensor_id", "data":pandas dataframe"} to map or sink - so you can more easily do statistical analysis on the incoming data.

Then seeing the setting_up file to see how to send data to the functions, remember to include an id for the different sensors. New separate pipelines will be created for every new data data stream coming in - filter them by sensor id.

Data should be added as a numpy array, with the first element the index, which should be the unix time in seconds.

