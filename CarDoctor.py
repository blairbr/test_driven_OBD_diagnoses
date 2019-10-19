import obd
import datetime
import logging
import yaml

class CarDoctor:
    # obd.commands.FREEZE_DTC



        error_104 = [("P0104", "Mass or Volume Air Flow Circuit Intermittent")]
        error_441 = [("P0441", "Try tightening your gas cap.")]
        error_300 = [("P0300", "Random/Multiple cylinder misfire detected.")]
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

            error_codes = {
                "P0104": {
                    "definition": "Mass or Volume Air Flow Circuit Intermittent",
                    "suggestion": "Check for frayed wires or loose connections to your MAF sensor."
                },
                "P0441": {
                    "definition": "Evaporative Emission Control System Incorrect Purge Flow",
                    "suggestion": "Try tightening your gas cap."
                },
                "P0300": {
                    "definition": "One or more of the cylinders is not working properly. See a mechanic.",
                    "suggestion": "Your engine is misfiring. One or more of the cylinders is not working properly. See a mechanic."
                }
            }
            return error_codes.get(errorcode[0][0]).get('suggestion')


        def log_information(self):
            logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
            logging.debug(self.dtc_codes)

        def print_yaml_file(self):
            with open(r'C:\Users\Blair\Projects\PythonProjects\CarDoctorFolder\test_driven_OBD_diagnoses\venv\error_codes.yaml') as file:
                # The FullLoader parameter handles the conversion from YAML
                # scalar values to Python the dictionary format
                error_codes_list = yaml.load(file, Loader=yaml.FullLoader)

                return error_codes_list
            #Future steps:
            #make the error codes dictionary a global variable
            #move it into a yaml file




