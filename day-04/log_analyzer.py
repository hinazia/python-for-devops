import json

def count_log_analyzer(filename):

    file = open(filename, 'r', encoding="utf-8")
    log_file = open('log_summary.txt', 'w', encoding="utf-8")

    #print(dir(file))
    #log_data = file.readlines() ---- not needed for now because of strip() string modifier
    #inside try so that if file does not exist, "except block" can catch it grcaefully
    info_count = 0
    error_count = 0
    war_count = 0
    count = []

    try:
            for data in file:
                data = data.strip()
                if data == "":
                    continue

                if "INFO" in data:
                    info_count += 1
                
                elif "ERROR" in data:
                    error_count += 1
                

                elif "WARNING" in data:
                    war_count += 1

    except FileNotFoundError:
        print("File Not Found")

    print("Summary : ")
    log_file.write("Summary : \n")
    print(f"Total INFO Count = {info_count}\n")
    log_file.write(f"Total INFO Count = {info_count}\n")
    print(f"Total ERROR Count = {error_count}\n")
    log_file.write(f"Total ERROR Count = {error_count}\n")
    print(f"Total WARNING Count = {war_count}\n")
    log_file.write(f"Total WARNING Count = {war_count}\n")

    count.append({"log" : "INFO", "Count" : info_count})
    count.append({"log" : "ERROR", "Count" : error_count})
    count.append({"log" : "WARNING", "Count" : war_count})
                
    

    with open("log_analyzer.json", 'w') as file:
        json.dump(count, file, indent=4)

    file.close()
    log_file.close()

count_log_analyzer("app.log")
