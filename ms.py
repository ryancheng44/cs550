'''
Ryan Cheng
10/15/23
Sources: None
Reflection: Overall I had fun making this game. There were some challenging moments, but they were
            welcomed. Since the last submission, I made what was expected from the user more clear
            by providing example statements.
On my honor, I have neither given nor received unauthorized aid: Ryan Cheng
'''

import random

mine_symbol = '*'
flag_symbol = '!'

x = 0
y = 0
m = 0

solution_board = [[]]
game_board = [[]]

selected_x = 0
selected_y = 0
flag = False

def get_dimensions():
    # Reference global variables
    global x, y, m
    
    while True:
        dimensions = input("Create a new game: (# of cols # of rows # of mines) ex. (5 5 4) ").split()
        dimensions_len = len(dimensions)

        # If there are more than three inputs, then tell the user
        if dimensions_len > 3:
            print("Error: too many inputs")
        # If there are less than three inputs, then tell the user
        elif dimensions_len < 3:
            print("Error: not enough inputs")
        else:
            # Try to assign x, y, and m; if integer cast fails, then tell the user
            try:
                x = int(dimensions[0])
                y = int(dimensions[1])
                m = int(dimensions[2])

                if x < 3 or y < 3 or x > 10 or y > 10:
                    print("Error: x and y must be between 3 and 10")
                elif m < 1:
                    print("Error: m must be greater than 0")
                elif m > x * y / 2:
                    print("Error: m must be less than x * y / 2")
                else:
                    break
            except ValueError:
                print("Error: non-integer input")


def get_move():
    # Reference global variables
    global selected_x, selected_y, flag

    while True:
        # Get the user's input, then split it into an array
        move = input("Enter a move: (x y flag?) ex. (1 1) or (3 3 f) ").lower().split()
        move_len = len(move)

        # If there are less than two inputs, then tell the user
        if move_len < 2:
            print("Error: not enough points for a coordinate")
            continue
        # If there are more than three inputs, then tell the user
        elif move_len > 3:
            print("Error: too many inputs")
            continue
        elif move_len == 3:
            # If the last input isn't an 'f', then tell the user. Otherwise, change the bool 'flag' to true.
            if move[2] != 'f':
                print("Error: last input isn't an 'f'")
                continue
            else:
                flag = True
        # If there are two inputs, then change the bool 'flag' to false
        else:
            flag = False
        
        # Try to assign x and y; if integer cast fails, then tell the user
        try:
            selected_x = int(move[0])
            selected_y = int(move[1])

            # Check to make sure the coordinates are in bounds:
            if selected_x < 1 or selected_x > x or selected_y < 1 or selected_y > y:
                print("Error: coordinate out of bounds")
            else:
                break
        except ValueError:
            print("Error: non-integer input in coordinate")

def setup_board():
    for i in range(m):
        while True:    
            rand_x = random.randint(1, x)
            rand_y = random.randint(1, y)

            # Check that the coordinate is not the user's selected coordinate and that a mine isn't already there
            if rand_x != selected_x and rand_y != selected_y and solution_board[rand_y][rand_x] != mine_symbol:
                solution_board[rand_y][rand_x] = mine_symbol

                # Increment the surrounding squares
                for j in range(rand_y - 1, rand_y + 2):
                    for k in range(rand_x - 1, rand_x + 2):
                        # If the neighboring square isn't a mine, then increase its count
                        if solution_board[j][k] != mine_symbol:
                            solution_board[j][k] = str(int(solution_board[j][k]) + 1)
            
                break

def handle_move():
    # If the user wants to flag
    if flag:
        # If the selected coordinate has not been flagged yet, flag it
        if game_board[selected_y][selected_x] != flag_symbol:
            game_board[selected_y][selected_x] = flag_symbol
        # Otherwise remove the flag
        else:
            game_board[selected_y][selected_x] = '+'
    else:
        # If the selected coordinate is a mine, return false to restart the game
        if solution_board[selected_y][selected_x] == mine_symbol:
            print("Game over! Here is what the solved board looks like: ")
            display_board(solution_board)
            return False
        # Otherwise take the value of the selected coordinate from the solution board and assign it to the selected coordinate in the game board
        else:
            check_recursively(selected_x, selected_y)
    return True

def check_recursively(x, y):
    # If the square is already open or is a gutter square, then return
    if game_board[y][x] != '+':
        return

    value = solution_board[y][x]
    game_board[y][x] = value
    if value == '0':
        # If the value is 0, then open all the surrounding squares
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                check_recursively(j, i)

def display_board(board):
    for i in range(1, y + 1):
        print(*board[i][1:-1])

def check_win():
    # Check if the number of unopened squares is equal to the number of mines
    unopened = 0
    for i in range(1, y + 1):
        for j in range(1, x + 1):
            if game_board[i][j] == '+':
                unopened += 1
    if unopened == m:
        print("You win! Here is what the solved board looks like: ")
        display_board(solution_board)
        return True
    else:
        return False

print("Welcome to Minesweeper.")

while True:
    get_dimensions()
    solution_board = [['0' for i in range(x + 2)] for j in range(y + 2)]
    game_board = [['-' for i in range(x + 2)] for j in range(y + 2)]
    
    # Set the inside of the board to '+'
    # This leaves the gutters of the board as '-'
    for i in range(1, y + 1):
        for j in range(1, x + 1):
            game_board[i][j] = '+'

    display_board(game_board)
    get_move()
    setup_board()
    handle_move()
    check_win()

    while True:
        if check_win():
            break
        display_board(game_board)
        get_move()
        if not handle_move():
            break
    
    while True:
        restart = input("Would you like to restart? (y/n) ").strip().lower()
        if restart == "y":
            break
        elif restart == "n":
            print("Thanks for playing!")
            quit()
        else:
            print("Error: invalid input")