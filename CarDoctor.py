import obd
import datetime
import logging
import yaml
import time
from OBD2_codes import OBD2_codes


class CarDoctor:


    # def format_yaml(self):
    #     data = 'P0016: Crankshaft Position - Camshaft Position Correlation  P0017: Crankshaft  Position - Camshaft    Position   Correlation'
    #     newYaml = data.replace(": ", ": suggestion: ")
    #     return newYaml

    def get_error_codes(self):  #try catch?
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

    # note to self - probs should rework this to a try/exception eventually
    def retrieve_troubleshooting_suggestion(self, error_code):
        with open(r'venv/error_codes_yaml.yaml') as yaml_file:
            doc = yaml.load(yaml_file, Loader=yaml.FullLoader)

        suggestion = "Suggestion not found."

        if error_code in doc and 'suggestion' in doc[error_code]:
            suggestion = doc[error_code].get('suggestion')

        return suggestion

    def log_information(self):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.debug(self.dtc_codes)

    def retrieve_yaml_file(self):
        with open(r'venv/error_codes_yaml.yaml') as file:
            error_codes_list = yaml.load(file, Loader=yaml.FullLoader)

            return error_codes_list

    def write_to_yaml_file(self):
        with open(r'venv/error_codes.yaml', 'w') as file:
            documents = yaml.dump(OBD2_codes.pcodes, file)

def main():
    five_minutes = 300
    while(True):
        print("The Car Doc is in the office")
        cd = CarDoctor()
        error_code = cd.get_error_codes()
        trimmed_error_code = cd.trim_dtc_code_to_four_digit_error_code(error_code)
        suggestion = cd.retrieve_troubleshooting_suggestion(trimmed_error_code)
        print(suggestion)
        time.sleep(five_minutes)

        #check for nulls and stuff
        #check if there is ever more than 1

if __name__ == "__main__":
    main()
