# using input commands - as the user to input their: name, age, house number and street name
# using this data - print this out into a readable sentence
# I will need to convert the and and house number digits into the string using the str() function 

name = (input("please enter your name: "))
age = (input("please enter your age: "))
house_no = (input("please enter your house number: "))
street = (input("please enter your street name: "))

print("This is " + name + ". They are " + str(age) + " years old, and they live at number " + str(house_no) + " " + street + "!")