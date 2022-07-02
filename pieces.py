"""Piece definitions"""


class Piece:
    """Generic Piece; not used directly"""

    def __init__(self, color, x, y):
        self.color: str = color
        self.x: int = x
        self.y: int = y
        self.legal_moves: list[tuple] = []

    @property
    def position(self):
        """returns a tuple of the position of the piece"""
        return self.x, self.y

    @position.setter
    def position(self, position):
        self.x, self.y = position

    def __str__(self):
        return self.color.capitalize() + ' ' + self.__class__.__name__

    def __repr__(self):
        return self.color.capitalize() + ' ' + self.__class__.__name__

    def get_legal_moves(self, board: list[list[str]]):
        """Get legal moves for this piece"""


class Pawn(Piece):
    """Pawn"""

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'pawn'
        self.value = 1

    def get_legal_moves(self, board):
        moves = []
        x, y = self.x, self.y
        if self.color == 'black':
            if y != 6:
                moves.extend([(x, y-1)])
            else:
                moves.extend([(x, y-1), (x, y-2)])
        elif self.color == 'white':
            if y != 1:
                moves.extend([(x, y+1)])
            else:
                moves.extend([(x, y+1), (x, y+2)])

        self.legal_moves = moves

    def get_capture_moves(self):
        """Gets special moves for pawns"""
        moves = []
        x, y = self.x, self.y
        if self.color == 'black':
            moves.append((x + 1, y - 1))
            moves.append((x - 1, y - 1))
        elif self.color == 'white':
            moves.append((x + 1, y + 1))
            moves.append((x - 1, y + 1))

        for move in moves:
            x, y = move
            if x < 0 or x > 7 or y < 0 or y > 7:
                moves.remove(move)

        return moves


class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'rook'
        self.value = 5

    def get_legal_moves(self, board):
        up, down, left, right = True, True, True, True
        x, y = self.x, self.y
        moves = []
        for i in range(1, 8):
            if up:
                if x+i > 7:
                    up = False
                    continue

                move = (x+i, y)
                if board[move[0]][move[1]] == 'e':
                    moves.append(move)
                else:
                    up = False
                    if board[move[0]][move[1]] != self.color[0]:
                        moves.append(move)
            if down:
                if x-i < 0:
                    down = False
                    continue

                move = (x-i, y)
                if board[move[0]][move[1]] == 'e':
                    moves.append(move)
                else:
                    down = False
                    if board[move[0]][move[1]] != self.color[0]:
                        moves.append(move)
            if left:
                if y-i < 0:
                    left = False
                    continue

                move = (x, y-i)
                if board[move[0]][move[1]] == 'e':
                    moves.append(move)
                else:
                    left = False
                    if board[move[0]][move[1]] != self.color[0]:
                        moves.append(move)
            if right:
                if x-i < 0:
                    right = False
                    continue

                move = (x - i, y)
                if board[move[0]][move[1]] == 'e':
                    moves.append(move)
                else:
                    right = False
                    if board[move[0]][move[1]] != self.color[0]:
                        moves.append(move)

        self.legal_moves = moves
        return moves


class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'bishop'
        self.value = 3

    def get_legal_moves(self, board):
        x, y = self.x, self.y
        moves = []

        up_left, up_right, down_left, down_right = True, True, True, True
        for i in range(1, 8):
            if up_left is True:
                if x+i > 7 or y-i < 0:
                    up_left = False
                    continue

                move = (x+i, y-i)
                if board[move[0]][move[1]] == 'e':
                    moves.append(move)
                else:
                    up_left = False
                    if board[move[0]][move[1]] != self.color[0]:
                        moves.append(move)

            if up_right is True:
                if x+i > 7 or y+i > 7:
                    up_right = False
                    continue

                move = (x+i, y+i)
                if board[move[0]][move[1]] == 'e':
                    moves.append(move)
                else:
                    up_right = False
                    if board[move[0]][move[1]] != self.color[0]:
                        moves.append(move)

            if down_left is True:
                if x-i < 0 or y-i < 0:
                    down_left = False
                    continue

                move = (x-i, y-i)
                if board[move[0]][move[1]] == 'e':
                    moves.append(move)
                else:
                    down_left = False
                    if board[move[0]][move[1]] != self.color[0]:
                        moves.append(move)

            if down_right is True:
                if x-i < 0 or y+i > 7:
                    down_right = False
                    continue

                move = (x-i, y+i)
                if board[move[0]][move[1]] == 'e':
                    moves.append(move)
                else:
                    down_right = False
                    if board[move[0]][move[1]] != self.color[0]:
                        moves.append(move)

        self.legal_moves = moves
        return moves


class Queen(Rook, Bishop):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'queen'
        self.value = 9

    def get_legal_moves(self, board):
        return Rook.get_legal_moves(self, board).extend(Bishop.get_legal_moves(self, board))


class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'knight'
        self.value = 3

    def get_legal_moves(self, board):
        x, y = self.x, self.y
        moves = [
            (x + 1, y + 2),
            (x + 1, y - 2),
            (x - 1, y + 2),
            (x - 1, y - 2),
            (x + 2, y + 1),
            (x + 2, y - 1),
            (x - 2, y + 1),
            (x - 2, y - 1)
        ]

        for move in moves:
            x, y = move
            if x < 0 or x > 7 or y < 0 or y > 7:
                moves.remove(move)
                continue
            if board[x][y] == self.color[0]:
                moves.remove(move)

        self.legal_moves = moves


class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'king'
        self.value = 100

    def get_legal_moves(self, board):
        x, y = self.x, self.y
        moves = [
            (x + 1, y + 1),
            (x + 1, y),
            (x + 1, y - 1),
            (x, y + 1),
            (x, y - 1),
            (x - 1, y + 1),
            (x - 1, y),
            (x - 1, y - 1)
        ]

        for move in moves:
            x, y = move
            if x < 0 or x > 7 or y < 0 or y > 7:
                moves.remove(move)

        self.legal_moves = moves


class Empty(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'empty'
        self.value = 0

    def get_legal_moves(self):
        return []
