import unittest

from src.mcts.MCTSSolver import MCTSSolver, max_iter, max_time_s, expansion_choose_meth, simulation_choose_meth
from NaughtCrossesState import NaughtCrossesState


def simulate(move, state=None):
    current_state = NaughtCrossesState() if state is None else state
    new_state = current_state.play_move(move)
    if new_state is None:
        raise Exception("Invalid move ", move)
    return new_state.next_player()


class MCTSTests(unittest.TestCase):

    def test_one_iteration_creates_correct_tree(self):
        start_player = True

        options = {
            max_iter: 1,
            max_time_s: 0,
            expansion_choose_meth: lambda children: children[0],
            simulation_choose_meth: lambda children: children[0]
        }

        start_state = NaughtCrossesState()

        mcts_solver = MCTSSolver(start_player, simulate, options)\
            .add_init_moves(start_player, start_state.get_valid_moves())

        move_id = mcts_solver.get_move([])
        self.assertEqual(move_id, 0)

    def test_three_iteration_full_game_correct_tree(self):
        start_player = True

        options = {
            max_iter: 3,
            max_time_s: 0,
            expansion_choose_meth: lambda children: children[0],
            simulation_choose_meth: lambda children: children[0]
        }

        move_history = []

        start_state = NaughtCrossesState()

        mcts_solver = MCTSSolver(start_player, simulate, options)\
            .add_init_moves(start_player, start_state.get_valid_moves())

        # I am player 1 - I go for the middle
        move_1 = 4
        move_history.append(move_1)

        move_2 = mcts_solver.get_move(move_history)
        move_history.append(move_2)

        self.assertEqual(move_2, 0)

        move_3 = 1
        move_history.append(move_3)

        move_4 = mcts_solver.get_move(move_history)
        move_history.append(move_4)

        self.assertEqual(move_4, 2)

        move_5 = 7
        move_history.append(move_5)

        final_move = mcts_solver.get_move(move_history)

        self.assertIsNone(final_move)


