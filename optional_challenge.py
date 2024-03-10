# optional task example of a logical and runtime error

# open while loop for user to enter whole number and convert to integer
while True: 
    user_input = input("Please enter a positive whole number: ")
    user_input = int(user_input)
     

# if users input is whole positive number then print thanks for donation message
    if user_input <= 0: 
        # logical error: as the greater than > sign should be there, not the less than <
        print(f"Thanks, for the £{user_input} donation!") 
# elif isers input is invalid print error message and break      
    elif ValueError:
        print(f"You entered {user_input} Please try again") 
        break
# else break loop
    else: 
        print("Well done if you managed this...")  
        break

# the example of a runtime error on this code, is entering letters into the user input.
# This causes a ValueError, but because the value is a string and no defensive programming is
# in place, the string cant be cast as an integer
       