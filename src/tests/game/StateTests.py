import unittest

from src.game.Actions import Colour
from src.game.State import State

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


if __name__ == '__main__':
    unittest.main()
