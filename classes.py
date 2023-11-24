class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def avg_grades(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades += grade
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.avg_grades()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")
    
    def __lt__(self, other):
        return self.avg_grades() < other.avg_grades()
    
    def __eq__(self, other):
        return self.avg_grades() == other.avg_grades()

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grades(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades += grade
        return round(sum(all_grades) / len(all_grades), 1)
    
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.avg_grades()}")
    
    def __lt__(self, other):
        return self.avg_grades() < other.avg_grades()
    
    def __eq__(self, other):
        return self.avg_grades() == other.avg_grades()

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
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")
    
def avg_grades(persons, course):    # Реализована единая функция для двух классов
    grades_list = []
    for person in persons:
        grades_list += person.grades[course]
    result = round(sum(grades_list) / len(grades_list), 1)
    if isinstance(persons[0], Student):
        print(f"Средняя оценка за домашние задания в рамках курса {course}: {result}")
    elif isinstance(persons[0], Lecturer):
        print(f"Средняя оценка за лекции в рамках курса {course}: {result}")

    
stud_1 = Student('Harry', 'Potter', 'Male')
stud_1.courses_in_progress += ['Charms', 'Potions']
stud_1.finished_courses += ['Transfiguration']

stud_2 = Student('Hermione', 'Granger', 'Female')
stud_2.courses_in_progress += ['Charms', 'Potions']
stud_2.finished_courses += ['Herbology']

lect_1 = Lecturer('Remus', 'Lupin')
lect_1.courses_attached += ['Charms', 'Potions']

lect_2 = Lecturer('Dolores', 'Umbridge')
lect_2.courses_attached += ['Charms', 'Potions']

rew_1 = Reviewer('Severus', 'Snape')
rew_1.courses_attached += ['Charms', 'Potions']

rew_2 = Reviewer('Albus', 'Dumbldore')
rew_2.courses_attached += ['Charms', 'Potions']

rew_1.rate_hw(stud_1, 'Charms', 9)
rew_1.rate_hw(stud_1, 'Charms', 7)
rew_1.rate_hw(stud_1, 'Potions', 8)
rew_2.rate_hw(stud_2, 'Charms', 10)
rew_2.rate_hw(stud_2, 'Potions', 9)
rew_2.rate_hw(stud_2, 'Potions', 10)

stud_1.rate_lc(lect_1, 'Charms', 10)
stud_1.rate_lc(lect_1, 'Charms', 9)
stud_1.rate_lc(lect_1, 'Charms', 8)
stud_1.rate_lc(lect_2, 'Charms', 10)
stud_1.rate_lc(lect_2, 'Charms', 9)
stud_1.rate_lc(lect_2, 'Charms', 10)

print(rew_1)
print('-------')
print(lect_1)
print('-------')
print(stud_1)
print('-------')
print(stud_2)
print('-------')
print(stud_1 < stud_2, stud_1 == stud_2, lect_1 > lect_2)
print('-------')
avg_grades([stud_1, stud_2], 'Potions')
print('-------')
avg_grades([lect_1, lect_2], 'Charms')