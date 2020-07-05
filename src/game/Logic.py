import enum


class Direction(enum.Enum):
    NorthWest = 1
    NorthEast = 2
    SouthWest = 3
    SouthEast = 4


class Color(enum.Enum):
    Black = True
    White = False


def move(state, color, direction, count_id):
    if check_move_constraint(state, color, direction, count_id):
        raise Exception("Incorrect parameters.")

    checker_position = state.get_black_position(count_id) if color == Color.Black \
        else state.get_white_position(count_id)

    new_position = {
        Direction.NorthWest: (checker_position[0] + 1, checker_position[1] - 1),
        Direction.NorthEast: (checker_position[0] + 1, checker_position[1] + 1),
        Direction.SouthWest: (checker_position[0] - 1, checker_position[1] - 1),
        Direction.SouthEast: (checker_position[0] - 1, checker_position[1] + 1)
    }[direction]

    return state.get_with_new_position(color, count_id, new_position)


def check_move_constraint(state, color, direction, count_id):
    return True


def take(state, color, direction, take_id, taken_id):
    if check_take_constraint(state, color, direction, take_id):
        raise Exception("Incorrect parameters.")

    take_position = state.get_position(color, take_id)

    take_new_position = {
        Direction.NorthWest: (take_position[0] + 2, take_position[1] - 2),
        Direction.NorthEast: (take_position[0] + 2, take_position[1] + 2),
        Direction.SouthWest: (take_position[0] - 2, take_position[1] - 2),
        Direction.SouthEast: (take_position[0] - 2, take_position[1] + 2)
    }[direction]

    state1 = state.get_with_new_position(color, take_id, take_new_position)
    return state1.get_with_removed_counter(not color, taken_id)


def check_take_constraint(state, color, direction, count_id):
    return True
