
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

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

for id, name in names.items():
    if id in exercises:
        exercises_score = sum(exercises[id])
        print(f'{name} {exercises_score}')
    else:
        print(f'{name} 0')