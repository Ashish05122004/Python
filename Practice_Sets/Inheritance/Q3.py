class Employee:
    salary=20000
    increment=10
    @property
    def salaryAfterIncrement(self):
        return (self.salary+(self.salary*self.increment/100))
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,newsalary):
        self.increment= ((newsalary-self.salary)/self.salary)*100
A =Employee()
# print(A.salaryAfterIncrement)
A.salaryAfterIncrement =22000
print(A.increment)