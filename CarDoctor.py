import obd
import datetime
import logging
import requests

class CarDoctor:
    # obd.commands.FREEZE_DTC
        error_codes = {
            "P0104":  {
                "definition": "Mass or Volume Air Flow Circuit Intermittent",
                "suggestion": "Check for frayed wires or loose connections to your MAF sensor."
            },
            "P0441":  {
                "definition": "Evaporative Emission Control System Incorrect Purge Flow",
                "suggestion": "Try tightening your gas cap."
            },
            "P0300": {
                "definition": "One or more of the cylinders is not working properly. See a mechanic.",
                "suggestion": "Try tightening your gas cap."
            }
        }


        error_104 = ("P0104", "Mass or Volume Air Flow Circuit Intermittent")
        error_441 = ("P0441", "Try tightening your gas cap.")  # was this an array??
        error_300 = ("P0300", "Random/Multiple cylinder misfire detected.")
        def get_error_codes(self):
            connection = obd.OBD()
            dtc_codes = connection.query(obd.commands.GET_DTC)
            if dtc_codes:
                for dtc_code in dtc_codes:
                    return dtc_code
            else:
                return 'no error codes found'

        def print_timestamp(self):
            current_DT = datetime.datetime.now()
            return current_DT

        def append_troubleshooting_suggestion(self, errorcode):
            if errorcode == ("P0300", "Random/Multiple cylinder misfire detected."):
                return 'One or more of the cylinders is not working properly. See a mechanic.'
            elif errorcode == ("P0441", "Evaporative Emission Control System Incorrect Purge Flow"):
                return 'Try tightening your gas cap'
            elif errorcode == ("P0104", "Mass or Volume Air Flow Circuit Intermittent"):
                return 'Check for frayed wires or loose connections to your MAF sensor.'
            else:
                return 'Unrecognized code. No suggestions for you yet'


        def log_information(self):
            logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
            logging.debug(self.dtc_codes)




