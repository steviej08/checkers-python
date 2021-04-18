import random
from src.mcts.Node import Node


def selection(node):
    """
    Using the root node, select the best weighted child node
    and repeat recursively until find a leaf node
    :param node: A node from tree
    :return: Selected Leaf node
    """
    if node.is_root() and not node.has_children():
        raise Exception("Root node must have children for selection.")

    if not node.has_children():
        return node

    node = choose_child(node.get_children())

    return selection(node)


def choose_child(children):
    """
    Choose the best weighted child
    :param children: List of nodes
    :return: Node
    """
    def take_value(node):
        return node.value

    if children is None or len(children) < 1:
        raise Exception("Children must exist")
    children.sort(key=take_value)
    return children[0]


def expansion(node, choose=random.choice):
    """
    Choose a random node to expand to
    :param choose: Function in which to choose expansion child
    :param node:
    :return:
    """
    children = node.children
    if children is None or len(children) < 1:
        raise Exception("Children must exist")
    return choose(node.get_children())


def simulation(state, node, simulate, simulation_method):
    """
    Simulate the game until there is a winner
    :param simulation_method: function for choosing next node
    :param state: The current state of the game
    :param node: The expanded node chosen to start simulation
    :param simulate: Function that takes a state and node and returns a new state
    :return: Winning node
    """
    new_state = simulate(node.get_move_id(), state)
    winner = state.get_winner()

    if winner is not None:
        return node, winner

    if len(new_state.get_valid_moves()) == 0:
        return node, None

    move_id = simulation_method(new_state.get_valid_moves())
    player = new_state.get_player()
    new_node = Node(move_id, player, node)

    return simulation(new_state, new_node, simulate, simulation_method)


def backpropagation(node, winner):
    """
    Update nodes with new weights based on simulation
    :param node: Winning node
    :param winner: The winner of the previous simulation
    :return: root node
    """
    if node.is_root():
        return node

    if node.is_leaf():
        return backpropagation(node.get_parent(), winner)

    node.visited()
    if winner == node.get_player():
        node.won()

    return backpropagation(node.get_parent(), winner)
