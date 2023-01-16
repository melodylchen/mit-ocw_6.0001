""""In Part B, you had a chance to explore how both the percentage of your salary that you save each month 
and your annual raise affect how long it takes you to save for a down payment.  This is nice, but
suppose you want to set a particular goal, e.g. to be able to afford the down payment in three years.
How much should you save each month to achieve this?  In this problem, you are going to write a 
program to answer that question.  To simplify things, assume:
3
1. Your semi­annual raise is .07 (7%)
2. Your investments have an annual return of 0.04 (4%)  
3. The down payment is 0.25 (25%) of the cost of the house 
4. The cost of the house that you are saving for is $1M.
You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 
36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of 
the required down payment. 
In ps1c.py, write a program to calculate the best savings rate, as a function of your starting salary.
You should use bisection search to help you do this efficiently. You should keep track of the number of 
steps it takes your bisections search to finish. You should be able to reuse some of the code you wrote
for part B in this problem.  
Because we are searching for a value that is in principle a float, we are going to limit ourselves to two
decimals of accuracy (i.e., we may want to save at 7.04% ­­ or 0.0704 in decimal – but we are not 
going to worry about the difference between 7.041% and 7.039%).  This means we can search for an
integer between 0 and 10000 (using integer division), and then convert it to a decimal percentage
(using float division) to use when we are calculating the current_savings after 36 months. By using
this range, there are only a finite number of numbers that we are searching over, as opposed to the
infinite number of decimals between 0 and 1. This range will help prevent infinite loops. The reason we
use 0 to 10000 is to account for two additional decimal places in the range 0% to 100%. Your code
should print out a decimal (e.g. 0.0704 for 7.04%).
Try different inputs for your starting salary, and see how the percentage you need to save changes to
reach your desired down payment.  Also keep in mind it may not be possible for to save a down
payment in a year and a half for some salaries. In this case your function should notify the user that it 
is not possible to save for the down payment in 36 months with a print statement. Please make your
program print results in the format shown in the test cases below.   
Note: There are multiple right ways to implement bisection search/number of steps so your
results may not perfectly match those of the test case. 
Hints
● There may be multiple savings rates that yield a savings amount that is within $100 of the
required down payment on a $1M house. In this case, you can just return any of the possible
values.
● Depending on your stopping condition and how you compute a trial value for bisection search,
your number of steps may vary slightly from the example test cases.
● Watch out for integer division when calculating if a percentage saved is appropriate and when
calculating final decimal percentage savings rate.
● Remember to reset the appropriate variable(s) to their initial values for each iteration of bisection
search.
Test Case 1 
>>>  
Enter the starting salary: 150000
Best savings rate: 0.4411  
Steps in bisection search: 12 
>>>
4
Test Case 2 
>>>  
Enter the starting salary: 300000
Best savings rate: 0.2206 
Steps in bisection search: 9 
>>>
Test Case 3 
>>>  
Enter the starting salary: 10000
It is not possible to pay the down payment in three years."""

#Implement bisection search with guess and check

#Request information from user
annual_salary = float(input("Enter your annual salary:"))

#State constants
r = 0.04 #rate of retun is 4%
total_cost = float(1000000) #Total cost of house is 1M
months_to_save = 36
epsilon = float(100) #epsilon for bisection search, being within 100 is 'good enough'
portion_down_payment = 0.25 #25% neeed for downpayment
semi_annual_raise = 0.07


#initialize a few variables
num_steps = 0 #number of steps for bisection search

#implement bisection search
low = 0
high = 10000
guess = (low+high)//2


while True: 
    current_savings = 0
    annual_salary_iterate = annual_salary
    for months in range(months_to_save+1):
        if months != 0 and months % 6 ==0:
            annual_salary_iterate = annual_salary_iterate*(float(1)+semi_annual_raise)
        current_savings = current_savings + current_savings*r/12.0 + (guess/10000.0)*annual_salary_iterate/12.0
    if high - low == 1:
        print("Sorry it is impossible")
        break
    elif abs(current_savings - total_cost*portion_down_payment) <= epsilon:
        print("Best savings rate:",guess/10000.0,"\nSteps in bisection search:",num_steps )
        break
    elif current_savings < total_cost*portion_down_payment:
        low = guess
    else:
        high = guess
    guess = (low+high)//2
    num_steps += 1


