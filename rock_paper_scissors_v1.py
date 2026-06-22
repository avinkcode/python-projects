while True:
    player1 = input("player1 rock, paper, or scissors? ")
    player2 = input("player2 rock, paper, or scissors? ")
    if player1 == "rock" and player2 == "paper":
        print("player2 won!")
    elif player1 == "rock" and player2 == "scissors":
        print("player1 won!")
    elif player1 == "rock" and player2 == "rock":
        print("it was a tie!")
    elif player1 == "paper" and player2 == "rock":
        print("player1 won!")
    elif player1 == "paper" and player2 == "scissors":
        print("player2 won!")
    elif player1 == "paper" and player2 == "paper":
        print("it was a tie!")
    elif player1 == "scissors" and player2 == "rock":
        print("player2 won!")
    elif player1 == "scissors" and player2 == "paper":
        print("player1 won!")
    elif player1 == "scissors" and player2 == "scissors":
        print("it was a tie!")
        