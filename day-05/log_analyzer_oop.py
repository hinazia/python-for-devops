import json
import pdb

class LogAnalyzer:

    def __init__(self, filename, output_file): #constructor
        self.filename = filename
        self.output_file = output_file


    def read_log(self):
        try:
            with open(self.filename, 'r') as log_file:
                return log_file.readlines()
        except FileNotFoundError:
            print("File Not Found")

    def write_json(self, log_count):
        with open(self.output_file, 'w') as file:
            json.dump(log_count, file, indent=4)

    def analyze(self):

        log_count = {"INFO" : 0, "ERROR" : 0, "WARNING" : 0}

        log_lines = self.read_log()

        for line in log_lines:

            if line == "":
                continue

            if "INFO" in line:
                
                log_count["INFO"] += 1

            elif "ERROR" in line:
                log_count["ERROR"] += 1

            elif "WARNING" in line:
                log_count["WARNING"] += 1
            else:
                pass
        
        self.write_json(log_count)


log_obj1 = LogAnalyzer("app.log", "output_json")
#print(log_obj1.filename)
log_count = log_obj1.analyze()
