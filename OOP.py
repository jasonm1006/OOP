class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average(self):
        quantity = 0
        amount = 0
        for key in self.grades:
            for values in self.grades[key]:
                quantity += 1
                amount += int(values)
        return amount / quantity

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __eq__(self, other):
        return self.average() == other.average()

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average()}\n' \
                 f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}'
        return output

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average(self):
        quantity = 0
        amount = 0
        for key in self.grades:
            for values in self.grades[key]:
                quantity += 1
                amount += int(values)
        return amount / quantity

    def __eq__(self, other):
        return self.average() == other.average()

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average()}'
        return output

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Roman', 'Matveev', 'male')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Maxim', 'Amosov')
reviewer_2.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 6)

reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 7)

lecturer_1 = Lecturer('Some', 'Body')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Dmitriy', 'Alaev')
lecturer_2.courses_attached += ['Git']

student_1.rate_lect(lecturer_1, 'Python', 8)
student_1.rate_lect(lecturer_1, 'Python', 9)
student_1.rate_lect(lecturer_2, 'Git', 10)
student_1.rate_lect(lecturer_2, 'Git', 7)

student_2.rate_lect(lecturer_1, 'Python', 7)
student_2.rate_lect(lecturer_1, 'Python', 9)
student_2.rate_lect(lecturer_2, 'Git', 8)
student_2.rate_lect(lecturer_2, 'Git', 10)

print(student_1)
print(student_2)
print(reviewer_1)
print(reviewer_2)
print(lecturer_1)
print(lecturer_2)

def average_grade_stud(students, course):
    sum_grades = 0
    count = 0
    for stud in students:
        if (isinstance(stud, Student) and (course in stud.courses_in_progress or course in stud.finished_courses)):
            sum_grades += sum(stud.grades[course])
            count += len(stud.grades[course])
    if count == 0:
        return "Нет оценок"
    else:
        return sum_grades / count

def average_grade_lect(lecturers, course):
    sum_grades = 0
    count = 0
    for lec in lecturers:
        if (isinstance(lec, Lecturer) and course in lec.courses_attached):
            sum_grades += sum(lec.grades[course])
            count += len(lec.grades[course])
    if count == 0:
        return "Нет оценок"
    else:
        return sum_grades / count

students_list = list()
students_list.append(student_1)
students_list.append(student_2)

lectors_list = list()
lectors_list.append(lecturer_1)
lectors_list.append(lecturer_2)

print("Средняя оценка среди студентов по курсу Python: ", average_grade_stud(students_list, 'Python'))
print("Средний оценка среди лекторов по курсу Git: ", average_grade_lect(lectors_list, 'Git'))

print(student_1 == student_2)
print(lecturer_1 == lecturer_2)
