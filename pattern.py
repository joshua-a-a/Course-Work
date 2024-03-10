# using stars "*" create the pattern below
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# start by defining the * as a variable
star = "*"

# using a for loop define the range and amount of rows the pattern will occur for
for row in range(1,10):
    
# if the row is less than 5 then print the star variable times the rows to get the first part of the pattern
    if row <= 5: 
        print(star * row)
# in the else statement - subtract the total rows (10) by the current row to repeat the pattern backwards
    else:
        print(star * (10 - row))
        

    
    

    
        

    



   



                

