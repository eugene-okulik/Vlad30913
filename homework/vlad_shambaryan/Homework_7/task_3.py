def extract_and_add_10(result_str):
    parts = result_str.split(':')
    number = int(parts[1].strip())
    return number + 10

results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for result in results:
    print(extract_and_add_10(result))
