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


class Grade:
    def __init__(self):
        self.grades = {}

    def assign_grade(self, student, course, grade):
        if course.course_id not in self.grades:
            self.grades[course.course_id] = {}
        self.grades[course.course_id][student.student_id] = grade


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

    def remove_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                self.courses.remove(course)
                print(f"Course with course ID {course_id} removed")
                return
        print(f"There is no course with that ID {course_id}")


def main():
    school = School()

    count = int(input("Pls enter how many students do you want to enter: "))
    print(f"Now you have to enter {count} Students and their grades")

    student_ids = []

    for i in range(count):
        student_id = int(input("Enter student id: "))
        name = input("Enter Student name: ")
        surname = input("Enter Student surname: ")
        student = Student(student_id, name, surname)
        school.append_student(student)
        student_ids.append(student_id)
        print("Student added")

        course = int(input("Enter number of courses: "))
        for j in range(course):
            course_id = int(input(f"Enter course id {j + 1}: "))
            course_name = input(f"Enter course name {j + 1}: ")
            course_credit = int(input(f"Enter credit of this course {j + 1}: "))
            course = Course(course_id, course_name, course_credit)
            school.append_course(course)
            student.adding_course(course)
            course.append_student(course)

            grade_value = random.uniform(51, 100)
            Grade().assign_grade(student, course, grade_value)
            print(f"Grade {grade_value:.2f} assigned to student {student.name} for course {course.course_name}")

    ques = input("Do you want to remove any student? pls answer yes or no: ")
    if ques.lower() == "yes":
        answer = int(input("Which student do you want to remove, pls write student id: "))
        school.remove_student(answer)
    else:
        print("You don't want to remove student")

    ques2 = input("Do you want to remove any course? Pls answer yes or no: ")
    if ques2.lower() == "yes":
        answer2 = int(input("Which course do you want to remove, pls course id: "))
        school.remove_course(answer2)


if __name__ == "__main__":
    main()
