students = ['Ivanov', 'Petrov', 'Sidorov']  # имена студентов

subjects = ['math', 'biology', 'geography']

students_str = ', '.join(students)  # создаем строку из элементов списка students

subjects_str = ', '.join(subjects)  # создаем строку из элементов списка subjects

print('Students ' + students_str + ' study these subjects: ' + subjects_str)
