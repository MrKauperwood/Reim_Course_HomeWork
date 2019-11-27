import random
import time

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

# Global variables
game_still_run = True
tic_tac_winner = None
tic_tac_drawn = False
current_player = "X"


# Printing boarding
def print_board(board):
    print("+-----------------+")
    for i in range(0, 3):
        print("|  " + board[3 * i + 0] + "  |  " + board[3 * i + 1] + "  |  " + board[3 * i + 2] + "  |")
        print("+-----------------+")


# Main game function
def play_game():
    print_board(board)
    global game_still_run

    while game_still_run:
        handle_turn(current_player)
        check_finish_game()
        change_player()

    if tic_tac_winner == "X" or tic_tac_winner == "Y":
        print("\n--- Игра окончена!Победил игрок", tic_tac_winner, "---")
    elif tic_tac_winner is None and tic_tac_drawn == True:
        print("Однако, это ничья!")


# Next game step
def handle_turn(player):
    if current_player == "X":

        # Is value entered correctly?
        is_correct = False
        while is_correct == False:
            try:
                position = input("\nСейчас ход \"" + current_player + "\". Выберите позицию от 1-9:\n")
                position = int(position) - 1
                if (position >= 0) and (position < 9):
                    if board[position] == " ":
                        board[position] = current_player
                        print_board(board)
                        is_correct = True
                    else:
                        print("\n--- Ошибка! Ячейка занята, повторите ввод")
                else:
                    print("\n---Ошибка! Значение должно быть от 1-9!---")
            except:
                print("\n---Ошибка! Вы ввели неверное значение. Повторите ввод!---")
    else:
        # Легкий уровень
        simple_machine_intel()


def check_finish_game():
    check_if_win()
    check_if_drawn_game()


def check_if_win():
    global tic_tac_winner

    column_winner = check_column()
    diag_winner = check_diag()
    rows_winner = check_rows()

    if rows_winner:
        tic_tac_winner = rows_winner
    elif diag_winner:
        tic_tac_winner = diag_winner
    elif column_winner:
        tic_tac_winner = column_winner
    else:
        tic_tac_winner = None
    return ...


def check_if_drawn_game():
    global tic_tac_drawn, game_still_run

    if " " not in board and tic_tac_winner is None:
        tic_tac_drawn = True
        game_still_run = False
        return ...


def change_player():
    global current_player

    if current_player == "X":
        current_player = "Y"
    else:
        current_player = "X"


def check_rows():
    global game_still_run

    rows1 = board[0] == board[1] == board[2] != " "
    rows2 = board[3] == board[4] == board[5] != " "
    rows3 = board[6] == board[7] == board[8] != " "

    if rows1 or rows2 or rows3:
        game_still_run = False
        if rows1:
            return board[0]
        if rows2:
            return board[3]
        if rows3:
            return board[8]
    return


def check_column():
    global game_still_run

    column1 = board[0] == board[3] == board[6] != " "
    column2 = board[1] == board[4] == board[7] != " "
    column3 = board[2] == board[5] == board[8] != " "

    if column1 or column2 or column3:
        game_still_run = False
        if column1:
            return board[0]
        if column2:
            return board[1]
        if column3:
            return board[2]
    return


def check_diag():
    global game_still_run

    diag1 = board[0] == board[4] == board[8] != " "
    diag2 = board[2] == board[4] == board[6] != " "

    if diag1 or diag2:
        game_still_run = False
        if diag1:
            return board[0]
        if diag2:
            return board[2]
    return


def simple_machine_intel():
    print("\nВаш соперник " + current_player + " сделал свой выбор!\n")
    mas_index = []
    sopernik = str

    if current_player == "X":
        sopernik = "Y"
    else:
        sopernik = "X"

    cols = [[0, 3, 6], [1, 4, 7],[2, 5, 8]]
    rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    diags = [[0, 4, 8],[2, 4, 6]]

    empty_col = may_win(cols, current_player)
    empty_row = may_win(rows, current_player)
    empty_diags = may_win(diags, current_player)

    empty_col_s = may_win(cols, sopernik)
    empty_row_s = may_win(rows, sopernik)
    empty_diags_s = may_win(diags, sopernik)

    if empty_col != None:
        board[empty_col] = current_player
        print_board(board)
    elif empty_row != None:
        board[empty_row] = current_player
        print_board(board)
    elif empty_diags != None:
        board[empty_diags] = current_player
        print_board(board)
    elif empty_col_s != None:
        board[empty_col_s] = current_player
        print_board(board)
    elif empty_row_s != None:
        board[empty_row_s] = current_player
        print_board(board)
    elif empty_diags_s != None:
        board[empty_diags_s] = current_player
        print_board(board)
    else:
        for i in range(len(board)):
            if board[i] == " ":
                mas_index.append(i)
        random.shuffle(mas_index)
        board[mas_index[0]] = current_player
        print_board(board)


def may_win(mas, player):
    for i in mas:
        count = 0
        empty = None
        for j in i:
            if board[j] == player:
                count += 1
            if board[j] == " ":
                empty = j
        if count == 2 and empty != None:
            return empty
        if count == 2 and empty is None:
            return empty



play_game()
