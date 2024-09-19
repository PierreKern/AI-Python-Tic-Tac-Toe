import pygame
import random
import sys

pygame.init()

width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

board = [' ' for _ in range(10)]
font = pygame.font.Font(None, 100)

def draw_grid():
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 5)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 5)
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 5)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 5)

def draw_move(letter, pos):
    x = (pos - 1) % 3 * 100 + 50
    y = (pos - 1) // 3 * 100 + 50
    label = font.render(letter, True, RED if letter == 'X' else BLUE)
    label_rect = label.get_rect(center=(x, y))
    screen.blit(label, label_rect)

def insert_letter(letter, pos):
    board[pos] = letter
    draw_move(letter, pos)

def is_space_free(pos):
    return board[pos] == ' '

def is_winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or \
           (bo[4] == le and bo[5] == le and bo[6] == le) or \
           (bo[1] == le and bo[2] == le and bo[3] == le) or \
           (bo[1] == le and bo[4] == le and bo[7] == le) or \
           (bo[2] == le and bo[5] == le and bo[8] == le) or \
           (bo[3] == le and bo[6] == le and bo[9] == le) or \
           (bo[3] == le and bo[5] == le and bo[7] == le) or \
           (bo[1] == le and bo[5] == le and bo[9] == le)


def is_board_full(board):
    return board.count(' ') <= 1

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
        move = random.choice(corners_open)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edges_open = [i for i in possible_moves if i in [2, 4, 6, 8]]
    if edges_open:
        move = random.choice(edges_open)
        return move
    return move

def player_move(pos):
    if is_space_free(pos):
        insert_letter('X', pos)
        if is_winner(board, 'X'):
            end_game("You won !")
        else:
            move = comp_move()
            if move != 0:
                insert_letter('O', move)
                if is_winner(board, 'O'):
                    end_game("Computer won ! (cheh)")
            if is_board_full(board):
                end_game("Tie !")


def end_game(message):
    print(message)
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

def get_pos_from_click(x, y):
    row = y // 100
    col = x // 100
    return row * 3 + col + 1

def main():
    draw_grid()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                pos = get_pos_from_click(x, y)
                player_move(pos)

        pygame.display.update()

if __name__ == "__main__":
    main()
