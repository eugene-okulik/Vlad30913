result1 = "результат операции: 42"
result2 = "результат операции: 514"
result3 = "результат работы программы: 9"

number1 = int(result1[result1.index(':') + 2:])

number2 = int(result2[result2.index(':') + 2:])

number3 = int(result3[result3.index(':') + 2:])

print(number1 + 10, number2 + 10, number3 + 10)

# Строки с результатами операций
result1 = "результат операции: 42"
result2 = "результат операции: 514"
result3 = "результат работы программы: 9"

# Извлечение числовой части из строки result1 и преобразование в целое число
number1 = int(result1[result1.index(':') + 1:])

# Извлечение числовой части из строки result2 и преобразование в целое число
number2 = int(result2[result2.index(':') + 1:])

# Извлечение числовой части из строки result3 и преобразование в целое число
number3 = int(result3[result3.index(':') + 1:])

# Вывод чисел, увеличенных на 10
print(number1 + 10, number2 + 10, number3 + 10)
