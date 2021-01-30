from repo.tabular_files import import_call_schedule_data

def load_call_data(valid_directory):
    """
    Retrieves a list of call data objects
        Parameters
        ----------
        valid_directory: str
            validated directory

        Returns
        -------
        call_data_object_dict: dict
            dict of call data objects grouped by year

        Raises
        ------
    """
    call_data_obj_dict = import_call_schedule_data(valid_directory)

    return call_data_obj_dict

def find_distinct_idrssd(valid_call_data_object_list):
    """
    Determines a list of distinct idrssd values in the call data object dataset
        Parameters
        ----------
        valid_call_data_object_list: list
            validated list of call data objects

        Returns
        -------
        distinct_idrssd_list: 
            list of unique idrssd values in dataset

        Raises
        ------
    """
    distinct_idrssd_list = []
    first_period = valid_call_data_object_list[0].period
    '''
        assumes every period has the same set of idrssd values
        TODO - its doesn't appear to be the case that all periods contain the same idrssd values,
        so a few may be skipped with this method. Ideally all periods would be searched and a 
        unique list developed after comparing the differences
    '''
    for data_obj in valid_call_data_object_list:
        if data_obj.period != first_period:
            break
        distinct_idrssd_list.append(data_obj.idrssd)

    return distinct_idrssd_list




