class Counter:

    def __init__(self, counter_id, colour, position, is_king=False):
        self.id = counter_id
        self.is_king = is_king
        self.position = position
        self.colour = colour

    def king(self):
        return Counter(self.id, is_king=True, position=self.position)
