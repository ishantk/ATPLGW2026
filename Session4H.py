"""
CHESSBOARD
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
"""

# Assignment: finish your chessboard
white = '\u25A0'
black = '\u25A1'
white_pawn = '\u2659' # print for outer value 1
black_pawn = '\u265F' # print for outer value 6

for outer in range(0,8):
    for inner in range(0,8):
        
        if outer == 1:
            print(white_pawn, end=' ')
        elif outer == 6:
            print(black_pawn, end=' ')
        elif (outer+inner)%2 == 0:
            print(white, end=' ')
        else:
            print(black, end=' ')
        
    print()
