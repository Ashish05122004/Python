class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"a={cls.a}")
    def newShow(self):
         print(f"a={self.a}")
e= Employee()
e.a=22
e.show()
e.newShow()