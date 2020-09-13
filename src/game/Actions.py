import enum


class Direction(enum.Enum):
    NorthWest = 1
    NorthEast = 2
    SouthWest = 3
    SouthEast = 4


class Colour(enum.Enum):
    Black = True
    White = False


def move(state, colour, count_id, new_position):

    position = state.get_position(colour, count_id)

    if abs(position[0] - new_position[0]) == 2:
        return move(state, colour, count_id, new_position)

    if not check_move_constraint(state, colour, count_id, new_position):
        raise Exception("Incorrect parameters.")

    move_state = state.new_black_position(count_id, new_position) if colour == Colour.Black \
        else state.new_white_position(count_id, new_position)

    return move_state.next_turn()


def check_move_constraint(state, colour, count_id, new_position):

    possible_moves = state.get_valid_moves(colour, count_id)

    if new_position not in possible_moves:
        return False

    position = state.get_position(colour, count_id)

    return abs(position[0] - new_position[0]) == 1


def take(state, colour, count_id, new_position):

    if not check_take_constraint(state, colour, count_id, new_position):
        raise Exception("Incorrect parameters.")

    move_state = state.new_black_position(count_id, new_position) if colour == Colour.Black \
        else state.new_white_position(count_id, new_position)

    position = state.get_position(colour, count_id)

    expected_take_position = [int(position(0) + ((position(0) - new_position(0))/2)),
                              int(position(1) + ((position(1) - new_position(1))/2))]

    take_counter = state.get_at_position(expected_take_position[0], expected_take_position[1])

    if take_counter is None:
        raise Exception("Unable to take as nothing to take.")

    return move_state.get_with_removed_counter(not colour, take_counter.id)


def check_take_constraint(state, colour, count_id, new_position):

    possible_moves = state.get_valid_moves(colour)

    if new_position not in possible_moves:
        return False

    position = state.get_position(colour, count_id)

    if abs(position(0) - new_position(0)) != 2:
        return False

    expected_take_position = [int(position(0) + ((position(0) - new_position(0))/2)),
                              int(position(1) + ((position(1) - new_position(1))/2))]

    take_counter = state.get_for_row(expected_take_position[1])[expected_take_position]

    return take_counter[0] == "w" if colour == Colour.Black else take_counter[1] == "b"
