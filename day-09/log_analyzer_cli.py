# Day 05 - Log Analyzer (Sample File For your Reference)
import argparse
import json

class LogAnalyzer:
    def __init__(self, log_file):
        """
        __init__ function runs first and initializes
        the values into class variables.
        """
        self.log_file = log_file
        self.counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "UNKNOWN": 0}

    def read_logs(self):
        """
        Function to read logs from the given log file
        """
        try:
            with open(self.log_file, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            print("Log file not found:", self.log_file)
            return []

    def analyze(self, lines):
        """
        Analyzer to count the error patterns & Counts
        """
        for line in lines:
            if "INFO" in line:
                self.counts["INFO"] += 1
            elif "WARNING" in line:
                self.counts["WARNING"] += 1
            elif "ERROR" in line:
                self.counts["ERROR"] += 1
            else:
                self.counts["UNKNOWN"] += 1

        return self.counts


def main(filename):
    """
    Main Function as a single entrypoint to the program
    """
    analyzer = LogAnalyzer(filename)
    lines = analyzer.read_logs()

    if not lines:
        print("No logs to analyze.")
        return

    result = analyzer.analyze(lines)
    

    print("Log Analysis Summary:")
    for level, count in result.items():
        print(f"{level}: {count}")

    return result

def write_json(output_file, log_count):
    with open(output_file, "w+") as file:
        json.dump(log_count, file, indent=4)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help="Log file path")
    parser.add_argument('--out', required=True, help="Output file Name")
    parser.add_argument('--level', help="Input Level")
    args = parser.parse_args()
    log_count = main(args.file)

    if args.level == "WARNING":
        print(log_count["WARNING"])

    write_json(args.out,log_count)
