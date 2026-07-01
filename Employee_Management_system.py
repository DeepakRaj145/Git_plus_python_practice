class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
        
    def display_employee_details(self):
        print(f'Employee_Id : {self.emp_id}')
        print(f'Employee Name : {self.emp_name}')
        print(f'Employee Salary : {self.salary}')   
    
    def annual_salary(self):
        print(f'Annual Salary : {self.salary * 12}')
    
    def annual_increment(self, percentage):
        increment = self.salary * percentage/100
        self.salary += increment
        print(f'Annual Increament Salary {int(self.salary *12)}')
emp1 = Employee(1, 'Deepak', 20000)
emp2 = Employee(2, 'Sarath', 40000)

emp1.display_employee_details()
emp1.annual_salary()
emp1.annual_increment(20)

emp2.display_employee_details()
emp2.annual_salary()
emp2.annual_increment(10)

        