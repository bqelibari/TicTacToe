import unittest
from ..gamefield import Coordinate, Gamefield, Field
from .. import SQUARE_GAMEFIELD_SIZE


class Test_Gamefield(unittest.TestCase):
    def setUp(self) -> None:
        self.gamefield = Gamefield( )

    def test__calculateListIndexFromCoordinates_firstFieldCoordinates_returns0(self) -> None:
        field_coordinate = Coordinate(1, 1)
        list_index = self.gamefield._calculate_list_index_from_coordinates(field_coordinate)
        self.assertEqual(list_index, 0)

    def test__calculateListIndexFromCoordinates_lastFieldCoordinates_returnsLastIndex(self) -> None:
        field_coordinate = Coordinate(SQUARE_GAMEFIELD_SIZE, SQUARE_GAMEFIELD_SIZE)
        list_index = self.gamefield._calculate_list_index_from_coordinates(field_coordinate)
        self.assertEqual(list_index, SQUARE_GAMEFIELD_SIZE ** 2 - 1)

    def test__getFieldFromCoordinates_firstFieldCoordinates_returnsFirstField(self):
        field = self.gamefield._get_field_from_coordinates(1, 1)
        self.assertEqual(field.coordinates.column, 1)
        self.assertEqual(field.coordinates.row, 1)

    def test__getFieldFromCoordinates_lastFieldCoordinates_returnsLastField(self):
        field = self.gamefield._get_field_from_coordinates(SQUARE_GAMEFIELD_SIZE, SQUARE_GAMEFIELD_SIZE)
        self.assertEqual(field.coordinates.column, SQUARE_GAMEFIELD_SIZE)
        self.assertEqual(field.coordinates.row, SQUARE_GAMEFIELD_SIZE)

    def test_getColumnFields_firstColumn_yieldsFirstColumn(self):
        generator = self.gamefield.get_column_fields(1)
        self.assertEqual(next(generator), Field(Coordinate(1, 1), ""))
        for field in generator: pass
        self.assertEqual(field, Field(Coordinate(1, SQUARE_GAMEFIELD_SIZE), ""))

    def test_getRowFields_firstRow_yieldsFirstRow(self):
        generator = self.gamefield.get_row_fields(1)
        self.assertEqual(next(generator), Field(Coordinate(1, 1), ""))
        for field in generator: pass
        self.assertEqual(field, Field(Coordinate(SQUARE_GAMEFIELD_SIZE, 1), ""))

    def test_getLeftDiagonalFields_leftDiagonal_yieldsLeftDiagonalFields(self):
        generator = self.gamefield.get_left_diagonal_fields( )
        self.assertEqual(next(generator), Field(Coordinate(1, 1), ""))
        for field in generator: pass
        self.assertEqual(field, Field(Coordinate(SQUARE_GAMEFIELD_SIZE, SQUARE_GAMEFIELD_SIZE), ""))

    def test_getRightDiagonalFields_rightDiagonal_yieldsRightDiagonalFields(self):
        generator = self.gamefield.get_right_diagonal_fields( )
        self.assertEqual(next(generator), Field(Coordinate(SQUARE_GAMEFIELD_SIZE, 1), ""))
        for field in generator: pass
        self.assertEqual(field, Field(Coordinate(1, SQUARE_GAMEFIELD_SIZE), ""))

    def test_getFieldsPerRow_returnsRowFields(self):
        generator = self.gamefield.get_fields_per_row( )
        self.assertEqual(next(next(generator)), Field(Coordinate(1, 1), ""))
        for row_fields in generator: pass
        self.assertEqual(next(row_fields), Field(Coordinate(1, SQUARE_GAMEFIELD_SIZE), ""))

    def test_getFieldsPerColumn_returnsColumnFields(self):
        generator = self.gamefield.get_fields_per_column()
        self.assertEqual(next(next(generator)), Field(Coordinate(1, 1), ""))
        for column_fields in generator: pass
        self.assertEqual(next(column_fields), Field(Coordinate(SQUARE_GAMEFIELD_SIZE, 1)))

