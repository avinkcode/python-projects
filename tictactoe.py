import random


def game_over(row1, row2, row3, player_choice,computer_choice):
   if (row1[0] == player_choice and  row2[1] == player_choice and  row3[2] == player_choice):
      print("you win!")
      return True
   elif (row1[0] == computer_choice and  row2[1] == computer_choice and  row3[2] == computer_choice):  
      print("computer wins!")
      return True
   elif (row1[2] == computer_choice and row2[1] == computer_choice and row3[0] == computer_choice):
      print("computer wins!")
      return True
   elif (row1[2] == player_choice and row2[1] == player_choice and row3[0] == player_choice):
      print("you win!")
      return True
   elif (row1[0] == player_choice and row2[0] == player_choice and row3[0] == player_choice):
      print("you win!")
      return True
   elif (row1[0] == computer_choice and row2[0] == computer_choice and row3[0] == computer_choice):
      print("computer wins!")
      return True
   elif (row1[1] == player_choice and row2[1] == player_choice and row3[1] == player_choice):
      print("you win!")
      return True
   elif (row1[1] == computer_choice and row2[1] == computer_choice and row3[1] == computer_choice):
      print("computer wins!")
      return True
   elif (row1[2] == player_choice and row2[2] == player_choice and row3[2] == player_choice):
      print("you win!")
      return True
   elif (row1[2] == computer_choice and row2[2] == computer_choice and row3[2] == computer_choice):
      print("computer wins!")
      return True
   elif (row1[0] == player_choice and row1[1] == player_choice and row1[2] == player_choice):
      print("you win!")
      return True
   elif (row1[0] == computer_choice and row1[1] == computer_choice and row1[2] == computer_choice):
      print("computer wins!")
      return True
   elif (row2[0] == player_choice and row2[1] == player_choice and row2[2] == player_choice):
      print("you win!")
      return True
   elif (row2[0] == computer_choice and row2[1] == computer_choice and row2[2] == computer_choice):
      print("computer wins!")
      return True
   elif (row3[0] == player_choice and row3[1] == player_choice and row3[2] == player_choice):
      print("you win!")
      return True
   elif (row3[0] == computer_choice and row3[1] == computer_choice and row3[2] == computer_choice):
      print("computer wins!")
      return True
   elif row1[0]!="" and row1[1]!="" and row1[2]!="" and row2[0]!="" and row2[1]!="" and row2[2]!="" and row3[0]!="" and row3[1]!="" and row3[2]!="":
      print("the grid has been filled")
      return True
   else:
      print("no one has won!")
      return False



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

   while True:
   
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
            
      status = game_over(row1,row2,row3,player_choice,computer_choice)
      if status == True:
         break


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

      status = game_over(row1,row2,row3,player_choice,computer_choice)
      if status == True:
         break
      
         