# Write your solution here
import urllib.request
import json
import math

def retrieve_all():
    getData = urllib.request.urlopen('https://studies.cs.helsinki.fi/stats-mock/api/courses')
    jsonFormat = json.loads(getData.read())
    activeList = []
    for data in jsonFormat:
        if data['enabled']:
            activeList.append((data['fullName'],data['name'],data['year'],sum(data['exercises'])))
    return activeList

def retrieve_course(course_name : str):
    getData = urllib.request.urlopen(course_name)
    jsonFormat = json.loads(getData.read())
    dataDict = {}
    students = []
    hours = []
    exercises = []

    for week, data  in jsonFormat.items():
        students.append(data['students'])
        hours.append(data['hour_total'])
        exercises.append(data['exercise_total'])

    dataDict["weeks"] = len(jsonFormat)
    dataDict['students'] = max(students)
    dataDict['hours'] = sum(hours)
    dataDict['hours_average'] =  math.floor(sum(hours) / max(students))
    dataDict['exercises'] = sum(exercises)
    dataDict['exercises_average'] = math.floor(sum(exercises) / max(students))
    return dataDict
if __name__ == "__main__":
    retrieve_course("https://studies.cs.helsinki.fi/stats-mock/api/courses/docker2019/stats")
