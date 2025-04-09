# Conditions and Loop
# syntax
# if condition:
# // code you want to execute if the condition is true
# else condition:
# // code you want to execute if the condition is true

# programm for user can go to club ornot

# logic
# step 1input datatype int
# o/p string
# step 2
# logic- age> 21 - print can go
# age< 21  - print cant go


age = input("Enter your age\n")
age = int(age)

if age > 21:
    print(f"can go the club {age}")
else:
    print(f"Cant go to th club{age}")
