from Logic import Color


class State:
    board_size = (8, 8)

    @staticmethod
    def init_black_positions():
        return State.gen_start_positions(8, 8, -1)

    @staticmethod
    def init_white_positions():
        return State.gen_start_positions(0, 0, 1)

    @staticmethod
    def gen_start_positions(x, y, direction):

        inner_x = x
        inner_y = y

        checker_count = State.counter_count()
        checker_list = range(checker_count)

        indent = False
        positions = {}

        for n in checker_list:
            positions[n] = (inner_x, inner_y)
            inner_x += direction
            if inner_x == State.board_size[0]:
                inner_y += direction
                inner_x = direction if indent else 0
                indent = not indent

        return positions

    @staticmethod
    def counter_count():

        if State.board_size[0] % 2 != 0:
            raise Exception("Board Size is invalid.")

        return int((State.board_size[0] / 2) * 3)

    def __init__(self, black_positions=None, white_positions=None):

        if black_positions is None:
            self._blackPositions = State.init_black_positions()
        else:
            self._blackPositions = black_positions

        if white_positions is None:
            self._whitePositions = State.init_white_positions()
        else:
            self._whitePositions = white_positions

    def get_with_new_positions(self, colour, positions):
        if colour == Color.Black:
            return State(positions, self._whitePositions)

        return State(self._blackPositions, positions)

    def get_position(self, color, checker):

        if checker not in range(State.counter_count()):
            raise Exception("Checker ID is invalid.")

        if color == Color.Black:
            return self._blackPositions[checker]

        return self._whitePositions[checker]

    def get_with_new_position(self, colour, checker, position):

        if checker not in range(State.counter_count()):
            raise Exception("Checker ID is invalid.")

        positions = self._blackPositions.copy() if colour == Color.Black else self._whitePositions.copy()

        positions[checker] = position

        return self.get_with_new_positions(colour, positions)

    def get_with_removed_counter(self, colour, checker):

        if checker not in range(State.counter_count()):
            raise Exception("Checker ID is invalid.")

        positions = self._blackPositions.copy() if colour == Color.Black else self._whitePositions.copy()

        del positions[checker]

        return self.get_with_new_positions(colour, positions)

    def has_finished(self):
        if len(self._blackPositions) == 0:
            return Color.Black
        if len(self._whitePositions) == 0:
            return Color.White
        return None
