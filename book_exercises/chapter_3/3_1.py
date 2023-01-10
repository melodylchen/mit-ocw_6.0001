# Write a program that asks the user to enter an integer
# and prints out two integers, root and pwr, such that
# 0 < pwr < 6 and root**pwr is equal to the integer
# entered by the user. If no such pair of integers exists,
# it should print a message to that effect


integer = int(input("Please enter an integer: "))
root = 0

while root <= integer:
    power = 1
    while power < 6:
        if root**power == integer:
            print("Root is:", root,"Power is:", power) 
            break
        else:
            power = power + 1
    if root**power == integer:
        break
    else:
        root = root + 1
    
if root ** power  > integer:
    print("There is no root and power combination available")


