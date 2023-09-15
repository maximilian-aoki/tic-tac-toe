# CHECK ALL COMBOS
def get_combos(board):
    rows_to_check = []
    cols_to_check = []
    diags_to_check = [
        [board["1"]["A"], board["2"]["B"], board["3"]["C"]],
        [board["1"]["C"], board["2"]["B"], board["3"]["A"]]
    ]
    for row in board:
        rows_to_check.append([board[row]["A"], board[row]["B"], board[row]["C"]])
    for column in ["A", "B", "C"]:
        col = []
        for row in board:
            col.append(board[row][column])
        cols_to_check.append(col)
    combos_to_check = rows_to_check + cols_to_check + diags_to_check
    return combos_to_check


# CHECK IF THE MOST RECENT MOVE WAS A WIN
def is_win(board):
    combos_to_check = get_combos(board)
    if ["X", "X", "X"] in combos_to_check:
        print("######----- CONGRATS, YOU WON! GAME OVER -----######\n")
        return True
    elif ["O", "O", "O"] in combos_to_check:
        print("######----- SORRY, YOU LOST. GAME OVER -----######\n")
        return True
    else:
        return False


# CHECK IF THE MOST RECENT MOVE RESULTED IN A TIE
def is_tie(board):
    full_board = True
    for row in board:
        for column in board[row]:
            if board[row][column] == " ":
                full_board = False
    if not full_board:
        return False
    else:
        print("######----- TIE! GAME OVER -----######\n")
        return True
