import unittest
from unittest.mock import Mock
from CarDoctor import CarDoctor

#To-do
#refactor in general and figure out how to make global variables, add in __init__ constructor
#   https://stackoverflow.com/questions/37626662/get-yaml-key-value-in-python
#clean up the tests so that they are fixtures that just pass in different stuff instead of all different tests

class Test_Car_Doctor(unittest.TestCase):

    def setUp(self):
        self.mock = Mock()

    def test_get_check_wires_suggestion_for_104(self):
        expected_suggestion = 'Check for frayed wires or loose connections to your MAF sensor.'

        self.mock.CarDoctor.get_error_codes.return_value = [("P0104", "Mass or Volume Air Flow Circuit Intermittent")]
        mocked_dtc = self.mock.CarDoctor.get_error_codes()
        trimmed_error_code = CarDoctor.trim_dtc_code_to_four_digit_error_code(self, mocked_dtc)
        actual_suggestion = CarDoctor.retrieve_troubleshooting_suggestion(self, trimmed_error_code)
        self.assertEqual(expected_suggestion, actual_suggestion)

    def test_get_see_mechanic_suggestion_for_300(self):
        expected_suggestion = 'Your engine is misfiring. One or more of the cylinders is not working properly. See a mechanic.'

        error_300 = [("P0300", "Random/Multiple cylinder misfire detected.")]
        self.mock.CarDoctor.get_error_codes.return_value = error_300
        mocked_dtc = self.mock.CarDoctor.get_error_codes()
        trimmed_error_code = CarDoctor.trim_dtc_code_to_four_digit_error_code(self, mocked_dtc)
        actual_suggestion = CarDoctor.retrieve_troubleshooting_suggestion(self, trimmed_error_code)

        self.assertEqual(expected_suggestion, actual_suggestion)

    def test_get_gas_cap_suggestion_for_441(self):
        expected_suggestion = 'Try tightening your gas cap.'

        error_441 = [("P0441", "Evaporative Emission Control System Incorrect Purge Flow")]

        self.mock.CarDoctor.get_error_codes.return_value = error_441
        mocked_dtc = self.mock.CarDoctor.get_error_codes()
        trimmed_error_code = CarDoctor.trim_dtc_code_to_four_digit_error_code(self, mocked_dtc)
        actual_suggestion = CarDoctor.retrieve_troubleshooting_suggestion(self, trimmed_error_code)

        self.assertEqual(expected_suggestion, actual_suggestion)

    def test_trim_dtc_returns_four_digit_error_code(self):
        error_104 = [("P0104", "Mass or Volume Air Flow Circuit Intermittent")]

        expected = 'P0104'
        actual = CarDoctor.trim_dtc_code_to_four_digit_error_code(self, error_104)
        self.assertEqual(expected, actual)


    def test_yaml_file_can_be_read(self):
        expected_yaml_data = {'P0104': {'definition': 'Mass or Volume Air Flow Circuit Intermittent',
           'suggestion': 'Check for frayed wires or loose connections to your '
                         'MAF sensor.'},
 'P0300': {'definition': 'One or more of the cylinders is not working '
                         'properly. See a mechanic.',
           'suggestion': 'Your engine is misfiring. One or more of the '
                         'cylinders is not working properly. See a mechanic.'},
 'P0441': {'definition': 'Evaporative Emission Control System Incorrect Purge '
                         'Flow',
           'suggestion': 'Try tightening your gas cap.'}}

        actual_yaml_data = CarDoctor.retrieve_yaml_file(self)
        self.assertEqual(expected_yaml_data, actual_yaml_data)
