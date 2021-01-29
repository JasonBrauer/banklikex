from entities.data_models import CallData
import os

def validate_call_data_object_list(call_data_object_list):
    """
    Validates that a call data object list contains the appropriate values and types
        Parameters
        ----------
        call_data_object_list: list
            list of call data objects

        Returns
        -------
        call_data_object_list: list
            validated list of call data objects

        Raises
        ------
        AssertionError: AssertionError
            if not a list and items in list are not CallData objects
    """
    assert type(call_data_object_list) == list, "call_data_object_list must be a list"
    for obj in call_data_object_list:
        assert type(obj) == CallData, "each item in call_data_object_list must be a CallData object"
    
    return call_data_object_list


def validate_directory(directory):
    """
    Validates that a directory is available
        Parameters
        ----------
        directory: str
            path to a directory

        Returns
        -------
        directory: list
            validated path to a directory

        Raises
        ------
        AssertionError: AssertionError
            if provided directory is not valid on the system
    """
    assert os.path.isdir(directory), "not a valid or available directory"

    return directory