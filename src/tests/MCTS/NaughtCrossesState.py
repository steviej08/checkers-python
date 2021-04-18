from abc import ABC

from src.mcts.MCTSState import MCTSState


def _init_grid():
    return [None for _ in range(NaughtCrossesState.grid_size)]


class NaughtCrossesState(MCTSState, ABC):
    grid_size = 8

    def __init__(self, grid=None, player=True):
        self.grid = _init_grid() if grid is None else grid
        self.player = player

    def get_valid_moves(self):
        return [x for x in range(NaughtCrossesState.grid_size) if self.grid[x] is None]

    def get_winner(self):
        if self.has_won(True):
            return True
        if self.has_won(False):
            return False

        return None

    def get_player(self):
        return self.player

    def next_player(self):
        return NaughtCrossesState(self.grid, not self.player)

    def play_move(self, position):
        valid_moves = self.get_valid_moves()
        if position not in valid_moves:
            return None

        new_grid = self.grid.copy()
        new_grid[position] = self.player
        return NaughtCrossesState(new_grid, self.player)

    def has_won(self, symbol):
        starts = {
            0: [[2, 1], [6, 3], [8, 4]],
            1: [[7, 3]],
            2: [[8, 3], [6, 2]],
            3: [[5, 1]],
            6: [[8, 1]]
        }

        def seek_threes(_start, end, diff):
            subset = self.grid[_start:end:diff]
            all(x == symbol for x in subset)

        for start, values in starts.items():
            for ends in values:
                if seek_threes(start, ends[0] + 1, ends[1]):
                    return True

        return False
