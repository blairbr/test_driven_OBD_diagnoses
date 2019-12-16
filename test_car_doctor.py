import unittest
from unittest.mock import Mock
from CarDoctor import CarDoctor

#To-do
#add suggestions for common error codes
#refactor in general
#clean up the tests so that they are fixtures that just pass in different stuff instead of all different tests
#   https://stackoverflow.com/questions/37626662/get-yaml-key-value-in-python

class Test_Car_Doctor(unittest.TestCase):

    def setUp(self):
        self.mock = Mock()

    def test_error_code_is_trimmed_correctly(self):
        expected = 'P0104'
        dtc = [("P0104", "Mass or Volume Air Flow Circuit Intermittent")]
        actual = CarDoctor.trim_dtc_code_to_four_digit_error_code(self, dtc)
        self.assertEqual(expected, actual)


    def test_get_check_wires_suggestion_for_104(self):
        expected_suggestion = 'Check for frayed wires or loose connections to your MAF sensor.'

        # self.mock.CarDoctor.get_error_codes.return_value = [("P0104", "Mass or Volume Air Flow Circuit Intermittent")]
        # mocked_dtc = self.mock.CarDoctor.get_error_codes()

        trimmed_error_code = 'P0104'
        actual_suggestion = CarDoctor.retrieve_troubleshooting_suggestion(self, trimmed_error_code)
        self.assertEqual(expected_suggestion, actual_suggestion)

    def test_get_see_mechanic_suggestion_for_300(self):
        expected_suggestion = 'Your engine is misfiring. One or more of the cylinders is not working properly. See a mechanic.'

        error_300 = [("P0300", "Random/Multiple cylinder misfire detected.")]
        trimmed_error_code = CarDoctor.trim_dtc_code_to_four_digit_error_code(self, error_300)
        actual_suggestion = CarDoctor.retrieve_troubleshooting_suggestion(self, trimmed_error_code)

        self.assertEqual(expected_suggestion, actual_suggestion)

    def test_get_gas_cap_suggestion_for_441(self):
        expected_suggestion = 'Try tightening your gas cap.'

        error_441 = [("P0441", "Evaporative Emission Control System Incorrect Purge Flow")]
        actual_suggestion = CarDoctor.retrieve_troubleshooting_suggestion(self, CarDoctor.trim_dtc_code_to_four_digit_error_code(self, error_441))

        self.assertEqual(expected_suggestion, actual_suggestion)

        #add a test for null values, empty strings, etc

    def test_unrecognized_code_returns_suggestion_not_found(self):
        expected_suggestion = 'Suggestion not found.'

        error_XYZ = [("P0XYZ", "Not A Real Error Code")]

        self.mock.CarDoctor.get_error_codes.return_value = error_XYZ
        mocked_dtc = self.mock.CarDoctor.get_error_codes()
        trimmed_error_code = CarDoctor.trim_dtc_code_to_four_digit_error_code(self, mocked_dtc)

        actual_suggestion = CarDoctor.retrieve_troubleshooting_suggestion(self, trimmed_error_code)

        self.assertEqual(expected_suggestion, actual_suggestion)

    def test_recognized_code_with_no_suggestion_in_yaml_returns_no_suggestion(self):
        expected_suggestion = 'Suggestion not found.'

        error_XYZ = [("P0NS0", "Testing When There's No Suggestion")]

        self.mock.CarDoctor.get_error_codes.return_value = error_XYZ
        mocked_dtc = self.mock.CarDoctor.get_error_codes()
        trimmed_error_code = CarDoctor.trim_dtc_code_to_four_digit_error_code(self, mocked_dtc)

        actual_suggestion = CarDoctor.retrieve_troubleshooting_suggestion(self, trimmed_error_code)

        self.assertEqual(expected_suggestion, actual_suggestion)

    def test_trim_dtc_returns_four_digit_error_code(self):
        error_104 = [("P0104", "Mass or Volume Air Flow Circuit Intermittent")]

        expected = 'P0104'
        actual = CarDoctor.trim_dtc_code_to_four_digit_error_code(self, error_104)
        self.assertEqual(expected, actual)