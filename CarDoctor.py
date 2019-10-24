import obd
import datetime
import logging
import yaml

class CarDoctor:

    def get_error_codes(self):
        connection = obd.OBD()
        dtc_codes = connection.query(obd.commands.GET_DTC)
        if dtc_codes:
            for dtc_code in dtc_codes:
                return dtc_code
        else:
            return 'no error codes found'

    def trim_dtc_code_to_four_digit_error_code(self, dtc):
        if dtc[0][0] is not None:
            return dtc[0][0]

    def print_timestamp(self):
        current_DT = datetime.datetime.now()
        return current_DT

    # note to self - fix this to the relative path so it'll work on other humans' machines
    def retrieve_troubleshooting_suggestion(self, error_code):
        with open(r'venv/error_codes_yaml.yaml') as yaml_file:
            doc = yaml.load(yaml_file, Loader=yaml.FullLoader)

        if error_code in doc:
            if doc[error_code]["suggestion"] is not None:
                suggestion = doc[error_code]["suggestion"]
        else:
            suggestion = "Suggestion not found."

        return suggestion

    def log_information(self):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.debug(self.dtc_codes)

    # note to self - fix this to the relative path so it'll work on other humans' machines
    def retrieve_yaml_file(self):
        with open(r'venv/error_codes_yaml.yaml') as file:
            error_codes_list = yaml.load(file, Loader=yaml.FullLoader)

            return error_codes_list
