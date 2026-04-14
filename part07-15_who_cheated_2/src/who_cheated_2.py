# Write your solution here
import csv
from datetime import timedelta, datetime

def start_time():
    students = {}
    with open('start_times.csv') as start_file:
        for line in csv.reader(start_file, delimiter=';'):
            startTime = datetime.strptime(line[1],"%H:%M")
            students[line[0]] = startTime 
    
    return students

def final_points():
    students = start_time()
    finalPoints = {}
    
    with open('submissions.csv') as sub_file:
        for line in csv.reader(sub_file,delimiter=';'):
            endTime = datetime.strptime(line[3],"%H:%M")
            name = line[0]
            task = line[1]
            grade = line[2]
            if name not in finalPoints:
                finalPoints[name] = {}
            
            if task not in finalPoints[name]:
                finalPoints[name][task] = []
            
            if (line[0] in students and (endTime - students[line[0]]) <= timedelta(hours=3) and 
                (int(line[1]) > 0 and int(line[1]) < 9) and 
                (int(line[2]) >= 0 and int(line[2]) < 7)):
                finalPoints[name][task].append(int(grade))

    for name,grades in finalPoints.items():
        total_score = 0
        for grade,score in grades.items():
            total_score += max(score)
        finalPoints[name] = total_score
    return finalPoints

if __name__ == "__main__":
    print(final_points())