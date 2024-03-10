# create inputs for the user to enter three randon mubers 
num1 = int(input("Please enter a random number: "))

num2 = int(input("Please enter another random number: "))

num3 = int(input("Please enter a final random number: "))

# then work out and print the sum of all the user entered numbers 

sum_of_all = (num1 + num2 + num3)

print(f"the sum of all is: {sum_of_all}")

# next subtract and print the outcome for the first number minus the second number
sum_subtract = (num1 - num2)
print(f"the sum number 1 minus number 2 is: {sum_subtract}")

# work out and print the third number multiplied by the first number
sum_multiply = (num3 * num1)
print(f"the sum number 3 multiplied by number 1 is: {sum_multiply}")

# finally work out and print the sum of all numbers divided by the third number 
sum_all_then_divide = (sum_of_all / num3)
print(f"the sum of all numbers, divided by number 3 is: {sum_all_then_divide}")