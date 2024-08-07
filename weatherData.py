from datetime import date
from bs4 import BeautifulSoup
import requests




NUM_ROWS = 11

HIGH_OFFSET = 0
LOW_OFFSET = 1
MEAN_OFFSET = 2

EARLIEST_YEAR = 2000


def updateData(year, month):
    url = "https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=28051&timeframe=2&StartYear=1840&EndYear=2024&Day=1&Year="+str(year)+"&Month=" + str(month) + "#"
    result = requests.get(url)
    #result = requests.get(url)

    doc = BeautifulSoup(result.text, "html.parser")
    #doc = BeautifulSoup(result.text, "html.parser")

    return doc.find_all("td") 
    #tags = doc.find_all("td") 
    

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
    print("Days with data collected: " + str(days))
    print("Missing data for " + str(i-days) + " days.")
    return sum/days

#ok so we're gonna start planning a compare function to compare maybe two months or a
#specific month to the average for that month of all time

#so get the month we want to look at first
# if the month isn't yet over, only look at the days that have passed for all prev months
#for example if its august 6th, when comparing to previous augusts, only take the average of
#the first 5 days
#get the current date, specifically the year AND day
#for each year, get the average temperature for that month
#take the average of all the months
#compare to the average temperature of the current month
#this function will also make use of the getAvg function and will require a helper function
#called get avgTemp
#start at the earliest year, make your way up to the latest year

def compare():
    #YYYY-MM-DD
    today = date.today()
    print(today)

def getAvgTemp():
    avgTemp = getAvg(MEAN_OFFSET)
    print("Average temp for " + str(month) + "/" + str(year) + ": " + str(avgTemp) + "\n")

def getAvgHigh():
    avgHigh = getAvg(HIGH_OFFSET)
    print ("Average daily high for " + str(month) + "/" + str(year) + ": " + str(avgHigh) + "\n") 
    
def getAvgLow():
    avgLow = getAvg(LOW_OFFSET)
    print ("Average daily low for " + str(month) + "/" + str(year) + ": " + str(avgLow) + "\n") 


month = input("Enter month number: ")

year = input("Enter year: ")

tags = updateData(year, month)

while 1:
    command = input("Select a function: \n"
                        + "1 - Get Average High\n"
                        + "2 - Get Average Low\n"
                        + "3 - Get Average Temp\n"
                        + "4 - Compare\n"
                        + "5 - Get new month\n"
                        + "X - Exit\n")

    print("\n")

    if command == "1":
        getAvgHigh()
        
    elif command == "2":
        getAvgLow()
        
    elif command == "3":
        getAvgTemp()
        
    elif command == "4":
        print("WIP")
        
    elif command == "5":
        month = input("Enter month number: ")
        year = input("Enter year: ")
        tags = updateData(year, month)
        
    else:
        print("exiting")
        exit()

today = date.today()
print(today)
