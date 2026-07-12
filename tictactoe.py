
def print_board():
    print("  |  |  ")
    print("--------")
    print("  |  |  ")
    print("--------")
    print("  |  |  ")

def print_line(char, index):
    if index == 1:
        print(f"{char} |   |  ")
    elif index == 2:
        print(f"  | {char} |  ")
    elif index == 3:
        print(f"  |   | {char} ")


if __name__ == "__main__":
   print("Welcome to Tic Tac Toe!")
   input("Would you like to be X or O? ")
   print_line("x", 1) 
   print_line("o", 2)
   print_line("d", 3)