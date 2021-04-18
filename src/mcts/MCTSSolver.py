from src.mcts.MCTS import *
from src.mcts.Node import Node
from time import monotonic

max_iter = "MAX_ITERATIONS"
max_time_s = "MAX_TIME_SECS"
expansion_choose_meth = "EXPANSION_METHOD"
simulation_choose_meth = "SIMULATION_METHOD"

default_options = {
    max_iter: 10,
    max_time_s: 10,
    expansion_choose_meth: random.choice,
    simulation_choose_meth: random.choice
}


class MCTSSolver:

    def __init__(self, start_player, simulate, options=None):
        if options is None:
            options = default_options
        self.simulate = simulate
        self.search_tree = Node.root(start_player)
        self.max_iter = options[max_iter] if max_iter in options else default_options[max_iter]
        self.max_time = options[max_time_s] if max_time_s in options else default_options[max_time_s]

        if self.max_time == 0 and self.max_iter == 0:
            raise Exception("Max time (s) and max iteration cannot both be equal to 0")

        self.expansion_method = options[expansion_choose_meth] if expansion_choose_meth in options else \
            default_options[expansion_choose_meth]
        self.simulation_method = options[simulation_choose_meth] if simulation_choose_meth in options else \
            default_options[simulation_choose_meth]

    def add_init_moves(self, start_player, move_ids):
        if self.search_tree.has_children():
            return self

        self.search_tree.set_children(
            list(map(lambda m: Node(m, start_player, self.search_tree), move_ids))
        )

        return self

    def get_move(self, move_ids):

        current_time = monotonic()
        to_stop = current_time + self.max_time
        curr_iter = 0

        def continue_solve():
            if self.max_time != 0 and monotonic() < to_stop:
                return False
            if self.max_iter != 0 and curr_iter >= self.max_iter:
                return False

            return True

        while continue_solve():
            curr_iter += 1
            selected_node = selection(self.search_tree)

            # add children to selected node
            state = self.get_state_for(selected_node)

            leaf_node = selected_node
            winner = state.get_winner()

            # if the state has no children then we have played out a whole game
            # therefore no need to expand
            if len(state.get_valid_moves()) > 0:
                selected_node.set_children(
                    list(map(lambda m: Node(m, state.get_player(), selected_node), state.get_valid_moves()))
                )
                expanded_node = expansion(selected_node, self.expansion_method)

                leaf_node, winner = simulation(state, expanded_node, self.simulate, self.simulation_method)

            backpropagation(leaf_node, winner)

        next_node = self.search_tree

        for move_id in move_ids:
            next_node = next_node.children[move_id]

        if not next_node.has_children():
            return None

        node = choose_child(next_node.children)
        return node.get_move_id()

    def get_state_for(self, node):

        if node is None:
            raise Exception("Node cannot be none")

        moves = []

        def get_move(inner_node):
            if inner_node.is_root():
                return
            moves.append(inner_node)
            get_move(inner_node.get_parent())

        get_move(node)

        state = self.simulate(moves[len(moves)-1].get_move_id())

        skip = True

        for n in reversed(moves):
            if skip:
                skip = False
                continue
            new_state = self.simulate(n.get_move_id(), state)
            state = new_state

        return state
