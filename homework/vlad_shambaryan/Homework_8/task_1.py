import random


salary = int(input("Введите вашу зарплату: "))

bonus = random.choice([True, False])

if bonus:
    bonus_amount = random.randint(0, 5000)
    salary += bonus_amount

print(f'${salary}')
