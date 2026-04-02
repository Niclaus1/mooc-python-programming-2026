# Write your solution here
from datetime import datetime,timedelta

def screen_time():
    try:
        filename = input("Filename:")
        dateInput = input("Starting date:")
        manyDays = int(input("How many days:"))
    except ValueError:
        print("Incorrect Inputs")
        
    startDate = datetime.strptime(dateInput,"%d.%m.%Y")
    totalMinutes = 0
    dateList = []
    print("Please type in screen time in minutes on each day (TV computer mobile): ")
    for i in range(manyDays):
        iDate = timedelta(days=i)
        nextDate = startDate + iDate
        try:
            screenTime = input(f"Screen time {nextDate.strftime("%d.%m.%Y")}:")
        except ValueError:
            screenTime = "0 0 0"
            
        minuteParts = screenTime.split()
        dateList.append(f"{nextDate.strftime('%d.%m.%Y')}: {minuteParts[0]}/{minuteParts[1]}/{minuteParts[2]}")
        totalMinutes += (int(minuteParts[0]) + int(minuteParts[1]) + int(minuteParts[2]))
    
    avgMinutes = totalMinutes / manyDays
    with open(filename, 'w') as new_file:
        new_file.write(f"Time period: {startDate.strftime('%d.%m.%Y')}-{dateList[-1][0:10]}\n")
        new_file.write(f"Total minutes: {totalMinutes}\n")
        new_file.write(f"Average minutes: {avgMinutes}\n")
        for date in dateList:
            new_file.write(f"{date}\n")

screen_time()