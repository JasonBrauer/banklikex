import unittest
from unittest.mock import patch

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

class TestValidateDirectory(unittest.TestCase):
    """
    Tests _grouped_files_by_year function
    """

    @patch("usecase.input_validation.os.path.isdir")
    def test_valid_directory(self, mock_isdir):
        from usecase.input_validation import validate_directory

        mock_isdir.return_value = True
        test_dir = ".\\some\\directory"

        result = validate_directory(test_dir)

        self.assertEqual(test_dir, result)
        mock_isdir.assert_called_once_with(test_dir)


