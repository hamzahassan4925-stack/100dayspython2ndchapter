class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_average(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("Average marks of student is: ", sum / len(self.marks))    
s1 = Student("hassan babar", [56, 67, 78])
s1.get_average()