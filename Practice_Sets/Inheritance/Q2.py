class Animals:
    def __init__(self):
        print("Animal class")
class Pets(Animals):
    def __init__(self):
        super().__init__()
        print("this is pet class")
class Dog(Pets):
    def __init__(self):
        super().__init__()
        print("this is dog class")
    @staticmethod
    def bark():
        print("dogs are barking")
tom = Dog()
tom.bark()