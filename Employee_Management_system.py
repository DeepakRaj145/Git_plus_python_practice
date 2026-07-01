class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
        
    def display_employee_details(self):
        print(f'Employee Id : {self.emp_id}')
        print(f'Employee Name : {self.emp_name}')
        print(f'Employee Salary : {self.salary}')   
        
emp1 = Employee(1, 'Deepak', 20000)
emp2 = Employee(2, 'Sarath', 40000)

emp1.display_employee_details()
emp2.display_employee_details()

        