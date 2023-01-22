# Write a function isIn that accepts two strings as arguments
# and returns True if either string occurs anywhere in the other,
# and False otherwise. 
# Hint: you might want to use the built-in str operation in.

def isIn(str1, str2):
    if str1 in str2 or str2 in str1:
        return True
    else:
        return False

x = isIn("eh","eh oh eh ohh")
print(x)

y = isIn("eek","eh oh eh ohh")
print(y)

z = isIn("hohoho hoo HOO","HOO")
print(z)