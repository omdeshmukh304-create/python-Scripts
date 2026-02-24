import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1" # server URL (API)
# get server se read karne ke liye
# post server ko info dene ke liye
# delete to del info from server
response = requests.get(url=api_url)

#print(response) = agar code pura chal ta hai to print(response) output 200 dikhata hai

# print(dir(response)) = dir se sab use cases dikte hai

for key,value in response.json().items():
    if key == "userId":
        if value in [100,200,300]:
            print("User found")