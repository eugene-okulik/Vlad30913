
results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]


def main(result_str):

    return int(result_str.split(':')[1].strip()) + 10


for result in results:
    print(main(result))
