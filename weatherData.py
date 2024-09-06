from datetime import date
from bs4 import BeautifulSoup
import requests

NUM_ROWS = 11

HIGH_OFFSET = 0
LOW_OFFSET = 1
MEAN_OFFSET = 2
monthMaxDay = 32

#earliest year of data collection
EARLIEST_YEAR = 2000

def dateIsValid(year, month):
    today = str(date.today())

    year = int(year)
    month = int(month)

    currMonth = int(today[5:-3])
    currYear = int(today[:4])
    
    if(month < 1 or month > 12):
        print("Month is not valid")
        return False
    elif(year < EARLIEST_YEAR or year > currYear):
        print("Year has no data")
        return False
    elif(year == currYear):
        if(month > currMonth):
            print("This month has yet to happen")
            return False
        
    return True



def updateData(year, month):
    url = "https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=28051&timeframe=2&StartYear=1840&EndYear=2024&Day=1&Year="+str(year)+"&Month=" + str(month) + "#"
    result = requests.get(url)

    doc = BeautifulSoup(result.text, "html.parser")
    
    global tags
    tags = doc.find_all("td")

    

    
def getInput():
    global month
    global year
    month = input("Enter month number: ")
    year = input("Enter year: ")
    while(dateIsValid(year, month) == False):
            month = input("Enter month number: ")
            year = input("Enter year: ")   
    
    updateData(year, month)
    
getInput()

def getAvg(offset):
    i = 0
    days = 0
    sum = 0
    
    while i <= monthMaxDay:
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
    #ok so star cycling through to find all da shit
    #start at year 2000
    currAvg = round(getAvg(MEAN_OFFSET),2)
    #if the year and month match the current, set max day to the current day
    #otherwise set it to 32
    today = str(date.today())

    currMonth = int(today[5:-3])
    currYear = int(today[:4])
    
    #this isnt gonna work at all cuz everytime i try to get data for a new month its gonna update
    if(currYear == int(year) and currMonth == int(month)):
        monthMaxDay = int(today[-2:])
        print("month max day is now: " + str(monthMaxDay))
    else:
        monthMaxDay = 32
        print("month max day is now: " + str(monthMaxDay))
        
    divisor = int(year) - EARLIEST_YEAR
    
    sum = 0
    
    
    maxYear = year
    
    i = EARLIEST_YEAR
    while i < int(maxYear):
        updateData(i, month)
        print("getting data for " +str(month)+"/"+str(i))
        newAvg = getAvg(MEAN_OFFSET)
        sum = sum + newAvg
        print("Sum is now: " + str(sum) + "\n")
        i = i + 1
        
    avg = round(sum/divisor, 2)
    
    if(currAvg < avg):
        print("With an average temperature of " + str(currAvg) + "°C, " + str(month)+"/"+str(year)+ " has been " + str(round((avg - currAvg),2)) + "°C cooler than usual.")
        
    elif(currAvg > avg):
        print("With an average temperature of " + str(currAvg) + "°C, " + str(month)+"/"+str(year)+ " has been " + str(round((currAvg - avg),2)) + "°C warmer than usual.")

    print("avg for the month over all is " + str(avg))
    print("Avg for this month is " + str(currAvg))
    
    monthMaxDay = 32
    
    
        
        

def getAvgTemp():
    avgTemp = getAvg(MEAN_OFFSET)
    print("Average temp for " + str(month) + "/" + str(year) + ": " + str(avgTemp) + "\n")

def getAvgHigh():
    avgHigh = getAvg(HIGH_OFFSET)
    print ("Average daily high for " + str(month) + "/" + str(year) + ": " + str(avgHigh) + "\n") 
    
def getAvgLow():
    avgLow = getAvg(LOW_OFFSET)
    print ("Average daily low for " + str(month) + "/" + str(year) + ": " + str(avgLow) + "\n") 




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
        compare()
        
    elif command == "5":
        
       getInput()
        
    else:
        print("exiting")
        exit()
