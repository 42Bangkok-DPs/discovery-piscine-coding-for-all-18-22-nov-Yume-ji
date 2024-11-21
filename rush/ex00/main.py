#/usr/bin/env python3

board = [0] * 8

for i in range(len(board)):
    board[i] = ["__"] * 8

def print_board(board):
    for i, row in enumerate(board):
        print(8 - i, end = ": ")
        for j, col in enumerate(row):
            print(col, end = " ")
        print("\n")
    print("   a   b   c   d   e   f   g   h")

white_piece_map = {
    "wP": [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
    "wN": [(7, 1), (7, 6)],
    "wB": [(7, 2), (7, 5)],
    "wR": [(7, 0), (7, 7)],
    "wQ": [(7, 3)],
    "wK": [(7, 4)]
}

black_piece_map = {
    "bP": [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
    "bN": [(0, 1), (0, 6)],
    "bB": [(0, 2), (0, 5)],
    "bR": [(0, 0), (0, 7)],
    "bQ": [(0, 3)],
    "bK": [(0, 4)]
}

col_map = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}

def put_pieces(board):
    for piece, squares in white_piece_map.items():
        for square in squares:
            x, y = square[0], square[1]
            board[x][y] = piece

    for piece, squares in black_piece_map.items():
        for square in squares:
            x, y = square[0], square[1]
            board[x][y] = piece

put_pieces(board)

curr_turn = 1

while(True):
    print_board(board)
    print("")

    curr_player = ""
    if curr_turn % 2 == 1:
        curr_player = "White"
    else:
        curr_player = "Black"
    
    curr_turn += 1

    print(curr_player + " to move!")
    print("")
    
    starting_square = input("Enter the square whose piece you'd like to play: ")
    start_x, start_y = starting_square[0], starting_square[1]
    start_x = col_map[start_x]
    start_y = 8 - int(start_y)
    start_x, start_y = start_y, start_x

    ending_square = input("Enter the square you'd like to move your piece to: ")
    end_x, end_y = ending_square[0], ending_square[1]
    end_x = col_map[end_x]
    end_y = 8 - int(end_y)
    end_x, end_y = end_y, end_x

    temp = board[start_x][start_y]
    board[start_x][start_y] = "  "
    board[end_x][end_y] = temp