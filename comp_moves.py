import random
from game_checks import get_combos


# EASY COMPUTER MOVE FUNCTION
def computer_move_easy(board):
    all_move_options = []
    for row in board:
        for column in board[row]:
            if board[row][column] == " ":
                all_move_options.append(f"{column}{row}")
    move_index = random.choice(all_move_options)
    board[move_index[1]][move_index[0]] = "O"
    print(f"Computer has played '{move_index}'\n")


# IMPOSSIBLE COMPUTER MOVE FUNCTION
def computer_move_impossible(board, move_counter):
    if move_counter == 1:
        board['2']['B'] = "O"
        print(f"Computer has played 'B2'\n")
    elif move_counter == 2:
        second_move(board)
    elif check_win_moves(board):
        pass
    elif board == {'1': {'A': "O", 'B': "X", 'C': " "},
                   '2': {'A': " ", 'B': "O", 'C': " "},
                   '3': {'A': " ", 'B': " ", 'C': "X"}}:
        board['3']['A'] = "O"
        print(f"Computer has played 'A3'\n")
    elif board == {'1': {'A': "O", 'B': " ", 'C': " "},
                   '2': {'A': "X", 'B': "O", 'C': " "},
                   '3': {'A': " ", 'B': " ", 'C': "X"}}:
        board['1']['C'] = "O"
        print(f"Computer has played 'C1'\n")
    else:
        computer_move_easy(board)


def second_move(board):
    combos_to_check = get_combos(board)
    x_row_index = None
    x_col_index = None
    for combo in combos_to_check:
        if "X" in combo:
            x_row_index = combos_to_check.index(combo)
            x_col_index = combo.index("X")
            break

    if board["1"]["A"] == "X" or board["3"]["A"] == "X" or board["1"]["C"] == "X" or board["3"]["C"] == "X":
        combo_row_index = -x_row_index + 2
        combo_col_index = x_col_index
        selected_move = convert_indices_str([combo_row_index, combo_col_index])
        board[selected_move[1]][selected_move[0]] = "O"
        print(f"Computer has played '{selected_move}'\n")
    else:
        board["1"]["A"] = "O"
        print(f"Computer has played 'A1'\n")


# CHECK IF THERE IS A WIN MOVE FOR EITHER SIDE - PLAY ACCORDINGLY
def check_win_moves(board):
    combos_to_check = get_combos(board)
    for symbol in ["OX", "XO"]:
        for combo in combos_to_check:
            num_pro = combo.count(symbol[0])
            num_con = combo.count(symbol[1])
            if num_pro == 2 and num_con == 0:
                combo_index = combos_to_check.index(combo)
                if combo_index < 3:
                    # the winning combo is in a row
                    combo_row_index = combo_index
                    combo_col_index = combo.index(" ")
                elif combo_index < 6:
                    # the winning combo is in a column
                    combo_row_index = combo.index(" ")
                    combo_col_index = combo_index - 3
                elif combo_index == 6:
                    # the winning combo is a diagonal from top left to bottom right
                    combo_row_index = combo.index(" ")
                    combo_col_index = combo.index(" ")
                elif combo_index == 7:
                    # the winning combo is a diagonal from top right to bottom left
                    combo_row_index = combo.index(" ")
                    combo_col_index = -(combo.index(" ")) + 2

                selected_move = convert_indices_str([combo_row_index, combo_col_index])
                board[selected_move[1]][selected_move[0]] = "O"
                print(f"Computer has played '{selected_move}'\n")
                return True


# CONVERTS INT INDICES TO STR TO READ TO BOARD
def convert_indices_str(combo_indices):
    row_str = str(combo_indices[0] + 1)
    col_int = combo_indices[1]
    if col_int == 0:
        col_str = "A"
    elif col_int == 1:
        col_str = "B"
    elif col_int == 2:
        col_str = "C"
    return col_str + row_str
