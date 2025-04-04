import random


salary = int(input("Введите вашу зарплату: "))

bonus = random.choice([True, False])

if bonus:
    bonus_amount = random.randint(0, 5000)
    salary += bonus_amount

print(f'${salary}')

import random  # Импортируем модуль random для генерации случайных чисел

# Запрашиваем у пользователя ввод зарплаты и преобразуем в целое число
salary = int(input("Введите вашу зарплату: "))

# Генерируем случайное значение для бонуса (True или False)
bonus = random.choice([True, False])

# Проверяем, был ли получен бонус
if bonus:
    # Генерируем случайную сумму бонуса от 0 до 5000
    bonus_amount = random.randint(0, 5000)
    # Добавляем сумму бонуса к зарплате
    salary += bonus_amount

# Выводим итоговую зарплату
print(f'${salary}')
