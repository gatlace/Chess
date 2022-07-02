from pieces import *


class Board:
    """Board where all the information is stored"""

    def __init__(self):
        self.board: list[list[Piece]] = [
            [Empty('', i, j) for i in range(8)] for j in range(8)]

        self.teams: dict[str: list] = {'white': [], 'black': []}
        self.turn = 'white'
        self.init_game()
        self.get_teams()

    def get_legal_moves(self):
        """Gets the legal moves for each piece"""
        team = self.teams[self.turn]
        for piece in team['pieces']:
            piece.get_legal_moves(board.teams_board())
            print(piece.position, piece.legal_moves)

    def get_teams(self):
        """Gets/Updates the teams"""
        self.teams = {'white': {
            'pieces': [],
            'legal_moves': [],
        }, 'black': {
            'pieces': [],
            'legal_moves': [],
        }}
        for row in self.board:
            for piece in row:
                if piece.color == 'white':
                    self.teams['white']['pieces'].append(piece)
                elif piece.color == 'black':
                    self.teams['black']['pieces'].append(piece)

    def init_game(self):
        """initialize the board with pieces"""

        self.board[0] = [
            Rook('white', 0, 0), Knight('white', 1, 0), Bishop(
                'white', 2, 0), Queen('white', 3, 0),
            King('white', 4, 0), Bishop('white', 5, 0), Knight(
                'white', 6, 0), Rook('white', 7, 0)
        ]
        self.board[1] = [
            Pawn('white', 0, 1), Pawn('white', 1, 1), Pawn(
                'white', 2, 1), Pawn('white', 3, 1),
            Pawn('white', 4, 1), Pawn('white', 5, 1), Pawn(
                'white', 6, 1), Pawn('white', 7, 1)

        ]

        self.board[7] = [
            Rook('black', 0, 7), Knight('black', 1, 7), Bishop(
                'black', 2, 7), Queen('black', 3, 7),
            King('black', 4, 7), Bishop('black', 5, 7), Knight(
                'black', 6, 7), Rook('black', 7, 7)
        ]

        self.board[6] = [
            Pawn('black', 0, 6), Pawn('black', 1, 6), Pawn(
                'black', 2, 6), Pawn('black', 3, 6),
            Pawn('black', 4, 6), Pawn('black', 5, 6), Pawn(
                'black', 6, 6), Pawn('black', 7, 6)
        ]

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
        """Switches the turn"""
        if self.turn == 'white':
            self.turn = 'black'
        elif self.turn == 'black':
            self.turn = 'white'

    def print_board(self):
        """Prints the Visual Representation of the board"""
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
                        return_string += f"{' ':^14}"
                    else:
                        return_string += f"{str(self.board[i][j]):^14}"
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
                        return_string += f"{' ':^14}"
                    else:
                        return_string += f"{str(self.board[i][j]):^14}"
                    return_string += "|"
                return_string += "\n"

                return_string += "  |"
                for i in range(8):
                    return_string += "-" * 14+"|"
                return_string += "\n"

        return_string += "  "

        for i in files:
            return_string += f"{i:^15}"

        return return_string

    def teams_board(self):
        """Returns a board with the teams"""
        new_board = []
        for row in self.board:
            new_row = []
            for piece in row:
                new_row.append(piece.color)
            new_board.append(new_row)

        return new_board

    def get_move(self):
        """Gets the move from the user"""
        print(self.print_board())
        old_coord = input("Enter old coordinate: ").split(",")
        new_coord = input("Enter new coordinate: ").split(",")
        self.move_piece(old_coord, new_coord)


board = Board()
board.get_legal_moves()
