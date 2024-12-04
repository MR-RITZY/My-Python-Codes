import sys
def merge(a,b):

    """
    Merges two inputs `a` and `b` into a list of labeled strings.

    - If `a` is numeric and `b` is not, it appends a number from `a` to each element in `b`.
    - If `b` is numeric and `a` is not, it appends a number from `b` to each element in `a`.
    - If both `a` and `b` are non-numeric, it concatenates each element of `a` with each element of `b`.

    Args:
        a (list or int): The first input (list of strings or number).
        b (list or int): The second input (list of strings or number).

    Returns:
        list: A list of merged labels.
    """

    merged = []
    if str(a).isdecimal() and not(str(b).isdecimal()):
        for k in range(len(a)):
            n = k+1
            for i, j in enumerate(b):
                label = str(n) + b[i]
                merged.append(label)
    elif not(str(a).isdecimal()) and str(b).isdecimal():
        for k in range(b):
            n = k+1
            for i, j in enumerate(a):
                label = str(n) + a[i]
                merged.append(label)
    else:
        for i, j in enumerate(b):
            for k, l in enumerate(a):
                label = a[k] + b[i]
                merged.append(label)
    return merged

def isChess(chessboard):

    """
    Validates a chessboard dictionary against standard chess rules.

    - Each key in `chessboard` represents a position on the board.
    - Each value in `chessboard` represents a chess piece.

    Validation includes:
    - Checking if board positions match standard chessboard labels.
    - Ensuring piece names and their quantities are within chess rules.

    Args:
        chessboard (dict): Dictionary where keys are board positions (e.g., 'a1') and values are piece names (e.g., 'wpawn').

    Prints:
        'VALID CHESSBOARD' if the chessboard passes validation.
        'INVALID CHESSBOARD' with the reason if it fails
        """

    # Standard chessboard labels and pieces
    Id = ['a','b','c','d','e','f','g','h']
    color = ['w', 'b']
    pawn = ['pawn']*8
    knight = ['knight']*8
    bishop = ['bishop']*2
    rook = ['rook']*2
    piece = ['king','queen'] + rook + bishop + knight + pawn
    chesspieces = merge(color,piece)
    boardlabel = merge(Id,8)
    board = list(chessboard.keys())
    pieces = list(chessboard.values())
    piecenumber = {}
    totalpiece = 0

    # Validating board positions and pieces
    while True:
        for i in range(len(chessboard)):
            piecenumber[pieces[i]] = piecenumber.get(pieces[i], 0) + 1
            if board[i] not in boardlabel or pieces[i] not in chesspieces:
                print('INVALID CHESSBOARD\nLabel numbers or piece names on your chessboard not in accordance with chess standard')
                sys.exit()
        break
    for j, k in enumerate(chesspieces):
        piecenumber.setdefault(k,0)
    for l, m in piecenumber.items():
        totalpiece = totalpiece + m
    if piecenumber['wking'] > 1 or piecenumber['bking'] > 1 or piecenumber['wpawn']>8 or piecenumber['bpawn']>8 or totalpiece > 16:
        print('INVALID CHESSBOARD\n Piece numbers on your chessboard more than or not in accordance with chess standard')
        sys.exit()
    print('VALID CHESSBOARD')



