from console.Console import Console
from console.Draw import draw_state
from console.Interaction import ask_to_move, ask_to_choose_counter
from game.Actions import Colour
from game.State import State


class CheckersConsole(Console):

    def work(self):
        # initial state
        state = State()

        draw_state(state, State.board_size)

        print("")

        # start game
        while not state.has_finished():
            counter_to_move = ask_to_choose_counter(state, state.get_turn(), self)
            new_state = ask_to_move(state, state.get_turn(), counter_to_move, self)

            print("")
            print("New State:\n")

            draw_state(new_state, State.board_size)


game = CheckersConsole()

try:
    game.start()
except Exception as exc:
    print(exc)


