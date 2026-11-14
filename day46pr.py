class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showdetails(self):
        print("Role:", self.role)
        print("Department:", self.dept)
        print("Salary:", self.salary)    
class engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "Development", 60000)



e1 = Employee("Manager", "HR", 50000)
e1.showdetails()

e2 = engineer("Alice", 30)
e2.showdetails()