import random
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

   computer_row_choice = [1,2,3]
   computer_col_choice = [0,1,2]

   for k in range(4):
   
      player_row = int(input("what row would you like? pick between 1,2, or 3| "))
      player_column = int(input("what column would you like? pick between 0,1, or 2| "))

      random.shuffle(computer_row_choice)
      random.shuffle(computer_col_choice)
      computer_row = computer_row_choice[0]
      computer_collumn = computer_col_choice[0]

      print(player_choice,player_row,player_column)
      print(f"computer picked: {computer_choice},{computer_row},{computer_collumn}")
      if player_row == computer_row and player_column == computer_collumn:
         print("the computer picked a spot that you picked")
         continue

      if player_row == 1:
          if row1[player_column] == "": 
            row1[player_column] = player_choice
          else:
             print("this slot is taken")

      elif player_row == 2:
         if row2[player_column] == "":
            row2[player_column] = player_choice
         else:
            print("this slot is taken")
      elif player_row == 3:
         if row3[player_column] == "":        
            row3[player_column] = player_choice
         else:
            print("this slot is taken")
      if computer_row == 1:
         if row1[computer_collumn] == "":
            row1[computer_collumn] = computer_choice
         else:
            print("the computer picked a slot that was already chosen")
      elif computer_row == 2:
         if row2[computer_collumn] == "":
            row2[computer_collumn] = computer_choice
         else:
            print("the computer picked a slot that was already chosen")
      elif computer_row == 3:
         if row3[computer_collumn] == "":
            row3[computer_collumn] = computer_choice
         else:
            print("the computer picked a slot that was already chosen")

         

      print(row1)
      print(row2)
      print(row3)
   