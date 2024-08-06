
from bs4 import BeautifulSoup
import requests
#this is a test
month = input("Enter month number: ")

year = input("Enter year: ")

url = "https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=28051&timeframe=2&StartYear=1840&EndYear=2024&Day=1&Year="+str(year)+"&Month=" + str(month) + "#"

result = requests.get(url)

#with open("/Users/williamgore/Documents/test.html", "r") as f:
doc = BeautifulSoup(result.text, "html.parser")

tags = doc.find_all("td") 


def getAvgHigh():
    i = 0
    days = 0
    sum = 0
    while i<33:
        if tags[i*11].string == u'\xa0' :
            break
        try:
            sum = sum + float(tags[i * 11].string)
            days = days + 1
        except:
            print("Missing some data\n")
        i = i + 1
    print("heres the sum: " + str(sum))
    print("Days with data collected: " + str(days))
    print("Missing data for " + str(i-days) + " days.")
    print ("Average daily high for " + str(month) + "/" + str(year) + ": " + str(sum/days) + "\n") 
    
def getAvgLow():
    i = 0
    sum = 0
    days = 0
    while i<33:
        if tags[i*11 + 1].string == u'\xa0' :
            break
        try:
            sum = sum + float(tags[i * 11 + 1].string)
            days = days + 1
        except:
            print("Missing some data\n")
        i = i + 1
    print("heres the sum: " + str(sum))
    print("Days with data collected: " + str(days))
    print("Missing data for " + str(i-days) + " days.")
    print ("Average daily low for " + str(month) + "/" + str(year) + ": " + str(sum/days) + "\n") 


print("\n")

getAvgHigh()

print("###########################################\n")

getAvgLow()
