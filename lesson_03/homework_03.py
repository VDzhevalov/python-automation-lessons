alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n\
"That depends a good deal on where you want to get to," said the Cat.\n\
"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"\
—— so long as I get somewhere," Alice added as an explanation.\n\
"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

for  ch in alice_in_wonderland:
    if ch == "'":
      print(ch)
print(alice_in_wonderland.count("'"))

print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + black_sea_area
print(f"Площа Чорного та Азовського моря разом = {total_area} км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods_amount = 375291
first_warehouse = total_goods_amount - 222950
second_warehouse = 250449 - first_warehouse
third_warehouse  = total_goods_amount- (first_warehouse + second_warehouse)

print(f"first_warehouse = {first_warehouse}, second_warehouse = {second_warehouse}, third_warehouse  = {third_warehouse}")
if total_goods_amount == (first_warehouse + second_warehouse + third_warehouse):
    print(f"Все вірно разом це=  {first_warehouse + second_warehouse + third_warehouse}")
else:
    print("Щось пішло не так")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
months = 12 + 12/2
total_price = 1179 * months;
print(f"Всього: {total_price}")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("Остача від ділення:")
print(f"a) 8019 : 8 = {8018 % 8}   d) 7248 : 6 = {7248 % 6}")
print(f"b) 9907 : 9 = {9907 % 9}   e) 7128 : 5 = {7128 % 5}")
print(f"c) 2789 : 5 = {2789 % 5}   f) 19224 : 9 = {19224 % 9}")

# task 08
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
pizza_big = 274
pizza_middle = 218
juice = 35
cake = 350
water = 21
#Дужки не обов'язкові, але так простіше сприймати
total_price = (pizza_big * 3) + (pizza_middle  * 2) + (juice * 4) + 350 + (21 * 3)
print(f"Ціна за все щастя разом= {total_price}")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
pages_capacity = 8
photos = 232
if photos % pages_capacity > 0:
    print(f"Ігорю потрібно {photos // pages_capacity +1} сторінок. ")
    photos / pages_capacity +1
else:
    print(f"Ігорю потрібно {photos // pages_capacity} сторінок. ")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
total_distance = 1600
tank_capacity = 48
fuel_consumption = (1600 * 9) / 100
stops_count = fuel_consumption / 48
print(f"fuel_consumption = {fuel_consumption}\nstops_count= {stops_count}")
