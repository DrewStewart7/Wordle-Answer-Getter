import requests
year = int(input("Which year would you like?(ex:2022) "))
x= int(input("Which day of the month would you like?(ex:1) "))
m = int(input("Which month would you like?(ex:11) "))

url = "https://www.nytimes.com/svc/wordle/v2/" + str(year) + "-"
yurl = url + str(m).zfill(2) + "-"
    
    
  
murl = yurl + f"{str(x).zfill(2)}.json"
req = requests.get(murl)
req = req.json()
try:
    print("\nDate: " + req["print_date"])
    print("Solution: " + req["solution"])
except:
    print("\nInvalid Date")
    
