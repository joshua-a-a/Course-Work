# here is my example of splitting strings and manipulating the letters and words

first_input = input("Please enter a phrase: ")
letter_even = True # if number is odd then character must be UPPER and if even the character must be lower
first_output = [] # storage variable for finished output

for i in first_input:
    
    # letters with even counted values [2, 4, 6, 8, etc] of input string must be lowercase
    if letter_even:
        first_output.append(i.upper()) # store uppercase input into output variable
        letter_even = False 

    # letters with odd counted values [1, 3, 5, 7, 9, etc] of input string must be UPPERCASE
    else:
        first_output.append(i.lower()) # store lowercase input into output variable
        letter_even = True

first_output = "".join(first_output) # join the list together so output is on one line

print(first_output) # prints eg: 'HeLlO WoRlD' / 'My Py SmElLs gOoD'


second_input = input("Please enter another phrase: ").split() # using split to seperate words in string
word_even = True # if number is even then word must be UPPER and if odd the character must be lower
second_output = [] # storage variable for finished output

for i in second_input:
    
    # words with even counted values [2, 4, 6, 8, etc] of input string must be UPPERCASE
    if word_even:
        second_output.append(i.lower()) # store uppercase input into output variable
        word_even = False 

    # words with odd counted values [1, 3, 5, 7, 9, etc] of input string must be lowercase
    else:
        second_output.append(i.upper()) # store lowercase input into output variable
        word_even = True

second_output = " ".join(second_output) # join the list together so output is on one line

print(second_output) # prints eg: 'hello WORLD' / 'my PY smells GOOD'