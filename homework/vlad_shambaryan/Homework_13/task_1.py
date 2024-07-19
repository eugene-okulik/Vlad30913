import os
import datetime


base_file = os.path.dirname(__file__)

homework = os.path.dirname(os.path.dirname(base_file))

data_text = os.path.join(homework, "eugene_okulik", "hw_13", "data.txt")


def file_reader():
    # открываем файл и читаем его
    with open(data_text, "r") as file_list:
        for line in file_list.readlines():
            yield line  # для возврата каждой строки по одной


# список дат из прочитанных строк, обрез строки до нужного формата
lists = [line[2:29].lstrip() for line in file_reader()]

# каждая дата по порядку
for index, date_str in enumerate(lists):
    # текущее время
    now = datetime.datetime.now()
    if index == 0:
        # преобразуем строку в объект datetime
        date_1 = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        # добавляем одну неделю и выводим результат
        print(f"Дата 1 через неделю: {date_1 + datetime.timedelta(weeks=1)}")
    elif index == 1:
        # преобразуем строку в объект datetime
        date_2 = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

        print(f"Дата 2 — это {date_2.strftime('%A')}")
    elif index == 2:
        # преобразуем строку в объект datetime
        date_3 = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        # вычисляем количество дней с текущего момента
        amount_of_days = (now - date_3).days
        # выводим количество дней
        print(f"Дата 3 было {amount_of_days} дней назад.")
