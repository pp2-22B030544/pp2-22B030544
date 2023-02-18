import math

number_of_sides= int(input())

length = float(input())
area=(number_of_sides * length ** 2) / (4 * math.tan(math.pi / number_of_sides))

print("Input number of sides: ", number_of_sides)
print("Input the length of a side: ", length)
print ("The area of the polygon is: " ,int(area))