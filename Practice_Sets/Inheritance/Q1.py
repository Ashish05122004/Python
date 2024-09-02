class TwoD:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"({self.i}, {self.j})")
class ThreeD(TwoD):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"({self.i}, {self.j}, {self.k})")
ob=ThreeD(1,2,3)
ob.show()  
