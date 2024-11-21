from main import board  # นำเข้าข้อมูลกระดานจากไฟล์ main.py

def is_king_in_check(board):
    # หาตำแหน่งของ King
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

    # ทิศทางที่หมากประเภท Rook และ Queen สามารถโจมตีได้ (แนวตั้งและแนวนอน)
    rook_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # ทิศทางที่หมากประเภท Bishop และ Queen สามารถโจมตีได้ (แนวทแยง)
    bishop_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # ทิศทางที่ Pawn สามารถโจมตีได้ (ทแยงไปข้างหน้า)
    pawn_attacks = [(-1, -1), (-1, 1)] if king_row > 0 else []

    # ตรวจสอบทิศทางการโจมตีของ Rook และ Queen
    for direction in rook_directions:
        row, col = king_row, king_col
        while True:
            row += direction[0]
            col += direction[1]
            if 0 <= row < n and 0 <= col < n:
                piece = board[row][col]
                if piece == '.':
                    continue
                elif piece == 'R' or piece == 'Q':  # Rook หรือ Queen
                    print("Success")
                    return
                else:
                    break
            else:
                break

    # ตรวจสอบทิศทางการโจมตีของ Bishop และ Queen
    for direction in bishop_directions:
        row, col = king_row, king_col
        while True:
            row += direction[0]
            col += direction[1]
            if 0 <= row < n and 0 <= col < n:
                piece = board[row][col]
                if piece == '.':
                    continue
                elif piece == 'B' or piece == 'Q':  # Bishop หรือ Queen
                    print("Success")
                    return
                else:
                    break
            else:
                break

    # ตรวจสอบการโจมตีจาก Pawn
    for direction in pawn_attacks:
        row = king_row + direction[0]
        col = king_col + direction[1]
        if 0 <= row < n and 0 <= col < n:
            if board[row][col] == 'P':  # Pawn สามารถโจมตีในทิศทางทแยง
                print("Success")
                return

    # ถ้าไม่พบการโจมตีจากหมากใดๆ
    print("Fail")

# เรียกใช้งานฟังก์ชัน
is_king_in_check(board)