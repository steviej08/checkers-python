from console.Console import Console
from console.Draw import draw_state
from console.Interaction import ask_to_move, ask_to_choose_counter
from game.State import State


class CheckersConsole(Console):

    def work(self):
        # initial state
        state = State()

        print("")

        # start game
        while not state.has_finished():
            draw_state(state, State.board_size)
            print("" + str(state.get_turn()) + "'s turn")
            counter_to_move = ask_to_choose_counter(state, state.get_turn(), self)
            new_state = ask_to_move(state, state.get_turn(), counter_to_move, self)

            print("")
            print("New State:\n")

            state = new_state

        print("" + str(state.has_finished()) + " has won the game. Well done.")


game = CheckersConsole()

try:
    game.start()
except Exception as exc:
    print(exc)


