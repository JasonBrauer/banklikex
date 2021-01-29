import unittest
from entities.data_models import CallData

class TestValidateCallDataObjectList(unittest.TestCase):
    """
    Tests _grouped_files_by_year function
    """

    def test_with_good_values(self):
        from usecase.input_validation import validate_call_data_object_list

        good_call_data_object_list = [CallData(), CallData()]

        result = validate_call_data_object_list(good_call_data_object_list)

        self.assertEqual(good_call_data_object_list, result)

    def test_with_one_non_calldata_item(self):
        from usecase.input_validation import validate_call_data_object_list

        bad_call_data_object_list = [CallData(), 1]

        self.assertRaises(
            AssertionError,
            validate_call_data_object_list,
            bad_call_data_object_list
        )