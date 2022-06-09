from pieces import *


class Board:

    def __init__(self):
        self.teams = ()
        self.board = [[Empty('', i, j) for i in range(8)]
                      for j in range(8)]
        self.turn = 'white'

    def init_game(self):
        self.board[0] = [
            Rook('white', 0, 0), Knight('white', 1, 0), Bishop('white', 2, 0), Queen('white', 3, 0), King(
                'white', 4, 0), Bishop('white', 5, 0), Knight('white', 6, 0), Rook('white', 7, 0)
        ]
        self.board[1] = [
            Pawn('white', 0, 1), Pawn('white', 1, 1), Pawn('white', 2, 1), Pawn('white', 3, 1), Pawn(
                'white', 4, 1), Pawn('white', 5, 1), Pawn('white', 6, 1), Pawn('white', 7, 1)
        ]

        self.board[7] = [
            Rook('black', 0, 7), Knight('black', 1, 7), Bishop('black', 2, 7), Queen('black', 3, 7), King(
                'black', 4, 7), Bishop('black', 5, 7), Knight('black', 6, 7), Rook('black', 7, 7)
        ]

        self.board[6] = [
            Pawn('black', 0, 6), Pawn('black', 1, 6), Pawn('black', 2, 6), Pawn('black', 3, 6), Pawn(
                'black', 4, 6), Pawn('black', 5, 6), Pawn('black', 6, 6), Pawn('black', 7, 6)
        ]

    def print_board(self):
        ranks = "12345678"
        files = "abcdefgh"
        return_string = ""

        for i in range(7, -1, -1):
            return_string += ranks[i] + " |"
            for j in range(8):
                return_string += "{:^14}".format(str(self._board[i][j]))
                return_string += "|"
            return_string += "\n"
        return_string += "  "

        for i in files:
            return_string += "{:^15}".format(i)

        return return_string

    def teams_board(self):
        new_board = []
        for row in self.board:
            new_row = []
            for piece in row:
                if piece.color == '':
                    new_row.append('e')
                else:
                    new_row.append(piece.color[0])
            new_board.append(new_row)

        return new_board

    def get_legal_moves(self):
        pieces = []
        if self.turn == 'white':
            for row in self.board:
                for piece in row:
                    if piece.color == 'white':
                        pieces.append(piece)
        elif self.turn == 'black':
            for row in self.board:
                for piece in row:
                    if piece.color == 'black':
                        pieces.append(piece)

        for piece in pieces:
            piece.get_legal_moves(self.teams_board())


board = Board()
board.init_game()

print(board.teams_board())
