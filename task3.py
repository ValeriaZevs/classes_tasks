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