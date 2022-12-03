class Individuo:

    def __init__(self, id, board, generation) -> None:
        self.id = id
        self.board = board[8]
        self.generation = generation