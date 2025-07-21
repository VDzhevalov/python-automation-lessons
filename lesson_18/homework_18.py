'''
Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
'''

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

for num in even_numbers(10):
    print(num)

def fibonacci_up_to(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

for num in fibonacci_up_to(20):
    print(num)


'Реалізуйте ітератор для зворотного виведення елементів списку.'

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value

items = [1, 2, 3, 4, 5]
for item in ReverseIterator(items):
    print(item)


'Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.'
class EvenRangeIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        return value

for num in EvenRangeIterator(10):
    print(num)

'''
Напишіть декоратор, який логує аргументи та результати викликаної функції.
Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
'''
def log_args_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Виклик {func.__name__} з аргументами: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Результат: {result}")
        return result
    return wrapper

@log_args_and_result
def add(a, b):
    return a + b

add(5, 7)