
class Node:

    @staticmethod
    def root(start_player):
        return Node("root", start_player)

    def __init__(self, move_id, player, parent=None):
        self.value = 0
        self.player = player
        self.move_id = move_id
        self.children = []
        self.parent = parent
        self.number_visits = 1
        self.number_wins = 0

        if parent is not None:
            parent.add_child(self)

    def has_children(self):
        return len(self.children) > 0

    def set_children(self, children):
        if type(children) != list:
            raise Exception("Children must be an a list")

        self.children = children

    def get_player(self):
        return self.player

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_move_id(self):
        return self.move_id

    def get_children(self):
        return self.children

    def add_child(self, child):
        self.children.append(child)

    def get_parent(self):
        return self.parent

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return len(self.children) == 0

    def get_number_visits(self):
        return self.number_visits

    def visited(self):
        self.number_visits += 1

    def get_number_wins(self):
        return self.number_wins

    def won(self):
        self.number_wins += 1
