# giving the user input function to enter the string to be manipulated 
str_manip = input("Please enter the sentence: ")
print(str_manip)
print("This sentence has " + str((len(str_manip))) + " characters including spaces in it.")

# using new_character for the replace function to have a character to replace the last character of the string
new_character = "@" 
new_string = str_manip.replace(str_manip[-1], new_character)
print(new_string)

# using the negative string slicing I can print the last 3 characters in reverse no matter what the user inputs
print(str_manip[:-4:-1])

# by slicing the string and defining the characters from "0 to 3" first slice and "-2" in the second slice then leaving the space after the colon blank I can print the first 3 and last 2 letters 
print(str_manip[0:3] + (str_manip[-2:]))