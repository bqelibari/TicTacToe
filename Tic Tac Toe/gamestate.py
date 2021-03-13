SQUARE_GAMEFIELD_SIZE = 4
player_symbols = []
active_player = 0
# Create rectangle shaped Gamefield
gamefield = []



def new_game(symbols: list[str]) -> None:
    global player_symbols, active_player, gamefield
    player_symbols = list(symbols)
    gamefield = ["" for _ in range(SQUARE_GAMEFIELD_SIZE ** 2)]


def place_symbol(x_coordinate: int, y_coordinate: int) -> None:
    global active_player, gamefield, SQUARE_GAMEFIELD_SIZE
    is_valid_coordinates = _validate_coordinates(x_coordinate, y_coordinate)

    if is_valid_coordinates:
        gamefield_index = _calculate_list_index_from_coordinates(x_coordinate, y_coordinate)
        gamefield[gamefield_index] = player_symbols[active_player]
        if not is_winning_state():
            _next_player()


def is_winning_state() -> bool:
    return is_diagonal_win() or _is_vertical_or_horizontal_win()


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


def _check_for_same_symbols(coordinate_list: list[(int, int)]) -> bool:
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
    column_coordinate_list = [[(x_coordinate, row) for row in range(1, SQUARE_GAMEFIELD_SIZE + 1)]
                              for x_coordinate in range(1, SQUARE_GAMEFIELD_SIZE + 1)]
    row_coordinate_list = [[(column, y_coordinate) for column in range(1, SQUARE_GAMEFIELD_SIZE + 1)]
                           for y_coordinate in range(1, SQUARE_GAMEFIELD_SIZE + 1)]
    coordinate_list = column_coordinate_list + row_coordinate_list

    for coordinate_sublist in coordinate_list:
        symbols_are_equal = _check_for_same_symbols(coordinate_sublist)
        if symbols_are_equal:
            return True
    return False


def is_diagonal_win() -> bool:
    global SQUARE_GAMEFIELD_SIZE
    left_right_diagonal_list = [[(column, column) for column in range(1, SQUARE_GAMEFIELD_SIZE + 1)]]
    right_left_diagonal_list = [
        [(column + 1, row) for (column, row) in enumerate(range(SQUARE_GAMEFIELD_SIZE, 0, -1))]]
    diagonal_coord_list = left_right_diagonal_list + right_left_diagonal_list

    for coordinate_sublist in diagonal_coord_list:
        symbols_are_equal = _check_for_same_symbols(coordinate_sublist)
        if symbols_are_equal:
            return True
    return False
