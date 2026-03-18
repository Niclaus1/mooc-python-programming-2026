
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
            
name_grade = {}
for name, score in name_score.items():
    if score > 0 and score <= 14:
        name_grade[name] = 0
    elif score > 14 and score <= 17:
        name_grade[name] = 1
    elif score > 17 and score <= 20:
        name_grade[name] = 2
    elif score > 20 and score <= 23:
        name_grade[name] = 3
    elif score > 23 and score <= 27:
        name_grade[name] = 4
    elif score > 27:
        name_grade[name] = 5


print(f'{'name':30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}')
for id, name in names.items():
    exec_nbr = 0
    if id in exercises:
        exec_nbr = sum(exercises[id])
        if id in exams:
            exm_pts = sum(exams[id])
    exec_pts = exec_nbr // 4
    tot_pts = exec_pts + exm_pts
    grade = name_grade[name]

    print(f'{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}')
