def choose_operation(func):
    def wrapper(first, second, *args, **kwargs):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif first < second:
            return func(first, second, '/')
        elif first < 0 or second < 0:
            return func(first, second, '*')
        else:
            return "No valid operation found"
    return wrapper

@choose_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return second / first
    elif operation == '*':
        return first * second
    else:
        return "Division by zero is not allowed."


first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))

result = calc(first_number, second_number)
print(f"Результат операции: {result}")
