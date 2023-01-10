# Replace comment with a while loop
numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
#concatenate X to toPrint numX times
i = 0
while i < numXs:
    toPrint = toPrint + 'X'
    i = i + 1
print(toPrint)