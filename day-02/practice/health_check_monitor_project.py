import requests

file = open("report.txt", "w")

websites_list = [
    "https://google.com",
    "https://github.com",
    "https://stackoverflow.com",
    "https://example.invalid"
]

up_count = 0
down_count = 0

def handle_down(url, down_count):
    down_count += 1
    print(f"Status{url} : DOWN, response time in seconds : {response.elapsed.total_seconds()}")
    if down_count == 3:
            print(f"Alert : {url} is down three times now")
    return down_count

for url in websites_list:
    try:
        response = requests.get(url = url)
         
        print(f"Checking : {url}")
        if response.status_code == 200:
            print(f"Status : UP, response time in seconds : {response.elapsed.total_seconds()}\n") #elapsed object is used to measure the response time
            up_count += 1   
            file.write(f"{url} is UP \n")         
        else:
           count = handle_down(url, down_count)

    except (requests.exceptions.ConnectionError, 
    requests.exceptions.Timeout, 
    requests.exceptions.RequestException) as e:
        #print(f"error : {e}")
        count = handle_down(url, down_count)
    
print("Summary : ")
file.write("Summary : ")
print(f"{up_count} websites are running")
file.write(f"{up_count} websites are running\n")
print(f"{count} websites are Down")
file.write(f"{count} websites are down\n")

file.close()



