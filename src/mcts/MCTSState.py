from abc import ABC, abstractmethod


class MCTSState(ABC):

    @abstractmethod
    def get_winner(self):
        pass

    @abstractmethod
    def get_valid_moves(self):
        pass

    @abstractmethod
    def get_player(self):
        pass
