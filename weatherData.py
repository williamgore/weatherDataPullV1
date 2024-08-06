from bs4 import BeautifulSoup
import requests

month = input("Enter month number: ")

year = input("Enter year: ")

NUM_ROWS = 11

HIGH_OFFSET = 0
LOW_OFFSET = 1

url = "https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=28051&timeframe=2&StartYear=1840&EndYear=2024&Day=1&Year="+str(year)+"&Month=" + str(month) + "#"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

tags = doc.find_all("td") 

#add month and year parameters
#wait would that even work

def getAvg(offset):
    i = 0
    days = 0
    sum = 0
    while i<33:
        if tags[i*NUM_ROWS + offset].string == u'\xa0' :
            break
        try:
            sum = sum + float(tags[i * NUM_ROWS + offset].string)
            days = days + 1
        except:
            print("Missing some data\n")
        i = i + 1
    print("heres the sum: " + str(sum))
    print("Days with data collected: " + str(days))
    print("Missing data for " + str(i-days) + " days.")
    return sum/days

def getAvgHigh():
    avgHigh = getAvg(HIGH_OFFSET)
    print ("Average daily high for " + str(month) + "/" + str(year) + ": " + str(avgHigh) + "\n") 
    
def getAvgLow():
    avgLow = getAvg(LOW_OFFSET)
    print ("Average daily low for " + str(month) + "/" + str(year) + ": " + str(avgLow) + "\n") 


print("\n")

getAvgHigh()

print("###########################################\n")

getAvgLow()
