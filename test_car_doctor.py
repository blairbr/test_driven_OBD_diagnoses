import unittest
from unittest.mock import Mock
from CarDoctor import CarDoctor


class Test_Car_Doctor(unittest.TestCase):
    error_104 = ("P0104", "Mass or Volume Air Flow Circuit Intermittent")

    def test_get_check_wires_suggestion_for_104(self):
        expected_suggestion = 'Check for frayed wires or loose connections to your MAF sensor.'

        # here need to mock out the call and tell it to get a specific code back??

        mock = Mock()
        mock.CarDoctor.get_error_codes.return_value = [("P0104", "Mass or Volume Air Flow Circuit Intermittent")]
        mocked_error_code = mock.CarDoctor.get_error_codes()

        actual_suggestion = CarDoctor.append_troubleshooting_suggestion(self, mocked_error_code)
        self.assertEqual(expected_suggestion, actual_suggestion)


    def test_get_see_mechanic_suggestion_for_300to305(self):
        expected_suggestion = 'Your engine is misfiring. One or more of the cylinders is not working properly. See a mechanic.'

        error_300 = [("P0300", "Random/Multiple cylinder misfire detected.")]

        mock = Mock()
        mock.CarDoctor.get_error_codes.return_value = error_300
        mocked_error_code = mock.CarDoctor.get_error_codes()
        actual_suggestion = CarDoctor.append_troubleshooting_suggestion(self, mocked_error_code)

        self.assertEqual(expected_suggestion, actual_suggestion)

    def test_get_gas_cap_suggestion_for_441(self):
        expected_suggestion = 'Try tightening your gas cap.'

        error_441 = [("P0441", "Evaporative Emission Control System Incorrect Purge Flow")]

        mock = Mock()
        mock.CarDoctor.get_error_codes.return_value = error_441
        mocked_error_code = mock.CarDoctor.get_error_codes()
        actual_suggestion = CarDoctor.append_troubleshooting_suggestion(self, mocked_error_code)

        self.assertEqual(expected_suggestion, actual_suggestion)