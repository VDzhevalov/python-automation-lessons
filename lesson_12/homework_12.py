class Rhombus:

    def __init__(self, a, alpha):
        self.__validation_a(a)
        self.__validation_alpha(alpha)
        self.__dict__["a"] = a
        self.__dict__["alpha"] = alpha
        self.__beta = 180 - self.alpha

    def __setattr__(self, name, value):
        if name == "a":
            self.__validation_a(value)
            self.__dict__[name] = value
        elif name == "alpha":
            self.__validation_alpha(value)
            self.__dict__[name] = value
            self.__beta = 180 - self.alpha
        else:
            super().__setattr__(name, value)

    def __validation_a(self, a):
        if not isinstance(a, int) or a <= 0:
            raise ValueError("Incorrect value a:  should be a number,  should be great than 0")

    def __validation_alpha(self, alpha):
        if not isinstance(alpha, int) or alpha <= 0 or alpha >= 180:
            raise ValueError("Incorrect value alpha:  should be a number,  should be great than 0 and less than 180")

    def get_side_size(self):
        return self.a

    def get_angle_alpha(self):
        return self.alpha

    def get_angle_beta(self):
        return self.__beta

    def __str__(self):
        return f"Rhombus with side a= {self.a}, angle alpha= {self.alpha}, angle beta= {self.__beta}"

"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_num(a, b):
    if isinstance(a, int)  and isinstance(b, int):
        return a + b
    else:
        return 0


def photo_paginator(*, amount_of_photos, pages_capacity):
    """Розрахунок кількості сторінок для фото згідно з їхньою місткістю
    Приймає: загальну кількість фото, та місткість сторінки.
    Повертає: кількість необхідних сторінок"""

    if not isinstance(amount_of_photos, int) or not isinstance(pages_capacity, int):
        raise TypeError("value should be a number")

    if amount_of_photos < 1 or  pages_capacity < 1:
        raise ValueError ("value can't be less than 1" )

    if amount_of_photos % pages_capacity > 0:
        return amount_of_photos // pages_capacity +1
    return amount_of_photos // pages_capacity