from datetime import date
date1 = date.today()
print(date1)
year = int(input("enter your birthday year in YYYY form "))
month = int(input("enter your birthday month in MM form "))
day = int(input("enter your birday day in DD form "))
date2 = date(year, month, day)
difference = date1 - date2
weeks = difference.days / 7
months = difference.days / 30
years = difference.days / 365
print(f"{difference} is equal to {weeks} weeks, and is also equal to {months} months, and you are {years} years old!")