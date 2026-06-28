from datetime import date
date1 = date.today()
print(date1)
year = int(input("enter your birthday year in YYYY form "))
month = int(input("enter your briday mont in MM form "))
day = int(input("enter your birday day in DD form "))
date2 = date(year, month, day)
difference = date1 - date2
print(difference)