

city_list = {"Bangkok": 1000, "Paris": 400, "Madrid": 600, "Kingston": 800}

def city_flight():
    while True:
        city = input("Please enter your destination city: ")
        city = city.capitalize()
        if city in city_list:
            return city_list[city]
        else:
            print("Invalid city. Please choose from the following cities: ", ', '.join(city_list.keys()))

def hotel_cost():
    num_nights = int(input("How many nights will you be staying? "))
    return num_nights * 70

def car_rental():
    rental_days = int(input("How many days will you be renting a car? "))
    return rental_days * 50

def holiday_cost():
    plane_cost = city_flight()
    hotel_cost_value = hotel_cost()
    car_rental_cost = car_rental()
    total = plane_cost + hotel_cost_value + car_rental_cost
    print(f"\nYour flight will cost: £{plane_cost}. \nYour hotel cost is: £{hotel_cost_value}. \nAnd your car rental will cost: £{car_rental_cost}.\n")
    print(f"The total of the holiday comes to: £{total}")

# Call the function
holiday_cost()