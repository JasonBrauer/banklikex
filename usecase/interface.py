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
            dict of call data objects grouped by year

        Raises
        ------
    """
    distinct_idrssd_list = []
    first_period = valid_call_data_object_list[0].period
    '''
        periods all grouped together in dataset and every period has the same set of idrssd values
    '''
    for data_obj in valid_call_data_object_list:
        if data_obj.period != first_period:
            break
        distinct_idrssd_list.append(data_obj.idrssd)

    return distinct_idrssd_list

def _find_all_periods(call_data_object_list, idrssd):
    """
    Collect all call data objects with common idrssd into single list
        
        Parameters
        ----------
        call_data_object_list: list
            list of call data objects

        Returns
        -------
        call_data_object_list: 
            list of call data object associated with input idrssd

        Raises
        ------
    """

def _call_data_idrssd_match(idrssd, call_data_object_list):
    """
    Finds the call data object with idrssd that matches the current row idrssd

        Parameters
        ----------
        idrssd: int
            idrssd value
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
        if idrssd > call_data_idrssd_list[mid_index]:
            call_data_idrssd_list = call_data_idrssd_list[(mid_index + 1):]
            call_data_index_list = call_data_index_list[(mid_index + 1):]
        else:
            call_data_idrssd_list = call_data_idrssd_list[:(mid_index + 1)]
            call_data_index_list = call_data_index_list[:(mid_index + 1)]

        call_data_length = len(call_data_idrssd_list)
    else:
        if idrssd == call_data_idrssd_list[0]:
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
        


