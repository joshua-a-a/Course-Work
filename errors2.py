# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
# runtime error: missing quotations around Lion so it was counted as a variable, not a string
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth."
# logical error: the above string should have preceded an "f" to make use of the function in the string
# logical error: the number_of_teeth and animal_type variables needed swapping, as "it is a 16 and it has cub teeth" would appear
print(full_spec)
# syntax error: missing parenteses