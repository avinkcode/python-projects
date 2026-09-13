budget = input("what is your budget for the month?|$")
budget2 = int(budget)

grocery_expense = int(input("what is your expense for grocery this month?|$"))
car_repairs_expense = int(input("what is your expense for car repairs this month?|$"))
sport_expense = int(input("what is your expense for sports this month?|$"))
class_expense = int(input("what is your expense for classes this month?|$"))
gas_expense = int(input("what is your expesnse for gas this month?|$"))
taxes = int(input("what are your taxes for this month?|$"))
house_repair = int(input("what are you house repair expenses for this month?|$"))
lawncare = int(input("what are your expenses for lawn care this month?"))
electricty = int(input("what are your electricty expenses for this month?|$"))
water = int(input("what are your water expenses for this month?"))
internet = int(input("what are your internet expenses for this month?|$"))
expenses = {
    'grocery':grocery_expense,
    'car_repairs':car_repairs_expense,
    'sports':sport_expense,
    'classes': class_expense,
    'gas': gas_expense,
    'taxes': taxes,
    'house_repair': house_repair,
    'lawncare': lawncare,
    'electricty': electricty,
    'water': water,
    'internet': internet    
}
total_expense = 0
for _,value, in expenses.items():
    total_expense += value
print(f"your total expenses are:{total_expense}")
remaining = budget2 - total_expense
if remaining < 0:
    print(f"you went over your budget, by{remaining}")
else:
    print(f"you have {remaining} money left!")