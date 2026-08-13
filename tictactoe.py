if __name__ == "__main__":
   row1 = ["","",""]
   row2 = ["","",""]
   row3 = ["","",""]
   print("Welcome to Tic Tac Toe!")
   player_choice = input("Would you like to be X or O? ")
   computer_choice = ""
   if player_choice == "x":
      computer_choice = "o"
   elif player_choice == "o":
      computer_choice = "x"
  

   for k in range(3):
   
      player_row = int(input("what row would you like? pick between 1,2, or 3| "))
      player_column = int(input("what column would you like? pick between 0,1, or 2| "))
      computer_row = ""
      computer_collumn = ""
      print(player_choice,player_row,player_column)
      print(f"computer picked: {computer_choice}")
      if player_row == 1:
          row1[player_column] = player_choice
      elif player_row == 2:
         row2[player_column] = player_choice
      elif player_row == 3:
         row3[player_column] = player_choice

      print(row1)
      print(row2)
      print(row3)
   