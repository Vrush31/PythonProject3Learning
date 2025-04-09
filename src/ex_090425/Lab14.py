# Pogramm for grade calculator
# Calculates  and display the letter grades for given score
# A = 90-100
# B = 80-89
# C = 70-79
# D = 60-69
# F = 0-59

# Logic
# step 1
# input > int
# o/p > int or str with the mark

Marks = int(input(" Enter  your Marks\n"))

if Marks >= 90 and Marks <= 100:
    print("Grade is", "A")
elif Marks >= 80 and Marks <= 89:
    print("Grade is", "B")
elif Marks >= 70 and Marks <= 79:
    print("Grade is", "C")
elif Marks >= 60 and Marks <= 69:
    print("Grade is", "D")
else:
    print("Grade is", "F", "You are failed")

