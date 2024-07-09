# Задание 3
# Даны такие списки:
#
# students = ['Ivanov', 'Petrov', 'Sidorov']
#
# subjects = ['math', 'biology', 'geography']
#
# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
#
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography


students = ['Ivanov', 'Petrov', 'Sidorov']  # имена студентов

subjects = ['math', 'biology', 'geography']

students_str = ', '.join(students)  # создаем строку из элементов списка students

subjects_str = ', '.join(subjects)  # создаем строку из элементов списка subjects

print('Students ' + students_str + ' study these subjects: ' + subjects_str)