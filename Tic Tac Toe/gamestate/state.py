from .gamefield import Gamefield, Field, Coordinate

player_symbols = []
active_player = 0
# Create rectangle shaped Gamefield
gamefield = None


def new_game(symbols: list[str]) -> None:
    global player_symbols, active_player, gamefield
    player_symbols = list(symbols)
    gamefield = Gamefield()


def place_symbol(field_coordinates: Coordinate) -> None:
    gamefield.place_symbol(field_coordinates, player_symbols[active_player])
    if not is_winning_state():
        _next_player()


def is_winning_state() -> bool:
    is_diagonal_win = _is_left_diagonal_win() or _is_right_diagonal_win()
    return is_diagonal_win or _is_horizontal_win() or _is_vertical_win()


def _next_player() -> None:
    global active_player
    next_player = active_player + 1
    number_of_players = len(player_symbols)

    active_player = next_player % number_of_players


def _check_for_same_nonempty_field_values(field_list: list[Field]) -> bool:
    previous_field_value = None
    is_first_symbol = True

    for field in field_list:
        if (not is_first_symbol and field.value != previous_field_value):
            return False
        previous_field_value = field.value
        is_first_symbol = False

    return previous_field_value != ""


def _is_left_diagonal_win():
    left_diagonal_fields = gamefield.get_left_diagonal_fields()
    return _check_for_same_nonempty_field_values(left_diagonal_fields)


def _is_right_diagonal_win():
    left_diagonal_fields = gamefield.get_right_diagonal_fields()
    return _check_for_same_nonempty_field_values(left_diagonal_fields)


def _is_horizontal_win():
    for horizontal_fields in gamefield.get_fields_per_row():
        if _check_for_same_nonempty_field_values(horizontal_fields):
            return True
    return False


def _is_vertical_win():
    for vertical_fields in gamefield.get_fields_per_column():
        if _check_for_same_nonempty_field_values(vertical_fields):
            return True
    return False