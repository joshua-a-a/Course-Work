# turn all inputs into intergers to set up formula later and import math for square root
import math

# ask user to input seperatly the 3 sides to a triangle
side1 = int(input("Please enter the length of the first side of the triangle: "))
side2 = int(input("Please enter the second side: "))
base = int(input("Please enter the base length: "))
# work out perimiter (sum_of_all) to allow for working out area
sum_of_all = (side1 + side2 + base)
print(sum_of_all)
# working out 1/2 of base length and semi perimeter to complete area formula
# using formula for scaline triangle as then any sized triangle can be worked out 
x = base / 2
y = sum_of_all / 2 
area = x * y 
print(area)
# using math.sqrt to determine square root as it is simpler
print(float(math.sqrt(area)))