import unittest
from collections.abc import Generator
from ..gamefield import Coordinate, Gamefield, Field
from .. import SQUARE_GAMEFIELD_SIZE


class Test_Gamefield(unittest.TestCase):
    first_field = Field(Coordinate(1, 1), "")
    first_row_last_field = Field(Coordinate(SQUARE_GAMEFIELD_SIZE, 1))
    first_field_last_row = Field(Coordinate(1, SQUARE_GAMEFIELD_SIZE), "")
    last_field = Field(Coordinate(SQUARE_GAMEFIELD_SIZE, SQUARE_GAMEFIELD_SIZE), "")

    last_field_index = SQUARE_GAMEFIELD_SIZE ** 2 - 1

    def setUp(self) -> None:
        self.gamefield = Gamefield( )

    def test__calculateListIndexFromCoordinates_firstFieldCoordinates_returns0(self) -> None:
        field_coordinate = Coordinate(1, 1)
        list_index = self.gamefield._calculate_list_index_from_coordinates(field_coordinate)
        self.assertEqual(list_index, 0)

    def test__calculateListIndexFromCoordinates_lastFieldCoordinates_returnsLastIndex(self) -> None:
        field_coordinate = Coordinate(SQUARE_GAMEFIELD_SIZE, SQUARE_GAMEFIELD_SIZE)
        list_index = self.gamefield._calculate_list_index_from_coordinates(field_coordinate)
        self.assertEqual(list_index, self.last_field_index)

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
        self.verify_generator_returns_fields_as_first_and_last_element(
            generator,
            self.first_field,
            self.first_field_last_row
        )

    def test_getRowFields_firstRow_yieldsFirstRow(self):
        generator = self.gamefield.get_row_fields(1)
        self.verify_generator_returns_fields_as_first_and_last_element(
            generator,
            self.first_field,
            self.first_row_last_field
        )

    def test_getLeftDiagonalFields_leftDiagonal_yieldsLeftDiagonalFields(self):
        generator = self.gamefield.get_left_diagonal_fields( )
        self.verify_generator_returns_fields_as_first_and_last_element(
            generator,
            self.first_field,
            self.last_field
        )

    def test_getRightDiagonalFields_rightDiagonal_yieldsRightDiagonalFields(self):
        generator = self.gamefield.get_right_diagonal_fields( )
        self.verify_generator_returns_fields_as_first_and_last_element(
            generator,
            self.first_row_last_field,
            self.first_field_last_row
        )

    def test_getFieldsPerRow_returnsRowFields(self):
        generator = self.gamefield.get_fields_per_row( )
        self.verify_generator_returns_fields_as_first_and_last_element(
            generator,
            self.first_field,
            self.first_field_last_row
        )

    def test_getFieldsPerColumn_returnsColumnFields(self):
        generator = self.gamefield.get_fields_per_column()
        self.verify_generator_returns_fields_as_first_and_last_element(
            generator,
            self.first_field,
            self.first_row_last_field
        )

    def verify_generator_returns_fields_as_first_and_last_element(self, generator, first_field, last_field):
        first_item = self.get_unpacked_first_generator_item(generator)
        self.assertEqual(first_item, first_field)
        last_item = self.get_unpacked_last_generator_item(generator)
        self.assertEqual(last_item, last_field)


    def is_generator(self, obj):
        return hasattr(obj, '__iter__') or isinstance(obj, Generator)

    def get_unpacked_first_generator_item(self, generator):
        first_item = next(generator)
        if self.is_generator(first_item):
            first_item = next(first_item)
        return first_item

    def get_unpacked_last_generator_item(self, generator):
        for item in generator: pass
        if self.is_generator(item):
            item = next(item)
        return item
