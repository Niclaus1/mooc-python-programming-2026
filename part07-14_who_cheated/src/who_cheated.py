# Write your solution here
import csv
from datetime import timedelta, datetime

def cheaters():
    threeHours = timedelta(hours=3)
    students = {}
    with open('start_times.csv') as start_file:
        for line in csv.reader(start_file, delimiter=';'):
            startTime = datetime.strptime(line[1],"%H:%M")
            students[line[0]] = startTime + threeHours 
    
    cheaterList = []
    with open('submissions.csv') as submission_file:
        for line in csv.reader(submission_file,delimiter=';'):
            endTime = datetime.strptime(line[3],"%H:%M") 
            if line[0] in students and endTime > students[line[0]]:
                print(line[0], endTime, students[line[0]])
                if line[0] not in cheaterList:
                    cheaterList.append(line[0])
    return cheaterList

if __name__ == "__main__":
    cheaters()