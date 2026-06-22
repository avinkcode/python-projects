import random
actions = ["rock","paper","scissors"]
if __name__ == "__main__":
    while True:
        player_choice = input("player, pick rock, paper or scissors ")
        random.shuffle(actions)
        computer_choice = random.choice(actions)
        if player_choice == "rock" and computer_choice == "paper":
            print("computer won!")
        elif player_choice == "rock" and computer_choice == "scissors":
            print("you won!")
        elif player_choice == "rock" and computer_choice == "rock":
            print("it was a tie!")
        elif player_choice == "paper" and computer_choice == "rock":
            print("you won!")
        elif player_choice == "paper" and computer_choice == "scissors":
            print("computer won!")
        elif player_choice == "paper" and computer_choice == "paper":
            print("it was a tie!")
        elif player_choice == "scissors" and computer_choice == "rock":
            print("computer won!")
        elif player_choice== "scissors" and computer_choice == "paper":
            print("you won!")
        elif player_choice== "scissors" and computer_choice == "scissors":
            print("it was a tie!")
            
            
