import csv
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

        Raises
        ------
    """
    if file_num == 0:
        call_data_object = CallData()
        '''
            collect each call data identifier
        '''
        import pdb; pdb.set_trace()
        for key in id_header_index_dict:
            setattr(call_data_object, call_data_identifier_dict[key], 
            row[id_header_index_dict[key]])

        '''
            collect required fields and build objects
        '''
        row_field_dict = {}
        for key in field_header_index_dict:
            row_field_dict[call_data_field_dict[key]] = row[field_header_index_dict[key]]
        setattr(call_data_object, "field_dict", row_field_dict)

        call_data_object_list.append(call_data_object)
    else:
        '''
            fill in remaining required fields in call data objects from additional files
        '''
        '''
            match unique identifier btwn row and call data object
        '''
        call_data_object = [cdo for cdo in call_data_object_list 
        if cdo.idrssd == row[id_header_index_dict["IDRSSD"]]][0]
        '''
            collect required fields and fill in relevant object fields
        '''
        for key in field_header_index_dict:
            getattr(call_data_object, "field_dict")[call_data_field_dict[key]] = (
                row[field_header_index_dict[key]])

    return call_data_object_list

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

