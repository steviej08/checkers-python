def ask_to_move(state, player):
    user_from_position = ""

    while not validate_position(user_from_position):
        user_from_position = str(input("Enter the position to move in format x,y: "))

    from_position = convert_user_position(user_from_position)

    valid_positions = state.get_valid_moves(from_position)


def validate_position(position):
    return True


def convert_user_position(position):
    return 0, 0
