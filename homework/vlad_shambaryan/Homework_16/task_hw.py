import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()

# Подключаемся к базе данных, используя переменные окружения
db = mysql.connect(
    user=os.getenv('DB_USER'),  # Получаем имя пользователя из переменных окружения
    passwd=os.getenv('DB_PASSW'),  # Получаем пароль из переменных окружения
    host=os.getenv('DB_HOST'),  # Получаем хост из переменных окружения
    port=os.getenv('DB_PORT'),  # Получаем порт из переменных окружения
    database=os.getenv('DB_NAME')  # Получаем имя базы данных из переменных окружения
)
print('=' * 140)  # Печатаем разделительную линию

cursor = db.cursor()  # Создаем курсор для выполнения SQL-запросов

# Определяем путь к файлу CSV
base_file = os.path.dirname(__file__)  # Получаем путь к текущему файлу
homework = os.path.dirname(os.path.dirname(base_file))  # Получаем путь к папке на уровень выше
data_text = os.path.join(homework, "eugene_okulik", "Lesson_16", "hw_data", "data.csv")  # Определяем путь к CSV файлу


with open(data_text, "r", newline="") as data_file:  # Открываем CSV файл в режиме чтения
    reader = csv.reader(data_file)  # Создаем объект для чтения CSV файла
    next(reader)  # Пропускаем заголовок

    # Проходим по каждой строке файла
    for read in reader:  # Для каждой строки в CSV файле
        # Распаковываем значения из строки
        name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = read

        query = """
    SELECT students.name, students.second_name, `groups`.title, books.title, subjets.title, lessons.title, marks.value
        FROM students
        JOIN `groups` ON students.group_id = `groups`.id
        JOIN books ON students.id = books.taken_by_student_id
        JOIN marks ON students.id = marks.student_id
        JOIN lessons ON marks.lesson_id = lessons.id
        JOIN subjets ON lessons.subject_id = subjets.id
        WHERE students.name = %s
        AND students.second_name = %s
        AND `groups`.title = %s
        AND books.title = %s
        AND subjets.title = %s
        AND lessons.title = %s
        AND marks.value = %s
        """
        # Параметры запроса
        values = (name, second_name, group_title, book_title, subject_title, lesson_title, mark_value)

        cursor.execute(query, values)  # Выполняем SQL-запрос с параметрами

        data_result = cursor.fetchall()  # Извлекаем все строки из результата запроса

        print(f"Не обнаружено в базе данных =>> {read}")

db.close()
