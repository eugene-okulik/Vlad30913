-- Создайте студента (student)
insert into students (name, second_name) VALUES ('Bob', 'Trump')


-- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
insert into books (title, taken_by_student_id) values ('Python', '1591'), ('Pytest', '1591'), ('XPATH', '1591')


-- Создайте группу (group) и определите своего студента туда
insert into `groups` (title, start_date, end_date) values
('QA testers', '2023-04-01', '2023-07-01')


-- Создайте несколько учебных предметов (subjects)
insert into subjets (title) values ('JavaScript'), ('Postman')


-- Создайте по два занятия для каждого предмета (lessons)
insert into lessons (title, subject_id) values ('JavaScript', '2039'),('Functions', '2039')
insert into lessons (title, subject_id) values ('Postman', '2040'), ('Autotests in Postman', '2040')


-- Поставьте своему студенту оценки (marks) для всех созданных вами занятий
insert into marks (value, lesson_id, student_id) values ('9', '4560', '1591'), ('8', '4561', '1591')
insert into marks (value, lesson_id, student_id) values ('9.5', '4562', '1591'), ('10', '4563', '1591')


-- Все оценки студента
select students.name, students.second_name, marks.value, marks.lesson_id
from students
left join marks on students.id = marks.student_id
where name = 'Bob'
and second_name = 'Trump'

-- Все книги, которые находятся у студента
select students.name, students.second_name, books.title
from students
left join books on students.id = books.taken_by_student_id
where students.name = 'Bob'
and students.second_name = 'Trump'


-- Для вашего студента выведит всё
select students.name, students.second_name, `groups`.title, `groups`.start_date, `groups`.end_date,
       subjets.title, lessons.title, lessons.subject_id, marks.value, marks.lesson_id, books.title
from students
left join `groups` on students.group_id = `groups`.id
left join marks on students.id = marks.student_id
left join lessons on marks.lesson_id = lessons.id
left join subjets on lessons.subject_id = subjets.id
left join books on students.id = books.taken_by_student_id
where student_id = '1591'
