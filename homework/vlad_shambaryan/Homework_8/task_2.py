import sys
sys.set_int_max_str_digits(30000)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()

for _ in range(4):
    next(fib_gen)
fifth = next(fib_gen)
print(f"Пятое число Фибоначи: {fifth}")

for _ in range(194):
    next(fib_gen)
two_hundredth = next(fib_gen)
print(f"Двухсотое число Фибоначи: {two_hundredth}")

for _ in range(800):
    next(fib_gen)
thousandth = next(fib_gen)
print(f"Тысячное число Фибоначи: {thousandth}")

for _ in range(100000):
    next(fib_gen)
hundred_thousandth = next(fib_gen)
print(f"Стотысячное число Фибоначи: {hundred_thousandth}")
