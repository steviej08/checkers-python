from src.game.Logic import Color


class State:
    board_size = (8, 8)

    @staticmethod
    def init_black_positions():
        return State.gen_start_positions(7, 7, -1)

    @staticmethod
    def init_white_positions():
        return State.gen_start_positions(0, 0, 1)

    @staticmethod
    def gen_start_positions(x, y, direction):

        inner_x = x
        inner_y = y

        checker_count = State.counter_count()
        checker_list = range(checker_count)

        indent = True
        positions = {}

        for n in checker_list:
            positions[n] = (inner_x, inner_y)
            inner_x += (direction * 2)
            if inner_x >= State.board_size[0] or inner_x <= -1:
                inner_y += direction
                inner_x = x + direction if indent else x
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

    def get_position(self, color, checker):

        if checker not in range(State.counter_count()):
            raise Exception("Checker ID is invalid.")

        if color == Color.Black:
            return self._blackPositions[checker]

        return self._whitePositions[checker]

    def new_black_positions(self, positions):
        return State(positions, self._blackPositions)

    def new_white_positions(self, positions):
        return State(self._blackPositions, positions)

    def new_black_position(self, checker, position):

        if checker not in range(State.counter_count()):
            raise Exception("Checker ID is invalid.")

        positions = self._blackPositions.copy()

        positions[checker] = position

        return self.new_black_positions(positions)

    def new_white_position(self, checker, position):

        if checker not in range(State.counter_count()):
            raise Exception("Checker ID is invalid.")

        positions = self._whitePositions.copy()

        positions[checker] = position

        return self.new_black_positions(positions)

    def remove_black_counter(self, checker):

        if checker not in range(State.counter_count()):
            raise Exception("Checker ID is invalid.")

        positions = self._blackPositions.copy()

        del positions[checker]

        return self.new_black_positions(positions)

    def remove_white_counter(self, checker):

        if checker not in range(State.counter_count()):
            raise Exception("Checker ID is invalid.")

        positions = self._whitePositions.copy()

        del positions[checker]

        return self.new_white_positions(positions)

    def get_for_row(self, y):
        black_row = {v: "b" + str(k) for (k, v) in self._blackPositions.items() if v[1] == y}
        white_row = {v: "w" + str(k) for (k, v) in self._whitePositions.items() if v[1] == y}

        to_ret = dict(black_row)
        to_ret.update(white_row)
        return to_ret

    def has_finished(self):
        if len(self._blackPositions) == 0:
            return Color.Black
        if len(self._whitePositions) == 0:
            return Color.White
        return None

    def get_valid_moves(self, colour, counter_id):
        my_counters = self._blackPositions if colour == Color.Black else self._whitePositions
        their_counters = self._blackPositions if colour == Color.White else self._whitePositions

        current_position = my_counters[counter_id]

        all_possible_moves = [(current_position[0] + x, current_position[1] + y)
                              for y in [-2, -1, 1, 2] for x in [-2, -1, 1, -2] if abs(x) == abs(y)]

        def is_valid(position):
            all_positions = list(my_counters.values()) + list(their_counters.values())

            if position in all_positions:
                return False

            is_outer = abs(position[0] - current_position[0]) == 2

            if not is_outer:
                return True

            between_pos = (position[0] - current_position[0] / 2, position[1] - current_position[1] / 2)

            return True if between_pos in their_counters.values() else False

        valid_positions = [x for x in all_possible_moves if is_valid(x)]

        return valid_positions

    def get_moves_for(self, colour):
        all_positions = self._blackPositions if colour == Color.Black else self._whitePositions
        return {k: v for k, v in all_positions.items() if len(self.get_valid_moves(colour, k)) != 0}
