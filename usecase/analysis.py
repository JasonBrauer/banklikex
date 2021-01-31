from statsmodels.distributions.empirical_distribution import ECDF

from entities.data_models import AggregateCallData

def find_all_periods(call_data_object_list, idrssd):
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
    grouped_cdo_idrssd = []
    '''
        split call data object list into multiple lists separated by period
    '''
    period_call_data_object_dict = _split_by_period(call_data_object_list)
    '''
        search for matching idrssd in each list
    '''
    for period in period_call_data_object_dict:
        obj_match = _call_data_idrssd_match(idrssd, period_call_data_object_dict[period])
        if obj_match is not None:
            grouped_cdo_idrssd.append(obj_match)

    return grouped_cdo_idrssd

def _split_by_period(call_data_object_list):
    """
    Splits call data object list into separate lists by period
        
        Parameters
        ----------
        call_data_object_list: list
            list of call data objects

        Returns
        -------
        period_call_data_object_dict: 
            dict of call data object lists grouped by period

        Raises
        ------
    """
    period_call_data_object_dict = {}
    period_start = call_data_object_list[0].period
    for obj in call_data_object_list:
        if obj.period not in period_call_data_object_dict.keys():
            period_call_data_object_dict[obj.period] = [obj]
        else:
            period_call_data_object_dict[obj.period].append(obj)

    return period_call_data_object_dict

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

def average_all_periods(call_data_object_list):
    """
    Averages data from all periods for each field in call data object list

        Parameters
        ----------
        call_data_object_list: list
            list of call data objects from different periods with a common idrssd

        Returns
        -------
        average_call_data: AggregateCallData
            aggregate call data object with field values of all periods in provided list averaged

        Raises
        ------
    """
    average_call_data = AggregateCallData()

    average_call_data.aggregation = "average"
    average_call_data.idrssd = call_data_object_list[0].idrssd

    avg_dict = {}
    for obj in call_data_object_list:
        for field in obj.field_dict:
            if obj.field_dict[field] is not None:
                if field not in avg_dict:
                    avg_dict[field] = [obj.field_dict[field]]
                else:
                    avg_dict[field].append(obj.field_dict[field])
    
    for field in avg_dict:
        avg_dict[field] = sum(avg_dict[field]) / len(avg_dict[field])
    
    average_call_data.field_dict = avg_dict

    return average_call_data

def create_distribution(data_dict_list, field):
    """
    Calculates the distribution from the aggregate objects for the specified field

        Parameters
        ----------
        data_dict_list: list
            each key in dict is a field and each value is list of values from all input agg objects
        field: string
            field that will have a distribution created

        Returns
        -------
        ecdf: ECDF object
            statsmodels ECDF object

        Raises
        ------
    """
    ecdf = ECDF(data_dict_list[field])

    return ecdf

def create_data_dict_list(period_agg_object_list):
    """
    Creates a dictionary where each key is a field from the provided aggregate objects and values
    are a list of all provided aggregate object's values for the respective field

        Parameters
        ----------
        period_agg_object_list: list
            list of call data aggregate objects with fields averaged across all periods in dataset

        Returns
        -------
        data_dict_list: list
            each key in dict is a field and each value is list of values from all input agg objects

        Raises
        ------
    """
    data_dict_list = {}
    for obj in period_agg_object_list:
        for field in obj.field_dict:
            if field not in data_dict_list:
                data_dict_list[field] = [obj.field_dict[field]]
            else:
                data_dict_list[field].append(obj.field_dict[field])
    
    return data_dict_list

def find_similar_bank_field(input_bank_idrssd, period_agg_object_list, ecdf_obj, field):
    """
    Flips the intersection dict value for each item in provided agg obj list to true for specified 
    field if field value within +- 10 percentile of the input bank field value

        Parameters
        ----------
        input_bank_idrssd: int
            idrssd of bank specified for finding similar banks
        period_agg_object_list: list
            list of call data aggregate objects with fields averaged across all periods in dataset
        ecdf_obj: ECDF object
            statsmodels ECDF object build from agg data of input field
        field: str
            field that will be used for interection comparison

        Returns
        -------
        period_agg_object_list: list
            list of call data aggregate objects with intersection field modified

        Raises
        ------
    """
    pass