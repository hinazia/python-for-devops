import json

def read_log(filename):
    try:
        with open(filename, 'r') as log_file:
            return log_file.readlines()
    except FileNotFoundError:
        print("File Not Found")

log_count = {"INFO" : 0, "ERROR" : 0, "WARNING" : 0}

def analyze(log_lines):
    
    for line in log_lines:

        if line == "":
            continue

        if "INFO" in line:
            #log_count.update({"INFO" : log_count["INFO"]+1})
            log_count["INFO"] += 1

        elif "ERROR" in line:
            log_count["ERROR"] += 1

        elif "WARNING" in line:
            log_count["WARNING"] += 1
        else:
            pass
    
    return log_count

def write_json():
    with open("log_analyzer.json", 'w') as file:
        json.dump(log_count, file, indent=4)

def write_txt():
    with open("log_summary.txt", 'w') as file:
        file.write(f"{log_count}")


lines = read_log("app.log")
analyze(lines)
print(log_count)
write_json()
write_txt()

