import random

board = [' ' for _ in range(10)]

def insert_letter(letter, pos):
    board[pos] = letter 

def is_space_free(pos):
    return board[pos] == ' '

def printf_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('   |   |')
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('   |   |')

def is_winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or \
           (bo[4] == le and bo[5] == le and bo[6] == le) or \
           (bo[1] == le and bo[2] == le and bo[3] == le) or \
           (bo[1] == le and bo[4] == le and bo[7] == le) or \
           (bo[2] == le and bo[5] == le and bo[8] == le) or \
           (bo[3] == le and bo[6] == le and bo[9] == le) or \
           (bo[3] == le and bo[5] == le and bo[7] == le)

def player_move():
    run = True
    while run:
        move = input('Please select a position to place an X (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if is_space_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print('Place occupied')
            else:
                print('Please type a number in the range (1-9)')
        except:
            print('Please type a number')

def is_board_full(board):
    return board.count(' ') == 1  # The board is full if there's only one empty space left

def comp_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move
    
    corners_open = [i for i in possible_moves if i in [1, 3, 7, 9]]
    if corners_open:
        move = select_random(corners_open)
        return move
    
    if 5 in possible_moves:
        move = 5
        return move
    
    edges_open = [i for i in possible_moves if i in [2, 4, 6, 8]]
    if edges_open:
        move = select_random(edges_open)
        return move
    
    return move

def select_random(li):
    return random.choice(li)

def main():
    print("Welcome to AI Tic Tac Toe!")
    printf_board(board)

    while not is_board_full(board):
        if not is_winner(board, 'O'):
            player_move()
            printf_board(board)
        else:
            print('O won')
            break
        
        if not is_winner(board, 'X'):
            move = comp_move()
            if move == 0:
                print('Tie Game!')
            else:
                insert_letter('O', move)
                print('Computer placed an O in position', move)
                printf_board(board)
        else:
            print('X won')
            break
    
    if is_board_full(board):
        print('Tie Game!')

if __name__ == "__main__":
    main()
