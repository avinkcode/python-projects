import math
def calc_circumfrence_area():
    print(math.pi)
    R = int(input("enter a radius "))
    Perimeter = 2 * math.pi * R
    Area = math.pi * R * R
    print(f"the area of the circle is: {Area}")
    print(f"the perimeter of the circle is: {Perimeter}")



def calc_rectangle():
    number1 = 5   
    number2 = 7
    perimeter = (number1 + number2) * 2
    area = number1 * number2
    print(f"the area of the rectangle is: {area}")
    print(f"the perimeter of the rectangle is: {perimeter}")



calc_circumfrence_area()
calc_rectangle()