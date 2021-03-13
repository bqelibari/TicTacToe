SQUARE_GAMEFIELD_SIZE = 3
player_symbols = []
active_player = 0
# Create rectangle shaped Gamefield
gamefield = []


def new_game(symbols: list[str]) -> None:
    global player_symbols, active_player, gamefield
    player_symbols = list(symbols)
    gamefield = ["" for i in range(SQUARE_GAMEFIELD_SIZE ** 2)]


def place_symbol(x_coordinate: int, y_coordinate: int) -> None:
    global active_player, gamefield, SQUARE_GAMEFIELD_SIZE
    is_valid_coordinates = _validate_coordinates(x_coordinate, y_coordinate)

    if is_valid_coordinates:
        gamefield_index = _calculate_list_index_from_coordinates(x_coordinate, y_coordinate)
        gamefield[gamefield_index] = player_symbols[active_player]
        if not is_winning_state():
            _next_player()


def is_winning_state() -> bool:
    is_diagonal_win = _is_left_diagonal_win() or _is_right_diagonal_win()
    return is_diagonal_win or _is_vertical_or_horizontal_win()


def _next_player() -> None:
    global active_player
    next_player = active_player + 1
    number_of_players = len(player_symbols)

    active_player = next_player % number_of_players


def _validate_coordinates(x_coordinate: int, y_coordinate: int) -> bool:
    global SQUARE_GAMEFIELD_SIZE
    is_x_coordinate_in_gamefield = 1 <= x_coordinate <= SQUARE_GAMEFIELD_SIZE
    is_y_coordinate_in_gamefield = 1 <= y_coordinate <= SQUARE_GAMEFIELD_SIZE

    return is_x_coordinate_in_gamefield and is_y_coordinate_in_gamefield


def _calculate_list_index_from_coordinates(x_coordinate: int, y_coordinate: int) -> int:
    global SQUARE_GAMEFIELD_SIZE
    horizontal_field_index = (x_coordinate - 1)
    vertical_push = (y_coordinate - 1) * SQUARE_GAMEFIELD_SIZE

    return horizontal_field_index + vertical_push


def _check_for_same_symbols(coordinate_list):
    global gamefield
    last_symbol = None
    is_first_symbol = True

    for x_coordinate, y_coordinate in coordinate_list:
        gamefield_index = _calculate_list_index_from_coordinates(x_coordinate, y_coordinate)
        current_symbol = gamefield[gamefield_index]
        if not is_first_symbol and current_symbol != last_symbol:
            return False
        last_symbol = current_symbol
        is_first_symbol = False

    return last_symbol != ""


def _is_vertical_or_horizontal_win() -> bool:
    global gamefield

    coordinate_list = [[(x_coordinate, row) for row in range(1, SQUARE_GAMEFIELD_SIZE + 1)]
                       for x_coordinate in range(1, SQUARE_GAMEFIELD_SIZE + 1)] + \
                      [[(column, y_coordinate) for column in range(1, SQUARE_GAMEFIELD_SIZE + 1)]
                       for y_coordinate in range(1, SQUARE_GAMEFIELD_SIZE + 1)]

    for coordinate_sublist in coordinate_list:
        are_same_symbols = _check_for_same_symbols(coordinate_sublist)
        if are_same_symbols:
            return True
    return False



def _is_left_diagonal_win() -> bool:
    global SQUARE_GAMEFIELD_SIZE

    coordinate_list = [(x_coordinate, x_coordinate) for x_coordinate in range(1, SQUARE_GAMEFIELD_SIZE + 1)]
    return _check_for_same_symbols(coordinate_list)


def _is_right_diagonal_win() -> bool:
    global SQUARE_GAMEFIELD_SIZE

    coordinate_list = [(x_coordinate + 1, y_coordinate) for x_coordinate, y_coordinate in
                       enumerate(range(SQUARE_GAMEFIELD_SIZE, 0, -1))]
    return _check_for_same_symbols(coordinate_list)


gamefield = ["x", "x", "y",
             "x", "x", "y",
             "y", "y", "x"]
assert is_winning_state() == True

gamefield = ["", "", "x",
             "", "x", "",
             "x", "", ""]
assert is_winning_state() == True

gamefield = ["x", "", "",
             "x", "", "",
             "x", "", ""]
assert is_winning_state() == True

gamefield = ["", "x", "",
             "", "x", "",
             "", "x", ""]
assert is_winning_state() == True

gamefield = ["", "", "x",
             "", "", "x",
             "", "", "x"]
assert is_winning_state() == True

gamefield = ["x", "x", "x",
             "x", "x", "v",
             "c", "v", "c"]
assert is_winning_state() == True

gamefield = ["", "", "",
             "x", "x", "x",
             "", "", ""]
assert is_winning_state() == True

gamefield = ["", "", "",
             "", "", "",
             "x", "x", "x"]
assert is_winning_state() == True

gamefield = ["x", "", "",
             "x", "", "",
             "x", "", ""]
assert is_winning_state() == True

gamefield = ["", "x", "",
             "", "x", "",
             "", "x", ""]
assert is_winning_state() == True

gamefield = ["", "", "x",
             "", "", "x",
             "", "", "x"]
assert is_winning_state() == True

gamefield = ["x", "y", "x",
             "x", "x", "y",
             "y", "d", "y"]
assert is_winning_state() == False

gamefield = ["", "", "",
             "", "", "",
             "", "", ""]
assert is_winning_state() == False
