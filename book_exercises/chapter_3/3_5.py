# Newton Raphson for Square Root
# Find x such that x**2 -24 is wthin epsilon of 0
epsilon = 0.01
k = 24.0
guess = k/2.0
while abs(guess*guess - k) >= epsilon:
    guess = guess - ((guess**2-k)/(2*guess))
print('Square root of', k, 'is about', guess)

#Add some code to the function above that keeps track of the 
#iterations to find the root from the Newton Raphson method.
# Use that code as a part of a program that compares the efficiency of
# the Newton-Raphson method vs. bisection search

epsilon = 0.01
k = 24.0
guess = k/2.0
num_guesses = 0

#initialize the high and the low for bisection search
high = k
low = 0

while abs(guess*guess - k) >= epsilon:
    num_guesses += 1
    guess = guess - ((guess**2-k)/(2*guess))
print("This is the Newton-Raphson method:")
print('Square root of', k, 'is about', guess, "\nNumber of steps is:", num_guesses)

#Implement via bisection search

epsilon = 0.01
k = 24.0
guess = k/2.0
num_guesses = 0
while abs(guess*guess - k) >= epsilon:
    num_guesses += 1
    if guess*guess < k:
        low = guess
    else:
        high = guess
    guess = (low + high)/2.0
print("This is the bisection search method:")
print('Square root of', k, 'is about', guess, "\nNumber of steps is:", num_guesses)


