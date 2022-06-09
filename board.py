from pieces import *


class Board:

    def __init__(self):
        self.board = [[Empty('', i, j) for i in range(8)] for j in range(8)]
        self.teams = {'white': [], 'black': []}
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

        self.get_legal_moves()

    def move_piece(self, old_coord, new_coord):
        old_x, old_y = old_coord
        new_x, new_y = new_coord
        piece = self.board[old_y][old_x]
        if piece.color != self.turn:
            print("It's not your turn!")
            return

        print(piece.type)
        print(piece.legal_moves)
        if new_coord in piece.legal_moves:
            self.board[new_y][new_x] = piece
            self.board[old_y][old_x] = Empty('', old_x, old_y)
            self.next_turn()
        else:
            print("Illegal move")

    def next_turn(self):
        if self.turn == 'white':
            self.turn = 'black'
        elif self.turn == 'black':
            self.turn = 'white'

    def get_legal_moves(self):
        pieces = []
        if self.turn == 'white':
            for row in self.board:
                for piece in row:
                    if piece.color.lower() == 'white':
                        pieces.append(piece)
        elif self.turn == 'black':
            for row in self.board:
                for piece in row:
                    if piece.color.lower() == 'black':
                        pieces.append(piece)

        for piece in pieces:
            piece.get_legal_moves(self.teams_board())

    def play_game(self):
        self.init_game()
        while True:
            coord = input("Enter coordinates: ").split(sep=',')

    def get_teams(self):
        self.teams = {'white': {
            'pawn': 0,
            'rook': 0,
            'knight': 0,
            'bishop': 0,
            'queen': 0,
            'king': 0,
        }, 'black': {
            'pawn': 0,
            'rook': 0,
            'knight': 0,
            'bishop': 0,
            'queen': 0,
            'king': 0,
        }}
        for row in self.board:
            for piece in row:
                if piece.color == 'white':
                    self.teams['white'][piece.type] += 1
                elif piece.color == 'black':
                    self.teams['black'][piece.type] += 1

    def print_board(self):
        ranks = "12345678"
        files = "abcdefgh"
        return_string = "  |"

        for i in range(8):
            return_string += "-" * 14 + "|"
        return_string += "\n"

        if self.turn == 'white':
            for i in range(7, -1, -1):
                return_string += ranks[i] + " |"
                for j in range(8):
                    if self.board[i][j].type == 'empty':
                        return_string += "{:^14}".format(" ")
                    else:
                        return_string += "{:^14}".format(str(self.board[i][j]))
                    return_string += "|"
                return_string += "\n"

                return_string += "  |"
                for i in range(8):
                    return_string += "-" * 14+"|"
                return_string += "\n"
        elif self.turn == 'black':
            for i in range(8):
                return_string += ranks[i] + " |"
                for j in range(7, -1, -1):
                    if self.board[i][j].type == 'empty':
                        return_string += "{:^14}".format(" ")
                    else:
                        return_string += "{:^14}".format(str(self.board[i][j]))
                    return_string += "|"
                return_string += "\n"

                return_string += "  |"
                for i in range(8):
                    return_string += "-" * 14+"|"
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
                new_row.append(piece.color)
            new_board.append(new_row)

        return new_board


board = Board()
board.init_game()
print(board.print_board())
board.move_piece((0, 1), (0, 3))
print(board.print_board())
print(board.turn)
