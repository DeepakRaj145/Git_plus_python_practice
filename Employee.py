class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def display(self):
        return f'Employee Name : {self.name}, Employee ID : {self.id}'
    
emp1 = Employee('Deepak', 101)
emp2 = Employee('Sarath', 102)

print(emp1.display())
print(emp2.display())