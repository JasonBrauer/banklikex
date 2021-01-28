import unittest

class TestGroupedFilesByYear(unittest.TestCase):
    """
    Tests _grouped_files_by_year function
    """

    '''
        TODO - write error handling tests
    '''

    def test_grouped_files_by_year_success(self):
        """
        Test the successful use of grouped files by year
        """

        from repo.tabular_files import _group_files_by_year

        test_file_list = [
            "FFIEC CDR Call Subset of Schedules 2020(1 of 2)",
            "FFIEC CDR Call Subset of Schedules 2020(2 of 2)",
            "FFIEC CDR Call Subset of Schedules 2019(1 of 2)",
            "FFIEC CDR Call Subset of Schedules 2019(2 of 2)",
        ]

        expected_output = [
            [
                "FFIEC CDR Call Subset of Schedules 2020(1 of 2)",
                "FFIEC CDR Call Subset of Schedules 2020(2 of 2)"
            ],
            [
                "FFIEC CDR Call Subset of Schedules 2019(1 of 2)",
                "FFIEC CDR Call Subset of Schedules 2019(2 of 2)"
            ]
        ]

        grouped_output = _group_files_by_year(test_file_list)

        self.assertEqual(grouped_output, expected_output)