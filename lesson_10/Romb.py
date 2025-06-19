class Romb:
    def __init__(self, a, alpha):
        self.__validation_and_set_values(a, alpha)

    def __validation_and_set_values(self, a, alpha):
        try:
            if int(a) <= 0:
                raise Exception("Incorrect value: a should be great than 0")
            elif  int(alpha) <= 0:
                raise Exception("Incorrect value: alpha should be great than 0")
            elif int(alpha) >= 180:
                raise Exception("Incorrect value: alpha should be less than 180")
            else:
                self.a = a
                self.alpha = alpha
                self.__beta = 180 - alpha
        except ValueError:
            raise ValueError("Incorrect value: should be a number")

    def get_side_size(self):
        return self.a

    def get_angle_alpha(self):
        return self.alpha

    def get_angle_beta(self):
        return self.__beta

    def __str__(self):
        return f"Romb with side a= {self.a}, angle alpha= {self.alpha}, angle beta= {self.__beta}"

romb = Romb(100, 30)
print(romb)