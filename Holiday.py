
# take user input for : 
    # city_flight , num_nights , rental_days

city_flight = {"Bangkok"  : 1000, 
               "Paris"    : 400,
               "Madrid"   : 600,
               "Kingston" : 800
               }

city_flight = input("Where will you be flying to? \n1. Bangkok, \n2. Paris, \n3. Madrid, \n4. Kingston. \nEnter here: ")
city_flight = city_flight.capitalize()
num_nights = int(input("\nHow many nights will you need a hotel? "))
rental_days = int(input("\nHow many days will you rent a car for?: "))

# create the following four functions : 

# 1: hotel_cost with the argument (num_nights)

def hotel_cost(num_nights):
    return num_nights * 100 # this is the cost of the hotel per night 

# 2: plane_cost with the argument (city_flight)

def plane_cost(city_flight):
    ticket = 0 # the value of the ticket will vary depending on the chosen city travelling to 

    while True:
            
        if city_flight == "Bangkok": # lets the user enter the city name or the number associated 
            ticket = 1000
            return ticket
        elif city_flight == "Paris":
            ticket = 400
            return ticket

        elif city_flight == "Madrid":
            ticket = 600
            return ticket

        elif city_flight == "Kingston":
            ticket = 800
            return ticket
        
        elif TypeError: 
            print("That isn't the name of a city! Try again :)")
            return False
        
        else:
            print("You have selected an invalid option. Try again :)")
            return False            

# 3: car_rental with the argument (rental_days)

def car_rental(rental_days):
    return rental_days * 50

# Print out all the details about the holiday in a readable way

def holiday_cost(num_nights, city_flight, rental_days):
    num_nights = hotel_cost(num_nights)
    city_flight = plane_cost(city_flight)
    rental_days = car_rental(rental_days)
    
    print(f"\nYour flight will cost: £{city_flight}. \nYour hotel cost is: £{num_nights}. \nAnd your car rental will cost: £{rental_days}.\n")
    return num_nights + city_flight + rental_days

total = holiday_cost(num_nights, city_flight, rental_days)

print(f"The total of the holiday comes to: £{total}")