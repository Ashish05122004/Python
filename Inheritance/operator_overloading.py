class Number:
    def __init__(self,n):
        self.n=n
    def __add__(self,x):
        return self.n+x.n
a=Number(2)
b=Number(3)
print(a+b)