
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"

names = {}
with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        names[parts[0]] = f'{parts[1]} {parts[2].strip()}'
        
exercises = {}
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        exercises[parts[0]] = []
        for score in parts[1:]:
            exercises[parts[0]].append(int(score))

exams = {}
with open(exam_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        exams[parts[0]] = []
        for score in parts[1:]:
            exams[parts[0]].append(int(score))


# Combine name with exercise and exam data
name_score = {}
for id, name in names.items():
    name_score[name] = 0
    if id in exercises:
        exercises_score = sum(exercises[id]) // 4
        if id in exams:
            exam_score = sum(exams[id]) + exercises_score
            name_score[name] = exam_score

for name, score in name_score.items():
    if score > 0 and score <= 14:
        print(f'{name} {0}')
    elif score > 14 and score <= 17:
        print(f'{name} {1}')
    elif score > 17 and score <= 20:
        print(f'{name} {2}')
    elif score > 20 and score <= 23:
        print(f'{name} {3}')
    elif score > 23 and score <= 27:
        print(f'{name} {4}')
    elif score > 27:
        print(f'{name} {5}')



