class Person:
    def __init__(self, name, surname, age, alive=True):
        self.name = name
        self.surname = surname
        self.age = age
        self.alive = alive

    def print_info(self):
        return f"Name {self.name} \nSurname{self.surname} \nAge is {self.age} \nAlive {self.alive}"


class Student(Person):
    def __init__(self, name, surname, age, id_stud, major, alive=True):
        super().__init__(name,surname,age,alive)
        self.id_stud = id_stud
        self.major = major

    def print_info(self):
        super().print_info()


class Child(Person,Student):
    def __init__(self,name,surname,age,major,alive,parents):
        super().__init__(name,surname,age,major,alive)
        self.parents = parents



obj1 = Person("Sagdii", "Rahimov",20,True)
print(obj1)


