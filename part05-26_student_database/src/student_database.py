# Write your solution here
def add_student(classroom : dict, student: str):
    classroom[student] = []

def print_student(classroom : dict, student : str):
    

    if student not in classroom:
        print(f'{student}: no such person in the database')
    elif classroom[student] == []:
        print(f'{student}:')
        print(" no completed courses")
    else:
        print(f'{student}:')
        print(f' {len(classroom[student])} completed courses:')

        total = 0
        for subject,grade in classroom[student]:
            print(f'  {subject} {grade}')
            total += grade

        average = total / len(classroom[student])
        print(f' average grade {average}')



def add_course(classroom : dict, student : str, subject : tuple):
    if student not in classroom:
        classroom[student] = []

    flag = False
    
    for index in range(len(classroom[student])):
        if classroom[student][index][0] == subject[0]:
            flag = True
            if classroom[student][index][1] < subject[1]:
                classroom[student][index] = subject

    if not flag and subject[1] != 0:
        classroom[student].append(subject)

def get_average(classroom : dict, student : str):
    if len(classroom[student]) == 0:
        return 0
    
    total = 0
    for subject,grade in classroom[student]:
        total += grade
    
    average = total / len(classroom[student])
    return average
        
def summary(classrooom : dict):
    print(f'students {len(classrooom)}')

    most_enrolled_count = 0
    most_enrolled_person = ""
    highest_grade = 0
    highest_person = ""

    for student in classrooom:
        if most_enrolled_count < len(classrooom[student]):
            most_enrolled_count = len(classrooom[student])
            most_enrolled_person = student
            
        if get_average(classrooom,student) > highest_grade:
            highest_grade = get_average(classrooom,student)
            highest_person = student

    print(f'most courses completed {most_enrolled_count} {most_enrolled_person}')
    print(f'best average grade {highest_grade} {highest_person}')

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)