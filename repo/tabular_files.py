import csv
from os import listdir
from os.path import isfile

def import_call_schedule_data(directory):
    """
    Imports data from tab delimited call reports

        Parameters
        ----------
        directory: str
            directory containing call schedule tab delimited files

        Returns
        -------
        call_object_list: list
            list of call data objects filled with imported data

        Raises
        ------
    """
    data_file_names = [f for f in listdir(directory) if isfile(f) 
    and f[0:14] == "FFIEC CDR Call Subset"]

    return data_file_names
