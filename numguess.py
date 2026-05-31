
answer = 47
number2 = 0
while number2 < 3:
    number = input("guess a number between 1 and 100 ")
    print(number)
    number = int(number)
    number2 = number2 + 1
    if number < 46:
        print("your guess was lower than the number")
    elif number == 47:
        print("good job! you guessed the number!")
    elif number > 48:
        print("your guess was higher than the number")
    