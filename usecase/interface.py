from repo.tabular_files import import_call_schedule_data

def load_call_data(valid_directory):
    """
    Retrieves a list of call data objects
        Parameters
        ----------
        valid_directory: str
            a validated directory

        Returns
        -------
        call_data_object_dict: dict
            dict of call data objects grouped by year

        Raises
        ------
    """
    call_data_obj_dict = import_call_schedule_data(valid_directory)

    return call_data_obj_dict

