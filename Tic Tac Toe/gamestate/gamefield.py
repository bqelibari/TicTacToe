from dataclasses import dataclass
from . import SQUARE_GAMEFIELD_SIZE


class Column_Out_Of_Field_Exception(Exception):
    pass


class Row_Out_Of_Field_Exception(Exception):
    pass

class Coordinate:
    def __init__(self, column: int, row: int):
        self.column = column
        self.row = row
        self._size = SQUARE_GAMEFIELD_SIZE
        self._validate_coordinates_or_throw_exception()

    def _validate_coordinates_or_throw_exception(self, column: int, row: int) -> bool:
        is_column_in_gamefield = 1 <= column <= self._size
        is_row_in_gamefield = 1 <= row <= self._size

        if not is_column_in_gamefield:
            raise Column_Out_Of_Field_Exception("Invalid row (x coordinate) given (out of gamefield).")

        if not is_row_in_gamefield:
            raise Row_Out_Of_Field_Exception("Invalid row (y coordinate) given (out of gamefield).")

    def as_index(self) -> int:
        horizontal_field_index = self.column
        vertical_push = (self.row - 1) * self.size

        return horizontal_field_index + vertical_push

    @staticmethod
    def from_index(index) -> 'Coordinate':
        column = index % SQUARE_GAMEFIELD_SIZE
        row = index // SQUARE_GAMEFIELD_SIZE + 1
        return Coordinate(column, row)

@dataclass
class Field:
    coordinates: Coordinate
    value: str = ""

class Gamefield:
    def __init__(self):
        self.gamefield = [Field(Coordinate.from_index(idx)) for idx in range(1, self.size ** 2 + 1)]
        self.size = SQUARE_GAMEFIELD_SIZE

    def place_symbol(self, field_coordinates: Coordinate, symbol: str):
        gamefield_index = self._calculate_list_index_from_coordinates(field_coordinates)
        self.gamefield[gamefield_index] = symbol

    def _calculate_list_index_from_coordinates(self, field_coordinates: Coordinate) -> int:
        return field_coordinates.as_index() - 1

    def _get_field_from_coordinates(self, column, row):
        field_coordinate = Coordinate(column, row)
        gamefield_index = self._calculate_list_index_from_coordinates(field_coordinate)
        return self.gamefield[gamefield_index]

    def get_column_fields(self, column):
        for row in range(1, self.size + 1):
            yield self._get_field_from_coordinates(column, row)

    def get_row_fields(self, row):
        for column in range(1, self.size + 1):
            yield self._get_field_from_coordinates(column, row)

    def get_left_diagonal_fields(self):
        for row in range(1, self.size + 1):
            yield self._get_field_from_coordinates(row, row)

    def get_right_diagonal_fields(self):
        for column in range(1, self.size + 1):
            from_right_x_coordinate = self.size + 1 - column
            yield self._get_field_from_coordinates(from_right_x_coordinate, column)

    def get_fields_per_row(self):
        for column in range(1, self.size + 1):
            return list(self.get_column_field_values(column))

    def get_fields_per_column(self):
        for row in range(1, self.size + 1):
            return list(self.get_row_field_values(row))
