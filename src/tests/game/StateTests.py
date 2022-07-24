import unittest

from game.Actions import Colour
from game.State import State

# | O - O - O - O -  |
# | - O - O - O - O  |
# | O - O - O - O -  |
# | - - - - - - - -  |
# | - - - - - - - -  |
# | - X - X - X - X  |
# | X - X - X - X -  |
# | - X - X - X - X  |


class TestState(unittest.TestCase):

    def test_get_valid_moves_none(self):
        state = State()

        for i in range(7):
            with self.subTest(i=i):
                valid_moves = state.get_valid_moves(Colour.White, i)
                self.assertEqual(0, len(valid_moves), "Should be no valid moves")

    def test_get_valid_moves_two(self):
        state = State()

        for i in [9, 10]:
            with self.subTest(i=i):
                valid_moves = state.get_valid_moves(Colour.White, i)
                self.assertEqual(2, len(valid_moves), "Should be 2 valid moves")

    def test_get_moves_for(self):
        state = State()

        valid_moves = state.get_moves_for(Colour.White)

        self.assertEqual(4, len(valid_moves))
        self.assertEqual((2, 0), valid_moves[8].position)
        self.assertEqual((2, 2), valid_moves[9].position)
        self.assertEqual((2, 4), valid_moves[10].position)
        self.assertEqual((2, 6), valid_moves[11].position)

    def test_when_move_correct(self):
        state = State()

        self.assertEqual(Colour.White, state.get_turn())

        valid_moves = state.get_valid_moves(Colour.White, 7)

        to_position = valid_moves[int(0)]
        move_state = state.new_white_position(7, to_position)
        new_state = move_state.next_turn()

        new_position = new_state.get_position(Colour.White, 7)

        self.assertEqual(Colour.Black, new_state.get_turn())
        self.assertEqual((2, 8), new_position)


if __name__ == '__main__':
    unittest.main()
