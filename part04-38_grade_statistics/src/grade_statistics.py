# Write your solution here
def main():
    grade_distribution()

def grade_input():
    exam_points = []
    exercise_points = []
    
    while True:
        point_input = input('Exam points and exercise completer:')
        if point_input == '':
            break

        split_points = point_input.split()

        exam_points.append(int(split_points[0]))
        exercise_points.append(int(split_points[1]))

    return exam_points, exercise_points

def point_average():
    exam_points, exercise_points = grade_input()
    
    raw_grade =[]
    sum = 0

    for index in range(len(exercise_points)):
        exercise_points[index] = exercise_points[index] // 10
        
        if exam_points[index] < 10:
            raw_grade.append(0)
        else:
            raw_grade.append(exercise_points[index] + exam_points[index])

        sum += (exercise_points[index] + exam_points[index])
    
    point_average = float(sum) / len(raw_grade)
    print('Statistics:')
    print(f'Points average: {point_average}')
    return raw_grade

def grade_equivalent(): 
    list = point_average()
    grades = []
    
    for raw_grade in list:
        if raw_grade <= 14 and raw_grade >= 0:
            grades.append(0)
        elif raw_grade >= 15 and raw_grade <= 17:
            grades.append(1)
        elif raw_grade >= 18 and raw_grade <= 20:
            grades.append(2)
        elif raw_grade >= 21 and raw_grade <= 23:
            grades.append(3)
        elif raw_grade >= 24 and raw_grade <= 27:
            grades.append(4)
        elif raw_grade >= 28 and raw_grade <= 30:
            grades.append(5)
    # print(f'Grade Equivalent: {grades}')

    return grades

def pass_percentage():
    student_grades = grade_equivalent()
    passing_students = 0
    
    for grade in student_grades:
        if grade >= 1:
            passing_students += 1

    passing_percentage = float(passing_students / len(student_grades)) * 100

    print(f'Pass percentage: {passing_percentage:.1f}')
    return student_grades
    
def grade_distribution():
    student_grades = pass_percentage()
    
    print('Grade distribution:')
    grade5 = '5: ' 
    grade4 = '4: '
    grade3 = '3: '
    grade2 = '2: '
    grade1 = '1: '
    grade0 = '0: '
    char = '*'
    
    for grading in student_grades:
        if grading == 5:
            grade5 += char
        if grading == 4:
            grade4 += char
        if grading == 3:
            grade3 += char
        if grading == 2:
            grade2 += char
        if grading == 1:
            grade1 += char
        if grading == 0:
            grade0 += char

    print(grade5)
    print(grade4)
    print(grade3)
    print(grade2)
    print(grade1)
    print(grade0)

main()