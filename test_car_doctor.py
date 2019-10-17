import unittest
from unittest.mock import Mock
from CarDoctor import CarDoctor


class Test_Car_Doctor(unittest.TestCase):

    def __init__(self):
        self.doc = CarDoctor()

    def test_get_gas_cap_suggestion_for_441(self):
        expected_suggestion = 'Try tightening your gas cap'
        actual_suggestion = self.doc.append_troubleshooting_suggestion(self)

        self.assertEqual(expected_suggestion, actual_suggestion)

    def test_get_gas_cap_suggestion_for_441(self):
        expected_suggestion = 'Try tightening your gas cap'
        actual_suggestion = self.doc.append_troubleshooting_suggestion(self)

        self.assertEqual(expected_suggestion, actual_suggestion)


    def test_get_see_mechanic_suggestion_for_300to305(self):
        expected_suggestion = 'Your engine is misfiring. One or more of the cylinders is not working properly. See a mechanic.'
        actual_suggestion = self.doc.append_troubleshooting_suggestion(self);
        self.assertEqual(expected_suggestion, actual_suggestion)