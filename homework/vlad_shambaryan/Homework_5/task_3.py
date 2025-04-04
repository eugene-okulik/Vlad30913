students = ['Ivanov', 'Petrov', 'Sidorov']  # фамилии студентов

subjects = ['math', 'biology', 'geography']

students_str = ', '.join(students)  # создаем строку из элементов списка students

subjects_str = ', '.join(subjects)  # создаем строку из элементов списка subjects

print('Students ' + students_str + ' study these subjects: ' + subjects_str)

# Список фамилий студентов
students = ['Ivanov', 'Petrov', 'Sidorov']

# Список предметов
subjects = ['math', 'biology', 'geography']

# Создаем строку из элементов списка students, разделенных запятыми
students_str = ', '.join(students)

# Создаем строку из элементов списка subjects, разделенных запятыми
subjects_str = ', '.join(subjects)

# Выводим сообщение, используя созданные строки
print('Students ' + students_str + ' study these subjects: ' + subjects_str)
