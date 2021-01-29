from entities.data_models import CallData

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
    """
    assert type(call_data_object_list) == list, "call_data_object_list must be a list"
    for obj in call_data_object_list:
        assert type(obj) == CallData, "each item in call_data_object_list must be a CallData object"
    
    return call_data_object_list