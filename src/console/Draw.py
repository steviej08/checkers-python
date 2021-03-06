
def draw_state(state, board_size):
    x_count = board_size[0]
    y_count = board_size[1]

    for x in range(x_count):
        this_row = state.get_for_row(x)

        draw_map = {
            "w": "O ",
            "b": "X "
        }

        line_text = [draw_map[this_row[(x, y)][0]] if (x, y) in this_row else "- " for y in range(y_count)]

        to_print = "".join(line_text)

        print("| " + to_print + "|")
