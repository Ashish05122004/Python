class Employee:
    @property
    def name(self):
        return f"{self.fname}"
    @name.setter
    def name(self,value):
        self.fname =value
    
e= Employee()
e.name="ashish"
print(e.name)