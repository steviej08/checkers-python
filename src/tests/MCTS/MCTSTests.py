import unittest

from src.mcts.MCTSSolver import MCTSSolver, max_iter, max_time_s, expansion_choose_meth
from src.tests.MCTS.NaughtCrossesState import NaughtCrossesState


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
            expansion_choose_meth: lambda children: children[0]
        }

        start_state = NaughtCrossesState()

        mcts_solver = MCTSSolver(start_player, simulate, options)\
            .add_init_moves(start_player, start_state.get_valid_moves())

        move_id = mcts_solver.get_move([0])

        self.assertEqual(move_id, 1)
