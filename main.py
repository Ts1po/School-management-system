class Student:
    def __init__(self, student_id, name, surname):
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.courses = []

    def adding_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.append_stundet(self)

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

    def get_student(self):
        return [student.name for student in self.students]


class Grade:
    def __init__(self):
        self.grades = {}

    def assign_grade(self, student, course, grade):
        if course.course_id not in self.grades:
            self.grades[course.course_id] = {}
        self.grades[course.course_id][student.student_id] = grade

    def get_grade(self, student, course):
        return self.grades.get(course.course_id, {}).get(student.student_id, None)


class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def append_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

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
