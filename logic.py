# this is my example of a logic error in programming 

# the user enters their choice of an animal noise
animal_greeting = input("Hello animal! Before you enter my house, what noise do you make? ")

# if the user enters the specific phrase "meow" then they will be given the print Get away, feline! 
if animal_greeting in ["meow"]:
	print("Get away, feline!.")

# if the user enters anything else then they will be welcomes 
else:
	print("Welcome to anyone but ferocious felines!")

# however if the user enters "Meow" "MEOW" or similar variations with a capital then they 
# will bypass the if statement to prevent this I would add a line under the first variable  
# "animal greeting" that would change the users input into all lower case, to prevent the
# pesky cats from getting in!
    
