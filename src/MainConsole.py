from src.console.Draw import draw_state
from src.console.UserInteractions import do_quit, ask_to_move, ask_to_choose_counter
from src.game.Actions import Colour
from src.game.State import State

# initial state
state = State()

draw_state(state, State.board_size)

print("")

player = Colour.White

# start game
while not do_quit():

    counter_to_move = ask_to_choose_counter(state, player)
    new_state = ask_to_move(state, player, counter_to_move)

    print("")
    print("New State:\n")

    draw_state(state, State.board_size)

    player = not player

