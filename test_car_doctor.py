import unittest
from unittest.mock import Mock
from CarDoctor import CarDoctor


class Test_Car_Doctor(unittest.TestCase):

    def test_get_gas_cap_suggestion_for_441(self):
        expected_suggestion = 'Try tightening your gas cap'
        # here need to mock out the call and tell it to get a specific code back
        errorcode = CarDoctor.get_error_codes()
#here i'd mock the response from get error codes
        actual_suggestion = CarDoctor.append_troubleshooting_suggestion(self, errorcode)
        self.assertEqual(expected_suggestion, actual_suggestion)


    def test_get_see_mechanic_suggestion_for_300to305(self):
        expected_suggestion = 'Your engine is misfiring. One or more of the cylinders is not working properly. See a mechanic.'

        errorcode = CarDoctor.get_error_codes();
        actual_suggestion = CarDoctor.append_troubleshooting_suggestion(self, errorcode)

        self.assertEqual(expected_suggestion, actual_suggestion)