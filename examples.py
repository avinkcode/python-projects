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



def day_count():
    year = 365
    week = 7
    day = 1
    user_input = int(input("Choose a amount of days "))
    num_of_year = int(user_input / year)
    remain_day = user_input % year
    num_of_week =  int(remain_day/week)    
    remain_day2 = remain_day % week
    print(num_of_year)
    print(num_of_week)
    print(remain_day2)
day_count()

