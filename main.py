import random

# STARTING BOARD
BOARD = {'1': {'A': " ", 'B': " ", 'C': " "}, '2': {'A': " ", 'B': " ", 'C': " "}, '3': {'A': " ", 'B': " ", 'C': " "}}


# WELCOME MESSAGES
print('''
  _____ _        _____            _____          _ 
 |_   _(_) ___  |_   _|_ _  ___  |_   _|__   ___| |
   | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \ |
   | | | | (__    | | (_| | (__    | | (_) |  __/_|
   |_| |_|\___|   |_|\__,_|\___|   |_|\___/ \___(_)                                      
''')
print("Welcome to Tic Tac Toe!\n")
print("The name of the game is to get 3-in-a-row, whether that be horizontal, diagonal, or vertical.")
print("The board is arranged in a grid spanning columns 'A', 'B', and 'C', and rows '1', '2', and '3'.\n")


# INITIALIZE DIFFICULTY (come back to this)
# difficulty = input("You will play as the 'X' symbol. "
#                    "Would you like to set the difficulty to 'easy', 'hard', or 'impossible': ").lower().strip()

print("Let's begin!\n")


# FUNCTIONS!

# INTERNAL BOARD SHOW FUNCTION
def show_board():
    for row in board:
        print(f" {board[row]['A']} | {board[row]['B']} | {board[row]['C']} ")
        if row != '3':
            print("-----------")


# PLAYER MOVE FUNCTION
def player_move():
    show_board()
    move_index = input("\nWhere would you like to place your 'X'? "
                       "(input the column letter follower by the row number, i.e. 'B2' for center: ").upper().strip()
    selected_move = board[move_index[1]][move_index[0]]
    if selected_move == " ":
        board[move_index[1]][move_index[0]] = "X"
    else:
        print("That space is occupied! Please choose again.\n")
        player_move()


# EASY COMPUTER MOVE FUNCTION
def computer_move_easy():
    all_move_options = []
    for row in board:
        for column in board[row]:
            if board[row][column] == " ":
                all_move_options.append(f"{column}{row}")
    move_index = random.choice(all_move_options)
    board[move_index[1]][move_index[0]] = "O"
    print(f"Computer has played '{move_index}'\n")


# CHECK IF THE MOST RECENT MOVE WAS A WIN
def is_win():
    rows_to_check = []
    cols_to_check = []

    diags_to_check = [
        board["1"]["A"] + board["2"]["B"] + board["3"]["C"],
        board["1"]["C"] + board["2"]["B"] + board["3"]["A"]
    ]

    for row in board:
        rows_to_check.append(board[row]["A"] + board[row]["B"] + board[row]["C"])

    for column in ["A", "B", "C"]:
        col_str = ""
        for row in board:
            col_str = col_str + board[row][column]
        cols_to_check.append(col_str)

    combos_to_check = rows_to_check + cols_to_check + diags_to_check
    if "XXX" in combos_to_check:
        print("\nCONGRATS, YOU WON! GAME OVER.\n")
        return True
    elif "OOO" in combos_to_check:
        print("\nSORRY, YOU LOST. GAME OVER.\n")
        return True
    else:
        return False


# CHECK IF THE MOST RECENT MOVE RESULTED IN A TIE
def is_tie():
    full_board = True
    for row in board:
        for column in board[row]:
            if board[row][column] == " ":
                full_board = False
    if not full_board:
        return False
    else:
        print("\nTIE! GAME OVER.\n")
        return True


# INITIALIZE THE GAME
board = BOARD


# GAMEPLAY
while True:
    player_move()
    if is_win():
        break
    if is_tie():
        break
    computer_move_easy()
    if is_win():
        break
    if is_tie():
        break

show_board()
