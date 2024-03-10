# here I am using the inputs as floats to allow for the user to input a value equal to seconds
run = float(input("Please enter in MINUTES your total running time: "))
bike = float(input("Please enter in MINUTES your total cycling time: "))
swim = float(input("Please enter in MINUTES your total swimming time: "))

# creating a sum to add all the times together 
total = (run + bike + swim)

# using a function string to print to the user their total time entered
print(f"Your total triathlon time is {total} minutes")

# using if elif and else statements - print the award that the user will recieve depending on their total event time
# if the users time is entered and is a negative number overall, print error message 
if (total < -1) or (total == -1):
    print("Number cannot be negative, sorry that's time traveling!")

# elif statement for users total time to be 100 minutes or less
# using or statement to allow total to be 100 or less
elif (total < 100) or (total == 100):
    print("Congratulations! You have qualified to recieve the PROVINCIAL COLOURS!")

# and statemtent to make sure total for half colours award is printed if time is betweeen 101 and 105 minutes
elif (total > 100) and (total < 105) :
    print("Well done, you are within 5 minutes of the qualifying time! You recieve the PROVINCIAL HALF COLOURS")

# entering 105 needs to print for half colours award 
elif (total == 105):
    print("Well done, you are within 5 minutes of the qualifying time! You recieve the PROVINCIAL HALF COLOURS")

# and statemtent to make sure total for provincial scroll award is printed if time is betweeen 106 and 110 minutes
elif (total > 105) and (total < 111):
    print("Well done, you are within 10 minutes of the qualifying time! You recieve the PROVINCIAL SCROLL")

# using the else statement to print a not qualified message if the time is 111 minutes or over
else:
     print("Sorry, you have not qualified for any awards this time around...")