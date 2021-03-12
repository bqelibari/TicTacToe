SQUARE_GAMEFIELD_SIZE = 3
player_symbols = []
active_player = 0
# Create rectangle shaped Gamefield
gamefield = []


def new_game(symbols: list[str]) -> None:
    global player_symbols, active_player, gamefield
    player_symbols = list(symbols)
    gamefield = ["" for i in range(SQUARE_GAMEFIELD_SIZE ** 2)]


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


def place_symbol(x_coordinate: int, y_coordinate: int) -> None:
    global active_player, gamefield, SQUARE_GAMEFIELD_SIZE
    is_valid_coordinates = _validate_coordinates(x_coordinate, y_coordinate)

    if is_valid_coordinates:
        gamefield_index = (x_coordinate - 1) + (y_coordinate - 1) * SQUARE_GAMEFIELD_SIZE
        gamefield[gamefield_index] = player_symbols[active_player]
        if not is_winning_state():
            _next_player()


def is_winning_state() -> bool:
    global gamefield, SQUARE_GAMEFIELD_SIZE

    for index in range(SQUARE_GAMEFIELD_SIZE):
        last_symbol = None
        for current_symbol in gamefield[index * SQUARE_GAMEFIELD_SIZE:index * SQUARE_GAMEFIELD_SIZE + SQUARE_GAMEFIELD_SIZE]:
            if current_symbol == last_symbol and last_symbol != "":
                symbol_counter += 1
            else:
                symbol_counter = 1
            last_symbol = current_symbol
            if symbol_counter == SQUARE_GAMEFIELD_SIZE:
                return True
    return False


gamefield = ["x", "x", "x", "y", "", "", "", "y", ""]
assert is_winning_state() == True
gamefield = ["", "", "", "", "", "", "", "", ""]
assert is_winning_state() == False
gamefield = ["x", "y", "y", "y", "y", "x", "", "", ""]
assert is_winning_state() == False
gamefield = ["x", "x", "x", "y", "", "", "", "y", ""]
assert is_winning_state() == True
gamefield = ["x", "x", "x", "y", "", "", "", "y", ""]
assert is_winning_state() == True
