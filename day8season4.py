#dictionary kay ander aik or 
#dictionary dal na ko nested dictionary kehtay hain
from turtle import update


student = {
    "name": "hassan",
    "subjects": {
        "math":90,
        "phy":99,
        "english": 88
    }
}
#nested dictionary
print(student)
print(student["subjects"]["english"])
print(list(student.keys()))
print(len(student))
print(student.values())
print(student.items())
print(student.get("names"))
#cannot return error
print(student.update({"name":"hassan ali"}))
print(student["name"])
print(student.update({"subjects":{"math" :100}}))
print(student["subjects"]["math"])
print(student)