class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        #self.percentage = str((phy + chem + math) / 3) + "%"

    # def calculate_percentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

student1 = Student(90, 80, 70)
print(student1.percentage)

student1 = Student(85, 75, 65)
student1.phy = 99
print(student1.phy)
print(student1.percentage)