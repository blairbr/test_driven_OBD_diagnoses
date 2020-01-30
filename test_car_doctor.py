import unittest
from unittest.mock import Mock
from CarDoctor import CarDoctor

#To-do
#add suggestions for common error codes
#refactor in general
#clean up the tests so that they are fixtures that just pass in different stuff instead of all different tests
#https://stackoverflow.com/questions/37626662/get-yaml-key-value-in-python

class Test_Car_Doctor(unittest.TestCase):

    def test_error_code_is_trimmed_correctly(self):
        expectedTrimmedCode = 'P0104'
        dtc = [("P0104", "Mass or Volume Air Flow Circuit Intermittent")]
        cd = CarDoctor()
        actualCodeReturned = cd.trim_dtc_code_to_four_digit_error_code(dtc)
        self.assertEqual(expectedTrimmedCode, actualCodeReturned)

    def test_get_check_wires_suggestion_for_104(self):
        cd = CarDoctor()
        expected_suggestion = 'Check for frayed wires or loose connections to your MAF sensor.'
        actual_suggestion = cd.retrieve_troubleshooting_suggestion('P0104')
        self.assertEqual(expected_suggestion, actual_suggestion)


    def test_get_see_mechanic_suggestion_for_300(self):
        cd = CarDoctor()
        expected_suggestion = 'Your engine is misfiring. One or more of the cylinders is not working properly. See a mechanic.'
        actual_suggestion = cd.retrieve_troubleshooting_suggestion('P0300')
        self.assertEqual(expected_suggestion, actual_suggestion)

    def test_get_gas_cap_suggestion_for_441(self):
        cd = CarDoctor()
        expected_suggestion = 'Try tightening your gas cap.'
        actual_suggestion = cd.retrieve_troubleshooting_suggestion('P0441')
        self.assertEqual(expected_suggestion, actual_suggestion)

    def test_trim_dtc_returns_four_digit_error_code(self):
        cd = CarDoctor()
        error_104 = [("P0104", "Mass or Volume Air Flow Circuit Intermittent")]
        actual = cd.trim_dtc_code_to_four_digit_error_code(error_104)
        self.assertEqual('P0104', actual)

    def test_unrecognized_code_returns_suggestion_not_found(self):
        cd = CarDoctor()
        expected_suggestion = 'Suggestion not found.'
        actual_suggestion = cd.retrieve_troubleshooting_suggestion('FAKEC0DE')
        self.assertEqual(expected_suggestion, actual_suggestion)

    def test_recognized_code_with_no_suggestion_in_yaml_returns_no_suggestion(self):
        cd = CarDoctor()
        expected_suggestion = 'Suggestion not found.'
        actual_suggestion = cd.retrieve_troubleshooting_suggestion('P0NS0')
        self.assertEqual(expected_suggestion, actual_suggestion)

        # TO-DO: add a test for null values, empty strings, etc