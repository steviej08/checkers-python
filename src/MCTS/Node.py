
class Node:

    def __init__(self, move_id, parent=None, winner=None):
        self.value = 0
        self.move_id = move_id
        self.children = None
        self.parent = parent
        self.winner = winner

        if parent is not None:
            parent.add_child(self)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_move_id(self):
        return self.move_id

    def get_children(self):
        return self.children

    def add_child(self, child):
        if self.children is None:
            self.children = []
        self.children.append(child)

    def get_parent(self):
        return self.parent

    def is_root(self):
        return self.parent is None

    def is_winner(self):
        return self.winner is not None

    def get_winner(self):
        return self.winner
