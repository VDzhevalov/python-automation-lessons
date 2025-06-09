# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
# Невпевнений, що зрозумів завдання вірно

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier * number < 25:
        result = number * multiplier
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1
        # десь тут помила, а може не одна
        # if  result > 25:
        #     # Enter the action to take if the result is greater than 25
        #     continue
        # print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        # multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_num(a, b):
    if isinstance(a, int)  and isinstance(b, int):
        return a + b
    else:
        return 0

print(sum_two_num(4,6))
print(sum_two_num("4",6))
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(*arg):
    return sum(arg)/len(arg)

print(f"середнє арифметичне= {average(2, 5, 11, 2)}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def string_reverse(string):
    if isinstance(string, str):
        return string[::-1]
    return "Not  a string!"

original_string = "test"
print(f"Оригінал: {original_string},  Зворотній порядок: {string_reverse(original_string)}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.

Насправді постановка завдання не враховує, що може бути декілька слів з однаковою довжиною, тому ось я трішки доробив, та виводжу 
всі слова максимальної довжини, у разі якщо вона співпадає 
"""
def longest_word(*words):
    """Функція приймає список слів та повертає найдовші слова у списку.
    Сортує за довжиною. Останнє слово буде мати найбільшу довжину.
    Перевіряємо чи є в списку ще слова довжина яких дорівнює довжині останнього слова, та виводимо їх.
    Приймає: послідовність слів у вигляді списку
    Повертає: список найдовших слів у вигляді словника"""
    sorted_words = sorted(list(words), key=len)
    return [el for el in sorted_words if len(el) == len(sorted_words[len(sorted_words)-1])]

print(longest_word("a", "ab", "abcd", "abc", "af", "abcd", "xsad"))

# task 6
""" Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    if str1.count(str2) > 0:
        return str1.index(str2)
    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

"""Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
"""

def waiting_for_character(users_input, searched_character):
    """Функція яка перевіряє рядок на наявність певного символу 'searched_character'.
    Приймає: рядок 'users_input' та символ 'searched_character'
    Повертає: True або False"""
    return users_input.lower().find(searched_character) == -1

counter = 1;
while waiting_for_character(input("Або ти введеш шось з літерою 'h', або я від тебе не відчеплюсь: "), "h"):
    print("Давай ще разочок")
    counter += 1;

if 1 == counter:
    print(f"Ти ще норм впорався, всього {counter} спроба")
elif counter < 5:
    print(f"Ти ще норм впорався, всього {counter} спроби")
else:
    print(f"Добре, я нікому не скажу, що ти витратив на це {counter} спроб")

# task 8
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

def total_seas_area(*, first_sea_area, second_sea_area):
    """Розрахунок загальної площі двох морів
    Приймає: площу цільових морів
    Повертає: сумарну площу """
    return first_sea_area + second_sea_area

black_sea_area = 436402
azov_sea_area = 37800
total = total_seas_area(first_sea_area = black_sea_area, second_sea_area = azov_sea_area)
print(f"Площа Чорного та Азовського моря разом = {total} км2")

# task 9
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

def total_cost_calculator(products):
    """Функція розрахунок загальної вартості замовлення:
    Приймає: словник з назв продуктів, та значеннями у формі їх ціни, та кількості кожного продукту.
    Повертає: загальну суму результатів перемноження ціни продукту на кількість"""
    total = 0;
    for cost in products.values():
        total += int(cost[0])*int(cost[1])
    return total

def product_printer(products):
    """Функція роздруковує в зручному вигляді замовлені продукти
    Приймає: словник з назв продуктів, та значеннями у формі їх ціни, та кількості кожного продукту,
    Повертає: список у Вигляді Продукт: 'назва', ціна: 'ціна', кількість: 'кількість' """
    result = []
    for key, val in products.items():
        result.append(f"Продукт: {key}, за ціною: {val[0]}, в кількості: {val[1]}")
    return result

all_products = {"pizza_big": (274, 3), "pizza_middle": (218, 2), "juice": (35, 4), "cake": (350, 1), "water": (21, 3)}

print(f"Всього замовлено= {product_printer(all_products)}")
print(f"Ціна за все щастя разом= {total_cost_calculator(all_products)}")


# task 10
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

def photo_paginator(*, amount_of_photos, pages_capacity):
    """Розрахунок кількості сторінок для фото згідно з їхньою місткістю
    Приймає: загальну кількість фото, та місткість сторінки.
    Повертає: кількість необхідних сторінок"""
    if amount_of_photos % pages_capacity > 0:
        return amount_of_photos // pages_capacity +1
    return amount_of_photos // pages_capacity

print(f"Ігорю потрібно {photo_paginator(amount_of_photos = 232, pages_capacity = 8)} сторінок. ")

