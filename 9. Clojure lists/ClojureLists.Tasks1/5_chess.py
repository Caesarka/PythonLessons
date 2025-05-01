game_board = [['·' for _ in range(8)] for _ in range(8)]
figures = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)]
bishop_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
rook_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def choose_figure():
    while True:
        figure = input(
            "Choose your figure (pawn, knight, bishop, rook, queen, king): ")

        if figure in figures:
            return figure
        else:
            usrUnput = input(
                "There is no such of figure in the game of chess. Press any key and try again or q for quit.")
            if usrUnput == 'q':
                break


def set_pos(figure):
    while True:
        pos = input(f"Choose start position for {figure}: ")

        pos_x = ord(pos[0]) - 97
        pos_y = ord(pos[1]) - 49

        if pos_x in range(8) and pos_y in range(8):
            return (pos_x, pos_y)
        else:
            usrUnput = input(
                'This position can not be set. Press any key and try again or q for quit.')
            if usrUnput == 'q':
                break


def set_figure(figure, pos_x, pos_y):
    for x in range(8):
        if x == pos_x:
            game_board[7 - pos_y][pos_x] = f'{figure[0].upper()}'


def show_steps(figure, pos_x, pos_y):
    match figure:
        case 'pawn':
            new_pos_y = 7 - pos_y - 1
            if is_valid(pos_x, new_pos_y):
                game_board[new_pos_y][pos_x] = '⋆'

            if pos_y == 1:
                game_board[7 - pos_y - 2][pos_x] = '⋆'

        case 'knight':
            for x, y in knight_moves:
                new_x = pos_x + x
                new_y = pos_y + y
                if is_valid(new_x, new_y):
                    game_board[7 - new_y][new_x] = '⋆'

        case 'bishop' | 'queen' | 'rook' | 'king':
            draw_figure_steps()


def get_figure_moves(figure):
    if figure == 'bishop':
        return bishop_moves, range(1, 8)
    elif figure == 'rook':
        return rook_moves, range(1, 8)
    elif figure == 'queen':
        return bishop_moves + rook_moves, range(1, 8)
    elif figure == 'king':
        return bishop_moves + rook_moves, range(1, 2)


def draw_figure_steps():
    for x, y in get_figure_moves(figure)[0]:
        for step in get_figure_moves(figure)[1]:
            new_pos_x = pos_x + x * step
            new_pos_y = pos_y + y * step

            if is_valid(new_pos_x, new_pos_y):
                game_board[7 - new_pos_y][new_pos_x] = '*'


def is_valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8


def draw_board():
    for y in range(8):
        for x in range(8):
            print(game_board[y][x], end=' ')
        print()


figure = choose_figure()
pos_x, pos_y = set_pos(figure)

show_steps(figure, pos_x, pos_y)
set_figure(figure, pos_x, pos_y)

draw_board()
