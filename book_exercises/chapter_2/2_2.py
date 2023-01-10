#Write a program that examines 3 variables, x, y, and z
#and prints the largest odd number among them. If none of them
#are odd, it should print a message to that effect

x = 2
y = 4
z = 6

xIsOdd = x%2
yIsOdd = y%2
zIsOdd = z%2

if xIsOdd+ yIsOdd + zIsOdd == 0:
    print("Sorry there are no odd numbers")
#if there are any odd numbers
elif xIsOdd + yIsOdd + zIsOdd == 3: #All odd numbers
    if x >= y and x >= z:
        print(x)
    elif y >= x and y>= z:
        print(y)
    elif z >= x and z >= y:
        print(z)
elif xIsOdd + yIsOdd + zIsOdd ==2: #2 odd numbers
    if xIsOdd and yIsOdd:
        if x > y:
            print(x)
        else:
            print(y)
    elif xIsOdd and zIsOdd:
        if x>z:
            print(x)
        else:
            print(z)
    else:
        if x>y:
            print(x)
        else: 
            print(y)
elif xIsOdd + yIsOdd + zIsOdd == 1:
    if xIsOdd:
        print(x)
    elif yIsOdd:
        print(y)
    else:
        print(z)
    
