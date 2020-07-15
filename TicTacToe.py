# Step1
def display_board(board):
    print('\n' * 100)
    print('| {} | {} | {} |'.format(board[7], board[8], board[9]))
    print('|___|___|___|')
    print('| {} | {} | {} |'.format(board[4], board[5], board[6]))
    print('|___|___|___|')
    print('| {} | {} | {} |'.format(board[1], board[2], board[3]))


# Step2
def player_input():
    '''
    OUTPUT = (Player1 marker, Player2 marker)
    '''
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input(f'Player 1, choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    elif marker == 'O':
        return ('O', 'X')


# Step3
def place_marker(board, marker, position):
    board[position] = marker


# step4
def win_check(board, mark):
    # rows
    return ((board[1] == mark and board[2] == mark and board[1] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            # columns
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            # diagonals
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


# step5
import random


def choose_first():
    coinflip = random.randint(0, 1)
    if coinflip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# Step6
def space_check(board, position):
    return board[position] == ' '


# Step7
def full_board_check(board):
    for x in range(1, 10):
        if space_check(board, x):
            return False
        # True means board is full
    return True


# Step8
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose a position (1-9):"))
    return position


# Step8
def replay():
    return (input('Play again? y/n').upper()) == 'Y'


# Game
print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here (board, who plays first, choose markers X,O)
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(f'{turn} will go first')

    play_game = input('Ready to play? Y/N').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:

        # player1 turn

        if turn == 'Player 1':

            # display the board
            display_board(the_board)

            # choose a position
            position = player_choice(the_board)

            # place marker on position
            place_marker(the_board, player1_marker, position)

            # check if p1 won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!')
                break
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE")
                    break
                else:
                    turn = 'Player 2'

        # player2 turn

        else:

            # display the board
            display_board(the_board)

            # choose a position
            position = player_choice(the_board)

            # place marker on position
            place_marker(the_board, player2_marker, position)

            # check if p2 won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!')
                break
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break