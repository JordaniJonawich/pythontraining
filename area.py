PI = 3.1416


def calculate_circle_properties(radius):
   
    circumference = 2 * PI * radius
    
    area = PI * radius * radius
    
    return round(circumference, 2), round(area, 2)


radius = float(input())


circumference, area = calculate_circle_properties(radius)


print(f"The circumference of the circle is: {circumference}")
print(f"The area of the circle is: {area}")
