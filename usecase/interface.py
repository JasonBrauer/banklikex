from repo.tabular_files import import_call_schedule_data

from usecase.analysis import (find_all_periods, average_all_periods, create_data_dict_list, 
create_distribution, find_similar_bank_field, find_similar_bank_intersection, 
call_data_idrssd_match)

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

def find_similar_banks(valid_idrssd, valid_call_data_object_list):
    """
    Finds a list of banks similar to the one provided via idrssd 
        Parameters
        ----------
        valid_idrssd: int
            validated bank unique idrssd
        valid_call_data_object_list: list
            validated list of call data objects

        Returns
        -------
        matching_agg_obj_list: AggregateCallData object
            list of aggregate call data objects for banks similar to provided bank

        Raises
        ------
    """
    unique_idrssd_list = find_distinct_idrssd(valid_call_data_object_list)

    period_agg_obj_list = []
    for idrssd in unique_idrssd_list:
        grouped_by_idrssd = find_all_periods(valid_call_data_object_list, idrssd)
        average_call_data = average_all_periods(grouped_by_idrssd)
        period_agg_obj_list.append(average_call_data)

    data_dict_list = create_data_dict_list(period_agg_obj_list)

    for field in data_dict_list:
        ecdf = create_distribution(data_dict_list, field)
        find_similar_bank_field(valid_idrssd, period_agg_obj_list, ecdf, field)

    matching_agg_obj_list = find_similar_bank_intersection(period_agg_obj_list)

    return matching_agg_obj_list

def idrssd_to_bank_name(valid_idrssd, valid_call_data_object_list):
    """
        Looks up a bank name via call data object list for provided idrssd

        Parameters
        ----------
        valid_idrssd: int
            validated bank unique idrssd
        valid_call_data_object_list: list
            validated list of call data objects

        Returns
        -------
        matching_bank_name: str
            bank name associated with provided idrssd

        Raises
        ------
    """
    matched_call_data_obj = call_data_idrssd_match(valid_idrssd, valid_call_data_object_list)
    
    return matched_call_data_obj.bank_name

def load_overall_distributions(valid_call_data_object_list):
    """
        Loads cumulative distributions and histograms of bank field data used for bank comparisons.
        Bank field data is averaged across all unique periods in the dataset for each bank

        Parameters
        ----------
        valid_call_data_object_list: list
            validated list of call data objects

        Returns
        -------
        data_dict_list: dict
            keys are fields and values are lists of aggregate call data objects
        ecdf_obj_dict: dict
            keys are fields and values are ecdf objects for each field

        Raises
        ------
    """
    unique_idrssd_list = find_distinct_idrssd(call_data_object_list)

    period_agg_obj_list = []
    for idrssd in unique_idrssd_list:
        grouped_by_idrssd = find_all_periods(call_data_object_list, idrssd)
        average_call_data = average_all_periods(grouped_by_idrssd)
        period_agg_obj_list.append(average_call_data)

    data_dict_list = create_data_dict_list(period_agg_obj_list)

    ecdf_obj_dict = {}
    for field in data_dict_list:
        ecdf_obj_dict[field] = create_distribution(data_dict_list, field)

    return data_dict_list, ecdf_obj_dict


    
    





