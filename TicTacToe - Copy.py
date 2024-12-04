import sys
def TicTacToe():
        """
    A simple text-based Tic Tac Toe game for two players.

    Instructions:
    Players take turns inputting positions to place their 'X' or 'O'.
    The positions correspond to the following keys:
        - Top row: 'tl', 'tm', 'tr' (top-left, top-middle, top-right)
        - Middle row: 'ml', 'mc', 'mr' (mid-left, mid-center, mid-right)
        - Bottom row: 'bl', 'bm', 'br' (bottom-left, bottom-middle, bottom-right)
    The game continues until a player wins or the board is full (draw).
    """

    # Initializing the game board
    T = {'tl':'   ', 'tm':'   ', 'tr':'   ',
        'ml':'   ', 'mc': '   ', 'mr':'   ',
        'bl':'   ', 'bm': '   ', 'br':'   '}
    gap = '---+---+---'

    print('Instruction\nTo play to the top-left corner, type tl then press enter, for top-middle, type tm then press enter, for \
top-right, type tr then press enter, for mid-left, type ml then press enter and for mid-center, type mc then press enter, \
for mid-right, type mr then press enter, for bottom-left, type bl then press enter, for bottom-middle, type bm then press enter, \
for bottom-right, type br then press enter.')


    print(T['tl'] + '|' + T['tm'] + '|' + T['tr'])
    print(gap)
    print(T['ml'] + '|' + T['mc'] + '|' + T['mr'])
    print(gap)
    print(T['bl'] + '|' + T['bm'] + '|' + T['br'])
    for i in range(9):
        if 2*(i//2) == i:
            turn = ' X '
        else:
            turn = ' O '
        if i == 0 or i == 1:
            move = input('Player ' + turn.strip() + ', your turn.\nMove your first ' + turn.strip() + '.\n')
        else:
            move = input('Player ' + turn.strip() + ', your turn.\nTake your next ' + turn.strip() + ' to a new place.\n')
        while True:
            error = ''
            try:
                while T[move] != '   ':
                    move = input('Position alreadly occupied.\nPlay to a place that is not yet occupied\n')
            except KeyError:
                error = 'INVALID KEY'
                if i == 0:
                    print(error + '\nSTART OVER!')
                    TicTacToe()
                else:
                    print(error)

                    print('Instruction\nTo play to the top-left corner, type tl then press enter, for top-middle, type tm then press enter, for \
top-right, type tr then press enter, for mid-left, type ml then press enter and for mid-center, type mc then press enter, \
for mid-right, type mr then press enter, for bottom-left, type bl then press enter, for bottom-middle, type bm then press enter, \
for bottom-right, type br then press enter.')

                    move = input('Player ' + turn.strip() + ', still your turn.\nEnter the correct key to move your next ' + turn.strip() + ' to new place.\n')
            if error == '':
                break

        # Updating board and display
        T[move] = turn
        print(T['tl'] + '|' + T['tm'] + '|' + T['tr'])
        print(gap)
        print(T['ml'] + '|' + T['mc'] + '|' + T['mr'])
        print(gap)
        print(T['bl'] + '|' + T['bm'] + '|' + T['br'])

        # Checking for a winner
        win = ''
        if T['tl'] == T['tm'] == T['tr'] == ' X ' or \
           T['bl'] == T['bm'] == T['br'] == ' X ' or \
           T['ml'] == T['mc'] == T['mr'] == ' X ' or \
           T['tl'] == T['ml'] == T['bl'] == ' X ' or \
           T['tm'] == T['mc'] == T['bm'] == ' X ' or \
           T['tr'] == T['mr'] == T['br'] == ' X ' or \
           T['tl'] == T['mc'] == T['br'] == ' X ' or \
           T['tr'] == T['mc'] == T['bl'] == ' X ':
            win ='PLAYER X WIN'
            print(win)
            break
        elif T['tl'] == T['tm'] == T['tr'] == ' O ' or \
             T['bl'] == T['bm'] == T['br'] == ' O ' or \
             T['ml'] == T['mc'] == T['mr'] == ' O ' or \
             T['tl'] == T['ml'] == T['bl'] == ' O ' or \
             T['tm'] == T['mc'] == T['bm'] == ' O ' or \
             T['tr'] == T['mr'] == T['br'] == ' O ' or \
             T['tl'] == T['mc'] == T['br'] == ' O ' or \
             T['tr'] == T['mc'] == T['bl'] == ' O ':
            win = 'PLAYER O WIN'
            print(win)
            break

    # Checking for draw and prompting replay
    if win == '':
        print('DRAW')
        startover = input('REPLAY?\nYES OR NO?\n')
        startover = startover.lower()
        while startover != 'no':
            TicTacToe()
        sys.exit(0)
    else:
        startover = input('START OVER?\nYES OR NO?\n')
        startover = startover.lower()
        while startover != 'no':
            TicTacToe()
        sys.exit(0)

# Entry point of the program
if __name__ == '__main__':
    TicTacToe()
