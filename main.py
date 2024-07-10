import random


class Student:
    def __init__(self, student_id, name, surname):
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.courses = []

    def adding_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.append_student(self)

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            course.remove_studnet(self)

    def get_grades(self):
        return {
            course.course_name: course.get_grades(self) for course in self.courses
        }


class Course:
    def __init__(self, course_id, course_name, credits_of_course):
        self.course_id = course_id
        self.course_name = course_name
        self.credits_of_course = credits_of_course
        self.students = []
        self.grades = {}

    def append_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    # def get_student(self):
    #     return [student.name for student in self.students]


class Grade:
    def __init__(self):
        self.grades = {}

    def assign_grade(self, student, course, grade):
        if course.course_id not in self.grades:
            self.grades[course.course_id] = {}
        self.grades[course.course_id][student.student_id] = grade

    # def get_grade(self, student, course):
    #     return self.grades.get(course.course_id, {}).get(student.student_id, None)


class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def append_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Student with student Id {student_id} removed")
                return
        print(f"There is no student with that ID {student_id}")

    def append_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def get_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student_id
        return None

    def get_courses_by_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None


def main():
    school = School()

    count = int(input("Pls enter how many students do you want to enter: "))
    print(f"Now you have to enter {count} Students and their grades")

    courses = {
        1: "Math",
        2: "English",
        3: "History",
        4: "Physics"
    }

    student_ids = []

    for i in range(count):
        student_id = int(input("Enter student id: "))
        name = input("Enter Student name: ")
        surname = input("Enter Student surname: ")
        student = Student(student_id, name, surname)
        school.append_student(student)
        student_ids.append(student_id)
        print("Student added")

        course_id = int(input("Enter course id (1: Math, 2: English, 3: History, 4: Physics): "))
        if course_id in courses:
            course_name = courses[course_id]
            print(f"That student Id is {student_id} and his/her course is {course_name}")

            grade_value = random.uniform(60, 100)
            course = Course(course_id, course_name, 3)
            student.adding_course(course)
            course.append_student(student)
            Grade().assign_grade(student, course, grade_value)
            print(f"Grade {grade_value:.2f} assigned to student {student.name} for course {course.course_name}")
        else:
            print(f"That student Id is {student_id} and the provided course id ({course_id}) is incorrect.")

    ques = input("Do you want to remove any student? pls answer yes or no: ")
    if ques.lower() == "yes":
        answer = int(input("Which student do you want to remove, pls write student id: "))
        school.remove_student(answer)
    else:
        print("You don't want to remove student")


if __name__ == "__main__":
    main()
