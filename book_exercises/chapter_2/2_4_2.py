#Write a program that asks the user to input 10 integers, and then prints
#the largest odd number that was entered. If no odd number was entered, it should print a message to that effect

i = 1 #initialize while loop
largest_odd = 0

while i<= 10:
    user_input = int(input("Please enter an integer: "))
    if user_input % 2 == 1 and user_input > largest_odd:
        largest_odd = user_input
    i = i + 1

if largest_odd == 0:
    print("No odd numbers")
else:
    print(largest_odd)
