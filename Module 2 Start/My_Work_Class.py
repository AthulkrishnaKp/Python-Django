class person:
    def __init__(self, v, n):
        self.vid = v
        self.name = n
    def display(self):
        print("Voterd id :", self.vid)
        print("Name id :", self.name)
class employee(person):
    def __init__(self, v, n, s):
        super().__init__(v, n)
        self.salary = s
    def display(self):
        super().display()
        print("Salary is :", self.salary)


emp1 = employee(123, 'Athul', 12000)
emp1.display()
