

def print_board():
    print("  |  |  ")
    print("--------")
    print("  |  |  ")
    print("--------")
    print("  |  |  ")

def print_line(char, index):
    if index == 1:
        print(f"{char} |   |  ")
        print("---------")
    elif index == 2:
        print(f"  | {char} |  ")
        print("---------")
    elif index == 3:
        print(f"  |   | {char} ")

def print_grid():
    print_line("x", 1) 
    print_line("o", 2)
    print_line("d", 3)


if __name__ == "__main__":
   
   row1 = ["","",""]
   row2 = ["","",""]
   row3 = ["","",""]

   print("Welcome to Tic Tac Toe!")
   player_choice = input("Would you like to be X or O? ")
   player_row = int(input("what row would you like? pick between 1,2, or 3| "))
   player_column = int(input("what column would you like? pick between 0,1, or 2| "))
   print(player_choice,player_row,player_column)
   if player_row == 1:
        row1[player_column] = player_choice
   elif player_choice == 2:
       row2[player_column] = player_choice
   elif player_choice == 3:
       row3[player_column] = player_choice

   print(row1)
   print(row2)
   print(row3)
   