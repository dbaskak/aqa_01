def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i


# for num in even_numbers_generator(10):
#     print(num)


def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


# for num in fibonacci_generator(10):
#     print(num)


class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lst[self.index]


# my_list = [1, 2, 3, 4, 5]
# for item in ReverseIterator(my_list):
#     print(item)


class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        current_value = self.current
        self.current += 2
        return current_value


# for num in EvenIterator(10):
#     print(num)

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function recall {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper


# @log_decorator
# def add(a, b):
#     return a + b
#
#
# add(5, 10)


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Some error appears: {e}")
    return wrapper


# @exception_handler
# def divide(a, b):
#     return a / b
#
#
# divide(10, 0)
