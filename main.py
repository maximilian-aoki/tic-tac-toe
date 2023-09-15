import game_checks
import comp_moves


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


# INITIALIZE DIFFICULTY AND CHECK INPUT
def difficulty_input():
    difficulty = input("You will play as the 'X' symbol. "
                       "Would you like to set the difficulty to 'easy' or 'impossible': ").lower().strip()
    if difficulty == "easy" or difficulty == "impossible":
        return difficulty
    else:
        print("Sorry, your input wasn't recognized.")
        return difficulty_input()


# CHECK 'PLAY AGAIN' INPUT FOR END OF GAME
def play_again_input():
    play_again = input("\nWould you like to play again? ('y' for Yes, 'n' for No): ")
    if play_again == "n":
        return False
    elif play_again == "y":
        return True
    else:
        print("Sorry, your input wasn't recognized.")
        return play_again_input()


# INTERNAL BOARD SHOW FUNCTION
def show_board():
    print("   (A) (B) (C)")
    for row in board:
        print(f"({row}) {board[row]['A']} | {board[row]['B']} | {board[row]['C']} ")
        if row != '3':
            print("   -----------")


# CHECK PLAYER MOVE
def check_player_input():
    move_index = input("\nWhere would you like to place your 'X'? "
                       "(input the column letter follower by the row number, i.e. 'B2' for center: ").upper().strip()
    if move_index in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
        return move_index
    else:
        print("Sorry, your input wasn't recognized.")
        return check_player_input()


# PLAYER MOVE FUNCTION
def player_move():
    show_board()
    move_index = check_player_input()
    selected_move = board[move_index[1]][move_index[0]]
    if selected_move == " ":
        board[move_index[1]][move_index[0]] = "X"
    else:
        print("That space is occupied! Please choose again.\n")
        player_move()


# GAMEPLAY
continue_playing = True
while continue_playing:
    board = {'1': {'A': " ", 'B': " ", 'C': " "},
             '2': {'A': " ", 'B': " ", 'C': " "},
             '3': {'A': " ", 'B': " ", 'C': " "}}
    move_counter = 1
    difficulty = difficulty_input()
    print("Let's begin!\n")
    if difficulty == "easy":
        while True:
            player_move()
            if game_checks.is_win(board):
                break
            if game_checks.is_tie(board):
                break
            comp_moves.computer_move_easy(board)
            if game_checks.is_win(board):
                break
            if game_checks.is_tie(board):
                break
    elif difficulty == "impossible":
        while True:
            comp_moves.computer_move_impossible(board, move_counter)
            move_counter += 1
            if game_checks.is_win(board):
                break
            if game_checks.is_tie(board):
                break
            player_move()
            if game_checks.is_win(board):
                break
            if game_checks.is_tie(board):
                break
    show_board()

    continue_playing = play_again_input()

print("Goodbye!")
