# syntax error found - the first print function is missing parenteses and has a space between print and the string that will be printed
print("Welcome to the error program")
# syntax error is below there is an unnessesary indentation and the print function issame as above with an unnessesary space and missing parentheses   
print("\n")

# syntax error: the 5 rows (8, 9, 10, 13, 14) below are indented when they are not needed to be     
# COMMENT Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # here the variable wasnt being defined due to the equal to "==" being used rather than a single "="
age = int(age_Str) 
print(f"I'm {age} years old.")
# syntax error: format wasnt being used or defined at the start of the string and the {} were not used to add the integer into the variable
# syntax error: removing the use of addition + and additional quotations "" in the print were trying to add the strings using math


# COMMENT Variables declaring additional years and printing the total years of age
years_from_now = 3 # syntax error: removed quotation marks " " to define 3 as an int not str
total_years = age + years_from_now

print(f"The total number of years: {total_years}") 
# syntax error: parentheses not used and unnessesary space between print 
# syntax error: this also needed to be an f string and make use of curly brackets {} to define the correct variable "total_years" NOT "answer_years"

# COMMENT Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12  # syntax error: the total years was not being defined as only "total" had been written
total_months = total_months + 6 # logical error: I added this line in, as the total was coming to 324 months because the extra 6 was not being added
print(f"In 3 years and 6 months, I'll be {total_months} months old") 
# syntax error: parentheses not used and unnessesary space between print and the string
# syntax error: changed the string to be a function string and added curly brackets to the {total months}
# syntax error: also removed the unnessesary quotations "" and addition functions + 

