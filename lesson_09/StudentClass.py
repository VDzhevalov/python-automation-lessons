#Створіть клас студента з атрибутами ім'я, прізвище, вік, та середній бал
#Створіть об'єкт цього класу, представляючий студента.
#Додайте метод до класу "Студент" якій дозволяє змінювати середній бал студента
#Виведить інформацію про студента та змінить його середній бал.

class Student:
    def __init__(self, name, surname, age, aver_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.__aver_grade = aver_grade

    def greet(self):
        return f"Hi, i'm a student. My full name is: {self.name} {self.surname}, i'm {self.age} years old"

    def change_average_grade(self, new_aver_grade):
        self.__aver_grade = new_aver_grade

    def get_average_grade(self):
        return f"My average grade is: {self.__aver_grade}"

student = Student("Vasyl", "Vasylenko", 25, 90)

print(student.greet())
print(student.get_average_grade())

student.change_average_grade(99)
print(student.get_average_grade())