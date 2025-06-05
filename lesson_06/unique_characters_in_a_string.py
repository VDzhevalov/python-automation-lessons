# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

users_input = input("Додайте хоч шось: ")

unique_characters = set(users_input)

if len(unique_characters) > 10:
    print(True)
    print("Кількість унікальних символів: ", len(unique_characters))
else: print(False)
