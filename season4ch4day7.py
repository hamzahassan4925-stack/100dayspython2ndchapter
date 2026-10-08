#dictionary and set
info = {
    "name": "hassan",  
        "age": "25",
      "learning":"Python",


}
print(info)
#we also use tuples in dictionary
print(info["name"])
print(type(info))
#they are unorderd
#dont allow duplicate values
#mutable
print(info["learning"])
info["name"] = "hassan ali"
#we also add new key value pair in dictionary
info["city"] = "lahore"
info["country"] = "newzeland"
print(info)
#we cant use old key to add new value in dictionary
#we also creat null dictionary
null_dict = {     }
print(null_dict)