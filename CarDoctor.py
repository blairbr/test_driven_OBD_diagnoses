import obd
import datetime
import logging
import requests

class CarDoctor:
        # def __init__(self):
        #     pass

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
            if 299 < errorcode < 305:
                return 'Your engine is misfiring. One or more of the cylinders is not working properly. See a mechanic.'
            elif errorcode is 441:
                return 'Try tightening your gas cap'
            else:
                return 'Unrecognized code. No suggestions for you yet'


        def log_information(self):
            logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
            logging.debug(self.dtc_codes)



