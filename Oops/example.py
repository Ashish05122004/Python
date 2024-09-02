class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getDetails(self,s):
        print(self.name,s)
    @staticmethod
    def greet():
        print("Hello friends.")

ob = A("ashish",20)
ob.getDetails(2000)
ob.greet()