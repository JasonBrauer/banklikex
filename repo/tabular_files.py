import csv
import copy
from os import listdir

from entities.data_models import call_data_field_dict, call_data_identifier_dict, CallData

def import_call_schedule_data(directory):
    """
    Imports data from tab delimited call reports

        Parameters
        ----------
        directory: str
            single unnested directory containing call schedule tab delimited files

        Returns
        -------
        call_data_object_dict: dict
            dict with year as key and values as call data object lists filled with imported data

        Raises
        ------
    """
    data_file_names = [f for f in listdir(directory) if f[0:21] == "FFIEC CDR Call Subset"]
    grouped_file_dict = _group_files_by_year(data_file_names)
    call_data_object_dict = {}
    for key in grouped_file_dict:
        grouped_call_data_object_list = _call_data_objects_from_file_group(grouped_file_dict[key], 
        directory)
        call_data_object_dict[key] = grouped_call_data_object_list


    return call_data_object_dict

def _group_files_by_year(file_list):
    """
    Groups call report files in list by year in file name

        Parameters
        ----------
        file_list: list
            list of call data file names

        Returns
        -------
        grouped_file_dict: dict
            dictionary of call data file names grouped by year

        Raises
        ------
    """
    grouped_file_dict = {}
    previous_year = ""
    subgroup = []
    for file_name in file_list:
        year = file_name.split(" ")[-3:][0].split("(")[0]
        if year != previous_year and bool(subgroup):
            grouped_file_dict[previous_year] = subgroup
            subgroup = []

        subgroup.append(file_name)
        previous_year = year
    else:
        grouped_file_dict[previous_year] = subgroup

    return grouped_file_dict

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
        with open(file_w_directory, mode='r') as call_data_file:
            call_data_reader = csv.reader(call_data_file, delimiter="\t")
            row_num = 0
            for row in call_data_reader:
                if row_num == 0:
                    header = row
                    id_header_index_dict = _create_id_header_index_dictionary(header)
                    field_header_index_dict = _create_field_header_index_dictionary(header)
                elif row_num > 1:
                    _build_call_data_object_list(
                        call_data_object_list,
                        id_header_index_dict,
                        field_header_index_dict,
                        row,
                        row_num,
                        file_num
                    )

                row_num += 1

        file_num += 1

    return call_data_object_list

def _build_call_data_object_list(call_data_object_list, id_header_index_dict, 
field_header_index_dict, row, row_num, file_num):
    """
    Appends data to provided call data object list

        Parameters
        ----------
        call_data_object_list: list
            list of call data objects
        id_header_index_dict: dict
            dictionary containing id header names as keys in index as values
        field_header_index_dict: dict
            dictionary containing field header names as keys in index as values
        row: list
            row of data from call data file
        row_num: int
            number of the row in the call data file
        file_num: int
            call data file number

        Returns
        -------
        call_data_object_list: list
            list of call data objects including those modified by this function

        Raises
        ------
    """
    if file_num == 0:
        call_data_object = CallData()
        '''
            collect each call data identifier
        '''
        for key in id_header_index_dict:
            setattr(call_data_object, call_data_identifier_dict[key], 
            row[id_header_index_dict[key]])

        '''
            collect required fields and build objects
        '''
        row_field_dict = {}
        for key in field_header_index_dict:
            '''
                convert strings for data fields to int when loading into call data obj 
                field dict
            '''
            value = row[field_header_index_dict[key]]
            try:
                value = int(value)
            except:
                '''
                    if cannot convert value to int, then store as None so can throw out of analysis
                '''
                value = None
            row_field_dict[call_data_field_dict[key]] = value
        setattr(call_data_object, "field_dict", row_field_dict)
        call_data_object_list.append(call_data_object)
    else:
        '''
            fill in remaining required fields in call data objects from additional files
            match unique identifier btwn row and call data object
            need to convert string idrssd into int for match
            binary chop for idrssd match match time by about 2x
        '''
        call_data_object = _call_data_idrssd_match(
            int(row[id_header_index_dict["IDRSSD"]]), 
            call_data_object_list
        )
        '''
            collect required fields and fill in relevant object fields
        '''
        if call_data_object is not None:
            for key in field_header_index_dict:
                '''
                    convert strings for data fields to int when loading into call data obj 
                    field dict
                '''
                value = row[field_header_index_dict[key]]
                try:
                    value = int(value)
                except:
                    value = None
                getattr(call_data_object, "field_dict")[call_data_field_dict[key]] = value
        
    return call_data_object_list

def _call_data_idrssd_match(row_idrssd, call_data_object_list):
    """
    Finds the call data object with idrssd that matches the current row idrssd

        Parameters
        ----------
        row_idrssd: int
            idrssd from current data row
        call_data_object_list: list
            list of call data objects

        Returns
        -------
        call_data_object: CallData object or None
            call data object that matches the provided row idrssd or None

        Raises
        ------
    """
    call_data_length = len(call_data_object_list)
    call_data_idrssd_list = [cdo.idrssd for cdo in call_data_object_list]
    call_data_index_list = list(range(call_data_length))
    
    while call_data_length > 1:
        mid_index = _find_middle_index(call_data_idrssd_list)
        if row_idrssd > call_data_idrssd_list[mid_index]:
            call_data_idrssd_list = call_data_idrssd_list[(mid_index + 1):]
            call_data_index_list = call_data_index_list[(mid_index + 1):]
        else:
            call_data_idrssd_list = call_data_idrssd_list[:(mid_index + 1)]
            call_data_index_list = call_data_index_list[:(mid_index + 1)]

        call_data_length = len(call_data_idrssd_list)
    else:
        if row_idrssd == call_data_idrssd_list[0]:
            return call_data_object_list[call_data_index_list[0]]
        else:
            return None

def _find_middle_index(list_in):
    """
    Binary chop to find the middle index of a list defaulting to lower index with even lengths

        Parameters
        ----------
        list_in: list
            list of values

        Returns
        -------
        middle_index: int
            the middle index of a list defaulting to lower index with even lengths

        Raises
        ------
    """
    length = len(list_in)
    if bool(length % 2):
        middle_index = int(length / 2 - 0.5)
    else:
        '''
            default to lower value if even length 
        '''
        middle_index = int(length / 2) - 1

    return middle_index
    
def _create_field_header_index_dictionary(header):
    """
    Creates a dictionary of data index number associated with each desired field header

    Parameters
        ----------
        header: list
            list of headers in call data file

        Returns
        -------
        field_header_index_dict: dict
            dictionary of header indecies

        Raises
        ------
    """
    field_header_index_dict = {}
    for name in header:
        if name in call_data_field_dict.keys():
            field_header_index_dict[name] = header.index(name)

    return field_header_index_dict

def _create_id_header_index_dictionary(header):
    """
    Creates a dictionary of data index number associated with each desired identifier header

    Parameters
        ----------
        header: list
            list of headers in call data file

        Returns
        -------
        id_header_index_dict: dict
            dictionary of header indecies

        Raises
        ------
    """
    id_header_index_dict = {}
    for name in header:
        if name in call_data_identifier_dict.keys():
            id_header_index_dict[name] = header.index(name)

    return id_header_index_dict

