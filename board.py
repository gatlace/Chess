from pieces import *
class Board:

    def __init__(self):
        self.grid = [['x' for i in range(8)] for i in range(8)]

    def contents(self):
                print(*self.grid, sep='\n')

    def is_empty(self, x, y):
        if self.grid[y][x] == 'x':
            return True
        return False

    def make_new_piece(self, piece, team, x, y):
        if self.is_empty(x, y):
            created_piece = self.grid[y][x] = piece(team, x, y)
            print(f"{created_piece.team} {created_piece.name} created on [{created_piece.x}, {created_piece.y}]")

    def move(self, piece, new_x, new_y):
        if (new_x, new_y) in piece.legal_moves:
            self.grid[new_x][new_y] = piece
            self.grid[piece.x][piece.y] = 'x'
            piece.update_coords(new_x, new_y)

    def reset_board(self):
        for i in range(8):
            self.make_new_piece(Pawn, 'White', i, 1)
            self.make_new_piece(Pawn, 'Black', i, 6)

board = Board()
board.reset_board()

board.contents()

