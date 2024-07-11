def extract_and_add_10(result_str):
    # Разделяем строку по ':' и сразу преобразуем вторую часть в число, добавляем 10 и возвращаем результат
    return int(result_str.split(':')[1].strip()) + 10

results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for result in results:
    print(extract_and_add_10(result))

