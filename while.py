# create a while loop that allows the user to continuiously enter numbers 

total_value = 0 # variable to store total value of the users inputs
total_input = 0 # variable to store the amuount of times the user has input 

# add a users input which will repeat until -1 is entered
# do not allow for users input to be a letter, without the program breaking or returning a value error
# using the else statement - add a +1 to each time the user has entered a number
# also else statement - also add to the total_value what the user has entered
while True:
    user_input = input("\nPlease enter a positive number, or (-1) to exit: ")

    if not user_input.isdigit() and user_input != "-1" : # here I have to also add "-1" to the conditions or it will return as "not a digit"
        print("\nYou have entered a negative number or a letter!\nPlease retry.")
    
    # when user enters -1 the program will continue onto the print statements below 
    # not using continue as there is not another loop to follow on'''
    elif user_input == "-1" : 
        break
    
    else :
        total_input += 1 # adding to the input counter for every time the user correctly inputs a number
        total_value += float(user_input) # adding the users input to the total value entered

print(f"\nThe total value you have entered is: {total_value}") # printed total of users input combined
print(f"Your total inputs are: {total_input}") # print of how many times user input a value
average_sum = total_value / total_input # formula for average sum of value and input
print(f"\nThe average sum is: {average_sum}\n") # printed the average of the users input value and total inputs


# my original rendition of this task (which I asked for help on) was overcomplicated and logically flawed.

# '''my biggest mistakes were that I was adding to the total variables inside the if statement not the else
# also trying to cast the input as an interger/float. So I was recieving value errors
#  when trying to convert them to a string just for the error. I now know best practice for this situation, 
# is start as a string and convert to int/float or I wont be able to return the -1 value and break the loop'''

