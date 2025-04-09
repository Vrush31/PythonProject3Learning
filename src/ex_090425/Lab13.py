# program to find max between 3 number

# input->  3 int
# o/p-> int
# here we have 2 condition more thanone so using here
# if elif else

num1 = int(input("Enter the number1\n"))
num2 = int(input("Enter the number2\n"))
num3 = int(input("Enter the number3\n"))

if num1 > num2 and num1 > num3:
    print("Maximum is ", num1)
elif num2 > num3 and num2 > num1:
    print("Maximum is", num2)
else:
    print("Maximum is", num3)
