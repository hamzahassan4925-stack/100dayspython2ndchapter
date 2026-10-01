age_input = input("Enter your age: ")


if age_input.isdigit():
    age = int(age_input)
    if age >= 18:
     print("You are eligible to vote and apply licence.")
    elif age < 18:
        print("You are not eligible to vote and apply licence.")
else:
    print("ok buy go home")










