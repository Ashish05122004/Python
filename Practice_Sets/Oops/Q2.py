class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(self.n*self.n)    
    def cube(self):
        print(self.n*self.n*self.n)    
    def root(self):
        print(self.n**1/2) 
    @staticmethod
    def greet():
        print("Hello")   
c =calculator(9)
c.square()
c.cube()
c.root()
c.greet()