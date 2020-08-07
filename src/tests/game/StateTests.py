import unittest

from src.game.Logic import Color
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

        valid_moves = state.get_valid_moves(Color.White, 0)

        self.assertEqual(0, len(valid_moves), "Should be no valid moves")


if __name__ == '__main__':
    unittest.main()
