def stud_count(list_stud, courses):

        student = list()
        student_1 = list()
        count = 0
        [student.append(b.grades.get(courses)) for b in list_stud]
        student_1 = sum(student, [])
        count = sum(sum(student, []), 0)/len(student_1)
        if list_stud == Student.student_list:
            return f'Cредняя оценка за домашние задания по всем студентам в рамках "{courses}" = {count}'
        elif list_stud == Lecturer.lecturer_list:
            return f'Cредняя оценка за лекции  по всем лекторам в рамках "{courses}" = {count}'
def lctr_count(list_lctr, courses):
    pass

class Student:
    student_list = list()
    def __init__(self, name, surname, gender):
        Student.student_list.append(self)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def __lt__(self, other):
        if sum(self.grades.values(),[]) > sum(other.grades.values(),[]):
            return f'Сравнение студентов по средней оценке за домашние задания {self.name} > {other.name}'
        else:
            return f'Сравнение студентов по средней оценке за домашние задания {self.name} < {other.name}'
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
    lecturer_list = list()
    def __init__(self, name, surname):
        Lecturer.lecturer_list.append(self)
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия :{self.surname}
Средняя оценка за лекции: {sum(j for j in sum(self.grades.values(),[]))/len(sum(self.grades.values(),[])):0.1f}'''
        return res
    # def compare(self, lecturer):
    #     if sum(self.grades.values(),[]) > sum(lecturer.grades.values(),[]):
    #         return f'Сравнение лектров по средней оценке за лекции {self.name} > {lecturer.name}'
    #     else:
    #         return f'Сравнение лектров по средней оценке за лекции {self.name} < {lecturer.name}'
    def __lt__(self, other):
        if sum(self.grades.values(),[]) > sum(other.grades.values(),[]):
            return f'Сравнение лектров по средней оценке за лекции {self.name} > {other.name}'
        else:
            return f'Сравнение лектров по средней оценке за лекции {self.name} < {other.name}'

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


best_student = Student('Ruoy', 'Eman', 'some_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['The school']
good_student = Student('Goose', 'Choker', 'The_best_gender')
good_student.courses_in_progress += ['Python']
good_student.courses_in_progress += ['C+-']
good_student.finished_courses += ['Some postgraduate studies']

super_lecturer = Lecturer('Hannibal', 'Lecter')
super_lecturer.courses_attached += ['Python']
ultra_lecturer = Lecturer('John', 'Cena')
ultra_lecturer.courses_attached += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
second_reviewer = Reviewer('Second', 'Friend')

cool_mentor = Mentor('Vasya', 'Thunderbolt')
cool_mentor.courses_attached += ['Python', 'C+-']
another_mentor = Mentor('Omar', 'Hayam')
another_mentor.courses_attached += ['Python']

best_student.rate_lecturer(super_lecturer, 'Python', 10)
best_student.rate_lecturer(super_lecturer, 'Python', 8)

good_student.rate_lecturer(ultra_lecturer, 'Python', 10)
good_student.rate_lecturer(ultra_lecturer, 'Python', 5)


cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 5)

cool_mentor.rate_hw(good_student, 'Python', 9)
cool_mentor.rate_hw(good_student, 'Python', 6)
cool_mentor.rate_hw(good_student, 'C+-', 10)
cool_mentor.rate_hw(good_student, 'C+-', 1)


#
print(some_reviewer)
print(super_lecturer)
print(best_student)

print(best_student > good_student)
print(super_lecturer > ultra_lecturer)
print(stud_count(Student.student_list, 'Python'))
print(stud_count(Lecturer.lecturer_list, 'Python'))


