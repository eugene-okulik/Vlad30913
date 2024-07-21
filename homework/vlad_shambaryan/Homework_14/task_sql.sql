
-- Создайте группу (group) и определите своего студента туда
insert into `groups` (title, start_date, end_date) values ('QA ', '2023-04-01', '2023-07-01')
SELECT * FROM `groups` WHERE id = 1480
-- DELETE FROM `groups` WHERE id = 1482


-- Создайте студента (student)
insert into students (name, second_name, group_id) VALUES ('Vl', 'Sh', '1480')
SELECT * FROM students WHERE second_name = 'Sh' and name = 'Vl'
-- DELETE FROM students WHERE id = 1476


-- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
insert into books (title, taken_by_student_id) values ('Python', '1477'), ('Pytest', '1477'), ('XPATH', '1477')
SELECT * FROM books WHERE taken_by_student_id = 1477
-- DELETE FROM books WHERE id = 1474



-- Создайте несколько учебных предметов (subjects)
insert into subjets (title) values ('JavaScript'), ('Postman')
SELECT * FROM subjets WHERE id = 1924
SELECT * FROM subjets WHERE id = 1925
-- DELETE FROM subjets WHERE id = 1917




-- Создайте по два занятия для каждого предмета (lessons)
insert into lessons (title, subject_id) values ('JavaScript', '1924'),('Functions', '1924')
insert into lessons (title, subject_id) values ('Postman', '1925'), ('Autotests in Postman', '1925')
SELECT * FROM lessons WHERE subject_id = 1924
-- DELETE FROM lessons WHERE subject_id = 1913



-- Поставьте своему студенту оценки (marks) для всех созданных вами занятий
insert into marks (value, lesson_id, student_id) values ('9', '4348', '1477'), ('8', '4349', '1477')
insert into marks (value, lesson_id, student_id) values ('9.5', '4340', '1477'), ('10', '4341', '1477')
SELECT * FROM marks WHERE lesson_id = 4340
-- DELETE FROM marks  WHERE lesson_id = 4329


-- Все оценки студента
select students.name, students.second_name, marks.value, marks.lesson_id
from students
-- Соединяем таблицу marks с таблицей students по полю student_id
left join marks on students.id = marks.student_id
-- Фильтруем результаты, чтобы выбрать записи только для студента с именем "Vladimir" и фамилией "Shambaryan"
where name = 'Vl'
and second_name = 'Sh'


-- Все книги, которые находятся у студента
select students.name, students.second_name, books.title
from students
-- Соединяем таблицу books с таблицей students по полю taken_by_student_id
left join books on students.id = books.taken_by_student_id
-- Фильтруем результаты, чтобы выбрать записи только для студента с именем "Vladimir" и фамилией "Shambaryan"
where students.name = 'Vl'
and students.second_name = 'Sh'


-- Для вашего студента выведит всё
select students.name, students.second_name, `groups`.title, `groups`.start_date, `groups`.end_date,
       subjets.title, lessons.title, lessons.subject_id, marks.value, marks.lesson_id, books.title
from students
-- Соединяем таблицу `groups` с таблицей students по полю group_id
left join `groups` on students.group_id = `groups`.id
-- Соединяем таблицу marks с таблицей students по полю student_id
left join marks on students.id = marks.student_id
-- Соединяем таблицу lessons с таблицей marks по полю lesson_id
left join lessons on marks.lesson_id = lessons.id
-- Соединяем таблицу subjets с таблицей lessons по полю subject_id
left join subjets on lessons.subject_id = subjets.id
-- Соединяем таблицу books с таблицей students по полю taken_by_student_id
left join books on students.id = books.taken_by_student_id
-- Фильтруем результаты, чтобы выбрать записи только для студента с ID
where student_id = '1477'