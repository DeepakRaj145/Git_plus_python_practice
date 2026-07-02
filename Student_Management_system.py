class Student:
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f'Student Name is {self.name}')
        print(f'Student Rollno is {self.rollno}')
        print(f'Student Marks is {self.marks}')
        
    def grade(self):
        if self.marks >= 90:
            return f'A'
        
        elif self.marks >= 75:
            return 'B'
        elif sef.marks >=50:
            return f'C'
        else:
            return f'Student is Fail'
        
s1 = Student(1, 'Deepak', 90)
s1.display()
print(f'Student Grade : {s1.grade()}')

s2 = Student(2, 'Saran', 74)
s2.display()
print(f' Student Grade : {s1.grade()}')