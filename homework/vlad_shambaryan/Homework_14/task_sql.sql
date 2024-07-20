-- Создайте студента (student)
insert into students (name, second_name, group_id) VALUES ('Vladimir', 'Shambaryan', 1)


-- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
insert into books (title, taken_by_student_id)
values ('Python', '1467'), ('Pytest', '1467'), ('XPATH', '1467')


-- Создайте группу (group) и определите своего студента туда
insert into `groups` (title, start_date, end_date)
values ('QA testers', '2024-04-01', '2024-07-01')


-- Обновляем запись студента, присваивая ему новую группу
update students
set group_id = (
    select id from `groups`
    where title = 'QA testers' and start_date = '2024-04-01' and end_date = '2024-07-01'
)
where id = '1467'


-- Создайте несколько учебных предметов (subjects)
insert into subjets (title) values ('JavaScript'), ('Postman')


-- Создайте по два занятия для каждого предмета (lessons)
insert into lessons (title, subject_id) values ('JavaScript', '1910'),('Functions', '1910')
insert into lessons (title, subject_id) values ('Postman', '1911'), ('Autotests in Postman', '1911')


-- Поставьте своему студенту оценки (marks) для всех созданных вами занятий
insert into marks (value, lesson_id, student_id) values ('10', '4324', '1467'), ('10', '4321', '1467')
insert into marks (value, lesson_id, student_id) values ('10', '4322', '1467'), ('10', '4323', '1467')


-- Все оценки студента
select students.name , students.second_name , marks.value , marks.lesson_id
from students
left join marks on students.id = marks.student_id
where name = 'Vladimir'
and second_name = 'Shambaryan'


-- Все книги, которые находятся у студента
select students.name , students.second_name , books.title
from students
left join books on students.id = books.taken_by_student_id
where students.name = 'Vladimir'
and students.second_name = 'Shambaryan'


-- Для вашего студента выведит всё
select students.name, students.second_name, `groups`.title, `groups`.start_date, `groups`.end_date, subjets.title, lessons.title, lessons.subject_id,
marks.value, marks.lesson_id, books.title
from students
join `groups` on students.group_id = `groups`.id
join marks on students.id = marks.student_id
join lessons on marks.lesson_id = lessons.id
join subjets on lessons.subject_id = subjets.id
join books on students.id = books.taken_by_student_id
where marks.student_id = '1467'


select students.name, students.second_name, `groups`.title, `groups`.start_date, `groups`.end_date, subjets.title, lessons.title, lessons.subject_id,
marks.value, marks.lesson_id, books.title
from students
left join `groups` on students.group_id = `groups`.id
left join marks on students.id = marks.student_id
left join lessons on marks.lesson_id = lessons.id
left join subjets on lessons.subject_id = subjets.id
left join books on students.id = books.taken_by_student_id
where marks.student_id = '1467'
