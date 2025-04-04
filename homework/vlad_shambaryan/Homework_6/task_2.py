# Перебираем числа от 1 до 100
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FuzzBuzz")
    elif i % 3 == 0:
        print("Fuzz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# Перебираем числа от 1 до 100
for i in range(1, 101):
    # Проверяем, делится ли число на 3 и 5
    if i % 3 == 0 and i % 5 == 0:
        print("FuzzBuzz")  # Выводим "FuzzBuzz", если число делится на 3 и 5
    elif i % 3 == 0:
        print("Fuzz")  # Выводим "Fuzz", если число делится только на 3
    elif i % 5 == 0:
        print("Buzz")  # Выводим "Buzz", если число делится только на 5
    else:
        print(i)  # Выводим само число, если оно не делится ни на 3, ни на 5
