from pieces import *
class Board:

    def __init__(self):
        self.grid = [['x' for i in range(8)] for i in range(8)]

    def contents(self):

        def reversed_list(lst):
            result = []
            for e in lst:
                if isinstance(e, list):
                    result.append(reversed_list(e))
                else:
                    result.append(e)

            result.reverse()

            return result

        print(*reversed_list(self.grid), sep = "\n")

    def is_empty(self, x, y):
        if self.grid[y][x] == 'x':
            return True
        return False

    def make_new_piece(self, piece, team, x, y):
        if self.is_empty(x, y):
            created_piece = self.grid[y][x] = piece(team, x, y)
            print(f"{created_piece.team} {created_piece.name} created on \
                    [{created_piece.x}, {created_piece.y}]")

    def move(self, piece, new_x, new_y):
        if (new_x, new_y) in piece.legal_moves:
            self.grid[new_x][new_y] = piece
            self.grid[piece.x][piece.y] = 'x'
            piece.update_coords(new_x, new_y)

    def reset_board(self):
        for i in range(8):
            self.make_new_piece(Pawn, 'White', i, 1)
            self.make_new_piece(Pawn, 'Black', i, 6)

        pieces = (Rook, Knight, Bishop)
        for i in range(3):
            piece = pieces[i]
            self.make_new_piece(piece, 'White', 7-i, 0)
            self.make_new_piece(piece, 'White', 0+i, 0)
            self.make_new_piece(piece, 'Black', 7-i, 7)
            self.make_new_piece(piece, 'Black', 0+i, 7)

        self.make_new_piece(Queen, 'White', 3, 0)
        self.make_new_piece(King, 'White', 4, 0)
        self.make_new_piece(Queen, 'Black', 3, 7)
        self.make_new_piece(King, 'White', 4, 7)

board = Board()
board.reset_board()
board.contents()

