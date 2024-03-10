age = int(input("Please enter your age: "))

if age < 13:
    print("You qualify for the childs discount!")
elif age == 21:
    print("Happy 21st Birthday!")
elif age > 100:
    print("Sorry, you are dead...")
elif age > 64:
    print("Enjoy your retirement!")
elif age > 39 :
    print("You are over the hill!")
else:
    print("Age is but a number!")

