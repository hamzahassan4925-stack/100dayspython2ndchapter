class Student:
    collage_name = "FAST"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome to the class of fast")
    def get_marks(self):
        return self.marks

s1 = Student("hassan babar", 90)
s1.welcome()
print(s1.get_marks())