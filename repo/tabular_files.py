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
        year = file_name.split(" ")[-3:][0].split("(")[0]
        if year != previous_year and bool(subgroup):
            grouped_file_list.append(subgroup)
            subgroup = []

        subgroup.append(file_name)
        previous_year = year
    else:
        grouped_file_list.append(subgroup)

    return grouped_file_list

def _call_data_objects_from_file_group(file_group):
    """
    Creates call object list from all data in file group

        Parameters
        ----------
        file_group: list
            list of file names in same date group

        Returns
        -------
        call_data_object_list: list
            list of call data objects generated from files in group

        Raises
        ------
    """
    pass
