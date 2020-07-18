from src.game.Logic import move


def ask_to_choose_counter(state, player):
    counter = ""

    is_valid_position = False

    counters = state.get_moves_for(player)

    while not is_valid_position:
        options = ["" + str(k) + ". (" + str(v[0]) + ", " + str(v[1]) + ")\n" for k, v in counters.items()]
        counter = str(input("Enter the counter to move: \n" + " ".join(options)))
        is_valid_position = validate_counter(counter, [k for k, v in counters.items()])

        if not is_valid_position:
            print(counter, " is not a valid counter id.")

    return int(counter)


def validate_counter(counter, ids):
    try:
        int(counter)
    except ValueError:
        return False

    if int(counter) in ids:
        return True

    return False


def ask_to_move(state, player, counter_id):
    move_position = ""

    valid_moves = state.get_valid_moves(player, counter_id)

    is_valid_position = False

    while not is_valid_position:
        move_position = \
            str(input(
                "Enter the position to play: " + " ".join(str("" + str(k) + ". (" + str(v[0]) + ", " + str(v[1]) + ")\n")
                                                          for k, v in enumerate(valid_moves))))
        is_valid_position = validate_position(move_position, valid_moves)

        if not is_valid_position:
            print(move_position, " is not a valid position...")

    to_position = valid_moves[int(move_position)]
    new_state = move(state, player, to_position, counter_id)

    return new_state


def validate_position(position, move_ids):
    try:
        int(position)
    except ValueError:
        return False

    if len(move_ids) > int(position) > -1:
        return True

    return False


def do_quit():
    quit_val = str(input("Continue? (Quit or Q)")).upper()
    if quit_val == "QUIT" or quit_val == "Q":
        return True
    return False