from src.mcts.MCTS import *
from src.mcts.Node import Node
from time import monotonic


class MCTSSolver:

    def __init__(self, start_player, simulate):
        self.simulate = simulate
        self.search_tree = Node.root(start_player)

    def get_move(self, move_ids):

        # give the solver 10 seconds to choose its move
        current_time = monotonic()
        to_stop = current_time + 10

        while monotonic() < to_stop:
            selected_node = selection(self.search_tree)

            # add children to selected node
            state = self.get_state_for(selected_node)
            selected_node.set_children(
                map(lambda m: Node(m, state.get_player()), state.get_valid_moves()))

            expanded_node = expansion(selected_node)

            state, leaf_node = simulation(state, expanded_node, self.simulate)

            backpropagation(leaf_node, state.get_player())

        next_node = self.search_tree

        for move_id in move_ids:
            next_node = next_node.children[move_id]

        return choose_child(next_node.children)

    def get_state_for(self, node):

        moves = []

        def get_move(inner_node):
            if inner_node.is_parent():
                return
            moves.append(inner_node)
            get_move(inner_node.get_parent())

        get_move(node)

        state = self.simulate()

        for n in reversed(moves):
            new_state = self.simulate(state, n.get_move_id())
            state = new_state

        return state

