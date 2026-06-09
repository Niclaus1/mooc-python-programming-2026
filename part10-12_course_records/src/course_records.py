# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str, grade: int, credit: int):
        self._name = name
        self._grade = grade
        self._credit = credit

    def course_name(self):
        return self._name

    def get_grade(self):
        return self._grade

    def get_credit(self):
        return self._credit

    # def __str__(self):
    #     return f"name: {self._name}, grade: {self._grade}, credit: {self._credit}"


class CourseCard:
    def __init__(self):
        self.__courses = {}

    def add_course(self, course_entry: Course):
        course = course_entry

        # if course._name not in self.__courses:
        #     self.__courses[course._name] = course
        self.__courses[course._name] = course

    def get_data(self, name: str):
        if name not in self.__courses:
            return None
        else:
            course = self.__courses[name]
            return f"{course.course_name()} ({course.get_credit()} cr) grade {course.get_grade()}"

    def name_found(self, name: str):
        if name in self.__courses:
            return True
        else:
            return False

    def get_grade(self, name):
        return self.__courses[name].get_grade()

    def sum_grade(self):
        grades = 0
        for course in self.__courses:
            grades += self.__courses[course].get_grade()

        return grades

    def sum_credits(self):
        credits = 0

        for course in self.__courses:
            credits += self.__courses[course].get_credit()
        return credits

    def entries_count(self):
        return len(self.__courses)

    def grade_distribution(self):
        grade_distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

        for name in self.__courses:
            if self.get_grade(name) in grade_distribution:
                grade_distribution[self.get_grade(name)] += 1

        return grade_distribution


class CardApplication:
    def __init__(self):
        self.__courses = CourseCard()

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credit = int(input("credits: "))

        if self.__courses.name_found(name) and grade < self.__courses.get_grade(name):
            grade = self.__courses.get_grade(name)

        self.__courses.add_course(Course(name, grade, credit))

    def search(self):
        name = input("course: ")
        course = self.__courses.get_data(name)

        if course is None:
            print("no entry for this course")
            return
        else:
            print(self.__courses.get_data(name))

    def statistics(self):
        course_num = self.__courses.entries_count()
        total_grades = self.__courses.sum_grade()
        total_credits = self.__courses.sum_credits()
        mean = round(total_grades / course_num, 1)
        print(f"{course_num} completed courses, a total of {total_credits} credits")
        print(f"mean {mean}")

        char = "x"
        print("grade distribution")
        grades = self.__courses.grade_distribution()

        for grade, count in sorted(grades.items()):
            print(f"{grade}: {count * char}")

    def execute(self):
        while True:
            print("")
            print("1 add course")
            print("2 get course data")
            print("3 statistics")
            print("0 exit")

            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.search()
            elif command == "3":
                self.statistics()
            else:
                self.execute()


nicko = CardApplication()
nicko.execute()
