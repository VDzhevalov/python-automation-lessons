# Створіть клас Employee, який має атрибути name та salary.
# Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
# Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників.
# Клас TeamLead повинен мати всі атрибути як Manager (ім('я, зарплата, відділ), '
# а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def __str__(self):
        return Employee.__str__(self) + f", department: {self.department}"

class Developer(Employee):
    def __init__(self, name, salary, prog_lang):
        super().__init__(name, salary)
        self.prog_lang = prog_lang

    def __str__(self):
        return super().__str__() + f", prog_lang: {self.prog_lang}"


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, team_size):
        Manager.__init__(self, name, salary, department)
        self.team_size = team_size

    def __str__(self):
        return Manager.__str__(self) + f", team size: {self.team_size}"


manager = Manager("AA", 2000, "Finance")
dev = Developer("BB", 1500, "Python")
tl = TeamLead("CC", 3000, "Dev team", 10)

print(manager)
print(dev)
print(tl)

