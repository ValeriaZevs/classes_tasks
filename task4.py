class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished = []
        self.progress_courses = []
        self.grades = {}
        self.average = float()

    def rate_student(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.progress_courses and course in lecturer.courses:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка: Невозможно выставить оценку.')

    def add_course(self, course_name):
        self.finished.append(course_name)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка: Нет такого ученика для сравнения')
            return False
        return self.average < other.average

    def __str__(self):
        count = sum(len(grades) for grades in self.grades.values())
        self.average = (sum(map(sum, self.grades.values())) / count) if count else 0
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за домашнее задание: {self.average:.2f}\n'
               f'Курсы в процессе обучения: {", ".join(self.progress_courses)}\n'
               f'Завершенные курсы: {", ".join(self.finished)}')
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []
        self.grades_from_lecturers = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average = float()
        self.grades = {}

    def __str__(self):
        count = sum(len(grades) for grades in self.grades.values())
        self.average = (sum(map(sum, self.grades.values())) / count) if count else 0
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.average:.2f}\n')
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка: Такое сравнение некорректно')
            return False
        return self.average < other.average


class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses and course in student.progress_courses:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка: Невозможно выставить оценку.')

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n'
        return res


def student_rating(list_of_students, course):
    total = 0
    count = 0
    for student in list_of_students:
        if course in student.progress_courses:
            total += student.average
            count += 1
    return total / count if count > 0 else 0  # Обработка деления на ноль


def lecturer_rating(list_of_lecturers, course):
    total = 0
    count = 0
    for lecturer in list_of_lecturers:
        if course in lecturer.courses:
            total += lecturer.average
            count += 1
    return total / count if count > 0 else 0  # Обработка деления на ноль



lecturer_1 = Lecturer('Pvel', 'Pavlovich')
lecturer_1.courses += ['Python']
lecturer_2 = Lecturer('Ivan', 'Ivanov')
lecturer_2.courses += ['Java']
lecturer_3 = Lecturer('Vasya', 'Vasilievich')
lecturer_3.courses += ['Python']


reviewer_1 = Reviewer('Reviewer', 'One')
reviewer_1.courses += ['Python', 'Java']
reviewer_2 = Reviewer('Reviewer', 'Two')
reviewer_2.courses += ['Python', 'Java']


student_1 = Student('Student', 'One', 'male')
student_1.progress_courses += ['Python']
student_1.finished += ['Pascal']

student_2 = Student('Student', 'Two', 'male')
student_2.progress_courses += ['Java']
student_2.finished += ['Pascal']

student_3 = Student('Student', 'Three', 'male')
student_3.progress_courses += ['Python']
student_3.finished += ['Pascal']


student_1.rate_student(lecturer_1, 'Python', 4)
student_1.rate_student(lecturer_1, 'Python', 5)
student_1.rate_student(lecturer_1, 'Python', 3)

student_2.rate_student(lecturer_2, 'Java', 10)
student_2.rate_student(lecturer_2, 'Java', 9)


reviewer_1.rate_student(student_1, 'Python', 8)
reviewer_1.rate_student(student_1, 'Python', 5)
reviewer_1.rate_student(student_1, 'Python', 9)

reviewer_2.rate_student(student_2, 'Java', 8)
reviewer_2.rate_student(student_2, 'Java', 7)


print('Студенты:')
print(student_1)
print()
print(student_2)
print()
print(student_3)
print()
print('Лектора:')
print(lecturer_1)
print()
print(lecturer_2)
print()
print(lecturer_3)

print(f'Результат сравнения студентов: '
      f'{student_1.name} {student_1.surname} > {student_2.name} {student_2.surname} = {student_1 > student_2}')
print(f'Результат сравнения лекторов: '
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 < lecturer_2}')

# Расчет средней оценки
print(f"Средняя оценка для всех студентов по курсу 'Python': {student_rating([student_1, student_2, student_3], 'Python'):.2f}")
print(f"Средняя оценка для всех лекторов по курсу 'Java': {lecturer_rating([lecturer_1, lecturer_2, lecturer_3], 'Java'):.2f}")