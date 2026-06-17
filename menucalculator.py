menu = {  
1:2.00,
2:1.50,
3: 1.00,
4: 0.75,
5: 1.25,
6: 0.50
}
print("Welcome to my resturaunt!")
num_of_burgers = input("how many burgers do you want? ")
num_of_fries = input("how many fries do you want? ")
num_of_pies = input("how many pies do you want? " )
num_of_hotdogs = input("how many hot dogs do you want? ")
num_of_pizzas = input("how many pizzas do you want? " )
num_of_chicken = input("how many pieces of chicken do you want? " )

total = (int(num_of_burgers) * menu[1]) + (int(num_of_fries) * menu[2]) + (int(num_of_pies) * menu[3]) + (int(num_of_hotdogs) * menu[4]) + (int(num_of_pizzas) * menu[5]) + (int(num_of_chicken) * menu[6])
print(f"Your total is ${total}. Thank you for visiting!  ")