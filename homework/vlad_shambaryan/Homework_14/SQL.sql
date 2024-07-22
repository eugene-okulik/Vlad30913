-- Создайте студента (student)
insert into students (name, second_name) VALUES ('Bob', 'Trump')


-- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
insert into books (title, taken_by_student_id) values ('Python', '1611'), ('Pytest', '1611'), ('XPATH', '1611')


-- Создайте группу (group) и определите своего студента туда
insert into `groups` (title, start_date, end_date) values
('QA testers', '2023-04-01', '2023-07-01')


-- Обновляем запись студента, присваивая ему созданную группу
UPDATE students
SET group_id = 1536
WHERE id = '1611'


-- Создайте несколько учебных предметов (subjects)
insert into subjets (title) values ('JavaScript'), ('Postman')


-- Создайте по два занятия для каждого предмета (lessons)
insert into lessons (title, subject_id) values ('JavaScript', '2057'),('Functions', '2057')
insert into lessons (title, subject_id) values ('Postman', '2058'), ('Autotests in Postman', '2058')


-- Поставьте своему студенту оценки (marks) для всех созданных вами занятий
insert into marks (value, lesson_id, student_id) values ('9', '4596', '1611'), ('8', '4597', '1611')
insert into marks (value, lesson_id, student_id) values ('9.5', '4598', '1611'), ('10', '4599', '1611')


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
SELECT students.name, students.second_name, `groups`.title AS group_title, `groups`.start_date, `groups`.end_date,
       subjets.title AS subject_title, lessons.title AS lesson_title, lessons.subject_id,
       marks.value AS mark_value, marks.lesson_id, books.title AS book_title
FROM students
LEFT JOIN `groups` ON students.group_id = `groups`.id
LEFT JOIN marks ON students.id = marks.student_id
LEFT JOIN lessons ON marks.lesson_id = lessons.id
LEFT JOIN subjets ON lessons.subject_id = subjets.id
LEFT JOIN books ON students.id = books.taken_by_student_id
WHERE students.name = 'Vlad' AND students.second_name = 'Shambaryan'