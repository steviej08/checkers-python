import random

from src.MCTS.Node import Node


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

    selection(node)


def choose_child(children):
    """
    Choose the best weighted child
    :param children: List of nodes
    :return: Node
    """
    if children is None or children.len < 1:
        raise Exception("Children must exist")
    children.sort()
    return children(0)


def expansion(node):
    """
    Choose a random node to expand to
    TODO: This could be extended to choose multiple nodes
    TODO: The chosen node will affect state (i.e. whose turn)
    :param node:
    :return:
    """
    children = node.children
    if children is None or children.len < 1:
        raise Exception("Children must exist")
    return random.choice(node.children)


def simulation(state, node, simulate):
    """
    Simulate the game until there is a winner
    :param state: The current state of the game
    :param node: The expanded node chosen to start simulation
    :param simulate: Function that takes a state and node and returns a new state
    :return: Winning node
    """
    old_node = node
    new_node = node
    chosen_move = old_node.get_move_id()

    while True:
        new_state = simulate(state, chosen_move)
        winner = new_state.get_winner
        move_id = random.choice(new_state.get_valid_moves)
        if winner is not None:
            new_node = Node(move_id, old_node)
            old_node = new_node
        else:
            break

    return new_node


def backpropagation(node):
    """
    Update nodes with new weights based on simulation
    :param node: Winning node
    :return: root node
    """
    raise NotImplemented
