import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)


cursor = db.cursor(dictionary=True)

# Создайте студента (student)
cursor.execute("""
INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)
""", ('Vlad', 'Shambaryan', None))
student_id = cursor.lastrowid
print(f"Student id: {student_id}")

# Создайте группу (group) и определите своего студента туда
group_query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values = ('QA', '2025-04-01', '2025-07-01')
cursor.execute(group_query, values)
group_id = cursor.lastrowid
print(f"Group id: {group_id}")

query = "UPDATE students SET group_id = %s WHERE id = %s"
values = (group_id, student_id)
cursor.execute(query, values)


# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
books_query = "insert into books (title, taken_by_student_id) values (%s, %s)"
cursor.executemany(
    books_query, [
        ('Python', student_id),
        ('Pytest', student_id),
        ('XPATH', student_id)
    ]
)


# Создайте несколько учебных предметов (subjects)
cursor.execute("INSERT INTO subjets (title) VALUES (%s)", ['JavaScript'])
subject_1_id = cursor.lastrowid
print(f"Subject 1 id: {subject_1_id}")

cursor.execute("INSERT INTO subjets (title) VALUES (%s)", ['Postman'])
subject_2_id = cursor.lastrowid
print(f"Subject 2 id: {subject_2_id}")

# Создайте по два занятия для каждого предмета (lessons)
cursor.execute("INSERT INTO lessons (title, subject_id) values (%s, %s)", ('JavaScript', subject_1_id))
lesson_1_id = cursor.lastrowid
print(f"JavaScript id: {lesson_1_id}")

cursor.execute("INSERT INTO lessons (title, subject_id) values (%s, %s)", ('Functions', subject_1_id))
lesson_2_id = cursor.lastrowid
print(f"Functions id: {lesson_2_id}")

cursor.execute("INSERT INTO lessons (title, subject_id) values (%s, %s)", ('Postman', subject_2_id))
lesson_3_id = cursor.lastrowid
print(f"Postman id: {lesson_3_id}")

cursor.execute("INSERT INTO lessons (title, subject_id) values (%s, %s)", ('Autotests in Postman', subject_2_id))
lesson_4_id = cursor.lastrowid
print(f"Autotests in Postman id: {lesson_4_id}")


# Поставьте своему студенту оценки (marks) для всех созданных вами занятий

query_marsk = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    query_marsk, [
        ('10', lesson_1_id, student_id),
        ('8', lesson_2_id, student_id),
        ('9', lesson_3_id, student_id),
        ('10', lesson_4_id, student_id)
    ]
)

db.commit()


print(':' * 50, 'Все оценки студента', ':' * 50)
# Все оценки студента
student_grades = """
SELECT students.id, students.name , students.second_name, marks.lesson_id, marks.value
FROM students
JOIN marks ON students.id = marks.student_id
WHERE students.id = %s
"""

cursor.execute(student_grades, (student_id,))
for student_grades in cursor.fetchall():
    print(f"Student grades: {student_grades}")


print(':' * 50, 'Все книги, которые находятся у студента', ':' * 30)
# Все книги, которые находятся у студента
student_books = """
SELECT students.id, students.name , students.second_name , books.title
FROM students
RIGHT JOIN books on students.id = books.taken_by_student_id
WHERE students.id = %s;
"""

cursor.execute(student_books, (student_id,))
for student_books in cursor.fetchall():
    print(f"Student books: {student_books}")


print(':' * 50, 'Вся информация о студенте', ':' * 45)
# Вся информация о студенте
student_info = """
SELECT students.id, students.name, students.second_name, `groups`.start_date,
`groups`.end_date, lessons.title, subjets.title, lessons.subject_id, marks.lesson_id,
marks.value, books.title
FROM students
join `groups` on students.group_id = `groups`.id
join marks on students.id = marks.student_id
join lessons on marks.lesson_id = lessons.id
join subjets on lessons.subject_id = subjets.id
join books on students.id = books.taken_by_student_id
WHERE students.id = %s;
"""

cursor.execute(student_info, (student_id,))
for student_all in cursor.fetchall():
    print(f"Student all: {student_all}")

db.close()
