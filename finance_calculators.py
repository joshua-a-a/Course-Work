# This program will run a finance calculator that will allow the user to an investment calculator and a home loan repayment calculator in the same place
# first import math - to aid with calculation simplicity 

import math

# define vairables and create an input for the user to select of the two calculators - investment, and home lone repayment
# use if-elif-else statement to allow user to type investment or bond however they want
# let users be flexible with typing ie: use of capitals not to prevent progres of user
while True:
    
    print("\ninvestment - to calculate the amount of interest you'll earn on your investment")
    print("\nbond       - to calculate the amount you'll have to pay monthly on a home loan\n")
    
    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

    choice = choice.lower()
    choice = choice.strip()
    
    if (choice == "investment"):
        print("\nYou have chosen the investment calculator.\n")
        
        invest_value = float(input("How much will you invest? (eg: 100000): "))

        invest_percent = float(input("Your interest rate %: "))
        invest_percent_conversion = invest_percent / 100
        
        invest_years = float(input("How many years will you be investing for?: "))
        
        interest = input("which interest type? (Compound/Simple): \n")

        interest = interest.lower()
        interest = interest.strip()

    #this is simply using the provided formula, along side using booleans, to get the inputs turned into variables
    #and to translate them into the formula for simple and compound interest 
        
        if (interest == "simple"):
            
            simple_interest = invest_value * (1 + invest_percent_conversion * invest_years)
            print(f"Your return will be: £{simple_interest}\n")
            break 
# using the if elif and else statements I can branch further out being able to create more inputs, questions and then revert back to the top        
        elif (interest == "compound"):
            
            compound_interest = invest_value * (math.pow((1+invest_percent_conversion),invest_years))
            print(f"Your return will be: £{compound_interest}\n") 
            break
        
        else: print("invalid input - please retry\n")
#  onto bond - this was very much the same kind of structure but much less complex. 
# using the provided formula, it was just making sure the variables I named did not clash with the earlier formale. then finally formatting by adding new lines and improving redability. 
    elif (choice == "bond"):
        house_value = float(input("What is the value of the house? (eg: 100000): "))
        
        house_percent = float(input("Your interest rate %: "))
        
        house_months = float(input("How many months will you be repaying the bond? (eg: 240): \n"))
        house_percent_conversion = (house_percent / 100) / 12
        
        repayment_rate = (house_percent_conversion * house_value)/(1 - (1 + house_percent_conversion)**(-house_months))
        
        print(f"you will repay £{repayment_rate} every month.\n")
        break
    
    else: print("\ninvalid input - please retry\n")




    
    

    



 

