from main import board 

def is_king_in_check(board):
    n = len(board)
    king_position = None
    for row in range(n):
        for col in range(n):
            if board[row][col] == 'K':
                king_position = (row, col)
                break
        if king_position:
            break
    
    if not king_position:
        print("Error: King not found")
        return

    king_row, king_col = king_position

   
    rook_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    bishop_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    pawn_attacks = [(-1, -1), (-1, 1)] if king_row > 0 else []

    for direction in rook_directions:
        row, col = king_row, king_col
        while True:
            row += direction[0]
            col += direction[1]
            if 0 <= row < n and 0 <= col < n:
                piece = board[row][col]
                if piece == '.':
                    continue
                elif piece == 'R' or piece == 'Q': 
                    print("Success")
                    return
                else:
                    break
            else:
                break

    for direction in bishop_directions:
        row, col = king_row, king_col
        while True:
            row += direction[0]
            col += direction[1]
            if 0 <= row < n and 0 <= col < n:
                piece = board[row][col]
                if piece == '.':
                    continue
                elif piece == 'B' or piece == 'Q': 
                    print("Success")
                    return
                else:
                    break
            else:
                break

    for direction in pawn_attacks:
        row = king_row + direction[0]
        col = king_col + direction[1]
        if 0 <= row < n and 0 <= col < n:
            if board[row][col] == 'P': 
                print("Success")
                return

    print("Fail")

is_king_in_check(board)