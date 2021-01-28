import csv
from os import listdir

from entities.data_models import call_data_import_list

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

def _call_data_objects_from_file_group(file_group, directory):
    """
    Creates call object list from all data in file group

        Parameters
        ----------
        file_group: list
            list of file names in same date group
        directory: str
            directory of call data files in raw or escaped format

        Returns
        -------
        call_data_object_list: list
            list of call data objects generated from files in group

        Raises
        ------
    """
    call_data_object_list = []

    file_num = 0
    for file_name in file_group:
        file_w_directory = directory + "\\" + file_name
        with open(file_w_directory, mode='br') as call_data_file:
            call_data_reader = csv.reader(call_data_file, delimiter="\t")
            row_num = 0
            for row in call_data_reader:
                if row_num == 0:
                    header = row

        file_num += 1

def _create_header_index_dictionary(header):
    """
    Creates a dictionary of data index number associated with each desired header

    Parameters
        ----------
        header: list
            list of headers in call data file

        Returns
        -------
        header_index_dict: dict
            dictionary of header indecies

        Raises
        ------
    """
    header_index_dict = {}
    for field in header:
        if field in call_data_import_list:
            header_index_dict[field] = header.index(field)

    return header_index_dict

