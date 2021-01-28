import csv
from os import listdir

def import_call_schedule_data(directory):
    """
    Imports data from tab delimited call reports

        Parameters
        ----------
        directory: str
            single unnested directory containing call schedule tab delimited files

        Returns
        -------
        call_object_list: list
            list of call data objects filled with imported data

        Raises
        ------
    """
    data_file_names = [f for f in listdir(directory) if f[0:21] == "FFIEC CDR Call Subset"]

    return data_file_names

def _group_files_by_year(file_list):
    """
    Groups call report files in list by year in file name

        Parameters
        ----------
        file_list: list
            list of call data file names

        Returns
        -------
        grouped_file_list: list
            list of call data file names grouped by year

        Raises
        ------
    """
    grouped_file_list = []
    previous_year = ""
    subgroup = []
    for file_name in file_list:
        year = file_name.split(" ")[-1:].split("(")
        if year != previous_year:
            grouped_file_list.append(subgroup)
            subgroup = []

        subgroup.append(file_name)

    return grouped_file_list
