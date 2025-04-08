#formating
#format of string
num= 90
print("This is the number you working with "f" {num}")
# it is replacing the value

table= 9
print(f"{table}*1={table}")
print(f"{table}*2={table*2}")
print(f"{table}*3={table*3}")

#task create programe, take  2 inputs num1 and num2  1)make the max num and 2) give the power1 to power 2

num1 = int(input("Enter the number 1"))
num2 = int(input("Enter the number 2"))
maximum= max(num1,num2)
print(maximum)
power= num1 ** num2
print(power)