"""Example below for using the in operator to iterate over a string
total = 0
for c in '12345678':
    total = total + int(c)
print(total)
print(sum(range(1,9)))
-> Output for both is 36
"""
#Exercise - let s be a string that contains a sequence of decimal numbers
#separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that
#prints the sum of the numbers in s

s = '1.23,2.4,3.123'
sum = 0
pointer_for_str = 0
#print(len(s))
for b in range(0, len(s)):
    if s[b] == ',' and b< len(s) -1 :
        # should be (0,4), (5,8)
        #print("This is a float", pointer_for_str, b)
        c = s[pointer_for_str:b] 
        sum = sum + float(c)
        pointer_for_str = b + 1
    elif b == (len(s)-1):
        b = b + 1
        #should be (9, 13)
        #print("last float", pointer_for_str, b)
        c = s[pointer_for_str:b]
        sum = sum + float(c)
        break
    #print('This is the increment', pointer_for_str, b)
print(sum)

