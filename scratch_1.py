class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия :{self.surname}
Средняя оценка за домашние задания: {sum(j for j in sum(self.grades.values(),[]))/len(sum(self.grades.values(),[])):0.1f}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}'''
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия :{self.surname}
Средняя оценка за лекции: {sum(j for j in sum(self.grades.values(),[]))/len(sum(self.grades.values(),[])):0.1f}'''
        return res


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
        res = f'Имя: {self.name}\nФамилия :{self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['The school']
good_student = Student('Ruoy', 'Eman', 'your_gender')
good_student.courses_in_progress += ['Python']
good_student.finished_courses += ['Some postgraduate studies']

super_lecturer = Lecturer('Hannibal', 'Lecter')
super_lecturer.courses_attached += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')

cool_mentor = Mentor('Ментор', 'Buddy')
cool_mentor.courses_attached += ['Python']

best_student.rate_lecturer(super_lecturer, 'Python', 10)
best_student.rate_lecturer(super_lecturer, 'Python', 9)
best_student.rate_lecturer(super_lecturer, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(super_lecturer.grades)
print(super_lecturer)
print(some_reviewer)
print(best_student)


