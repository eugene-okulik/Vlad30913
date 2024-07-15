
def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        for _ in range(count):
            func(*args, **kwargs)
    return wrapper

@repeat_me
def example(text):
    print(text)

example('print me', count=2)


def repeat_me(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_me(count=2)
def example(text):
    print(text)

example('print me')

