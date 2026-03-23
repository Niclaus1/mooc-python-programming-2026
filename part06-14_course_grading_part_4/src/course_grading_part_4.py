# tee ratkaisu tänne

if True:
    student_file = input("Student information: ")
    exercise_file = input("Exercises completed: ")
    exam_file = input("Exam completed: ")
    course_file = input("Course information: ")
    print('Results written to files results.txt and results.csv')
else:
    student_file = "students1.csv"
    exercise_file = "exercises1.csv"
    exam_file = "exam_points1.csv"
    course_file = "course1.txt"

# Get Student ID & Name
students = {}
with open(student_file) as new_file:
    for line in new_file:
        parts = line.strip().split(';')
        if parts[0] == 'id':
            continue
        students[parts[0]] = f'{parts[1]} {parts[2]}'

def load_data(filename: str) -> dict:
    data = {}
    try:
        with open(filename) as new_file:
            for line in new_file:
                parts = line.strip().split(";")
                if parts[0] == 'id':
                    continue
                data[parts[0]] = []
                for value in parts[1:]:
                    data[parts[0]].append(int(value))
    except FileNotFoundError:
        return {}
    return data

exercises = load_data(exercise_file)
exams = load_data(exam_file)

# Combine name with exercise and exam data
name_score = {}
for id, name in students.items():
    name_score[name] = 0
    if id in exercises:
        exercises_score = sum(exercises[id]) // 4
        if id in exams:
            exam_score = sum(exams[id]) + exercises_score
            name_score[name] = exam_score

def get_grade(total_score):
    statistic = [(27, 5), (23, 4), (20, 3), (17, 2), (14, 1)]
    for limit, grade in statistic:
        if total_score > limit:
            return grade
    return 0

def get_course():
    with open(course_file) as new_file:
        course = ""
        for line in new_file:
            line = line.split(":")
            if line[0] == 'name': 
                course += f'{line[1].strip()}, '
            else:  
                course += f'{line[1].strip()} credits'
        return f"{course}\n{'=' * len(course)}\n"

with open("results.txt","w") as txt_file, open("results.csv","w")as csv_file:
    txt_file.write(get_course())
    txt_file.write(f'{'name':30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}\n')
    
    for id, name in students.items():
        exec_nbr = 0
        if id in exercises:
            exec_nbr = sum(exercises[id])
            if id in exams:
                exm_pts = sum(exams[id])
        exec_pts = exec_nbr // 4
        tot_pts = exec_pts + exm_pts
        grade = get_grade(tot_pts)
        txt_file.write(f'{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}\n')
        csv_file.write(f'{id};{name};{grade}\n')
    txt_file.close()
    csv_file.close()