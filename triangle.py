import math


def is_valid_triangle(a, b, c):
    #
    return a + b > c and b + c > a and c + a > b

# Read the lengths of the three sides from the console
a = float(input(""))
b = float(input(""))
c = float(input(""))


if is_valid_triangle(a, b, c):
    
    s = (a + b + c) / 2
    
    
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
   
    print(f"The area of the triangle is: {area:.2f}")
else:
    
    print("Invalid Triangle")
