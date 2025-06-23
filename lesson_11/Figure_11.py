# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod
from math import pi

class Figure(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f"Perimeter is {self.perimeter()}. Area is {self.area()}."

class Square(Figure):

    def __init__(self, side):
        self.__side = side

    def perimeter(self):
        return 4 * self.__side

    def area(self):
        return self.__side ** 2

    def __str__(self):
        return super().__str__() + f" This is Square with side: {self.__side}"


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def perimeter(self):
        return 2 * pi * self.__radius

    def area(self):
        return pi * (self.__radius)**2

    def __str__(self):
        return super().__str__() + f" This is Circle with radius: {self.__radius} "

for i in range(1, 10):
    print(Circle(i))
    print(Square(i))
