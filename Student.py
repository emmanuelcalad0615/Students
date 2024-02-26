class Student:
    def __init__(self, name: list, age: list, grades: list):
        self.name: list = name
        self.age: list = age
        self.grades: list = grades


    def add_grade(self, numero):
        self.grades.append(numero)

    def average_grade(self):
        for i in range(0, self.grades):
    


