'''
#Finding circumference of a circle
import math
r = float(input("Enter the radius of the circle:"))
Circumference = 2 * math.pi * r
print(f"The circumference of a circle is: {round(Circumference, 2)} cm")

#Finding area of a circle
import math
r = float(input("Enter the radius of a circle:"))
Area = math.pi * pow(r,2)
print(f"The area of a circle is: {round(Area, 2)} cm")

#finding hypotenuse of the right triangle
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
hypotenuse = math.sqrt(pow(a,2)+pow(b,2))
print(f"The hypotenuse of the triangle is {hypotenuse}")
'''