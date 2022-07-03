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
        self.legal_moves.extend(self.get_capture_moves(board))

    def get_capture_moves(self, board):
        """Gets special moves for pawns"""
        moves = []
        x, y = self.x, self.y
        if self.color == 'black':
            moves.append((x + 1, y - 1))
            moves.append((x - 1, y - 1))
        elif self.color == 'white':
            moves.append((x + 1, y + 1))
            moves.append((x - 1, y + 1))

        for move in moves[:]:
            x, y = move
            if x < 0 or x > 7 or y < 0 or y > 7:
                moves.remove(move)
            elif board[y][x] == self.color[0] or board[y][x] == 'e':
                moves.remove(move)

        return moves


class Rook(Piece):
    @classmethod
    def get_rook_moves(cls, position, board):
        up, down, left, right = True, True, True, True
        x, y = position
        moves = []

        for i in range(8):
            if up:
                try:
                    if board[y-i][x] == 'e':
                        moves.append((x, y-i))
                    else:
                        up = False
                except IndexError:
                    up = False
            if down:
                try:
                    if board[y+i][x] == 'e':
                        moves.append((x, y+i))
                    else:
                        down = False
                except IndexError:
                    down = False
            if left:
                try:
                    if board[y][x-i] == 'e':
                        moves.append((x-i, y))
                    else:
                        left = False
                except IndexError:
                    left = False
            if right:
                try:
                    if board[y][x+i] == 'e':
                        moves.append((x+i, y))
                    else:
                        right = False
                except IndexError:
                    right = False

            return moves

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'rook'
        self.value = 5


    def get_legal_moves(self, board):
        self.legal_moves = Rook.get_rook_moves(self.position, board)


class Bishop(Piece):
    @classmethod
    def get_bishop_moves(cls, position, board):
        moves = []
        x, y = position

        up_left, up_right, down_left, down_right = True, True, True, True
        for i in range(1, 8):
            if up_left:
                try:
                    if board[y-i][x-i] == 'e':
                        moves.append((x-i, y-i))
                    else:
                        up_left = False
                except IndexError:
                    up_left = False
            if up_right:
                try:
                    if board[y-i][x+i] == 'e':
                        moves.append((x+i, y-i))
                    else:
                        up_right = False
                except IndexError:
                    up_right = False
            if down_left:
                try:
                    if board[y+i][x-i] == 'e':
                        moves.append((x-i, y+i))
                    else:
                        down_left = False
                except IndexError:
                    down_left = False
            if down_right:
                try:
                    if board[y+i][x+i] == 'e':
                        moves.append((x+i, y+i))
                    else:
                        down_right = False
                except IndexError:
                    down_right = False

        return moves

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'bishop'
        self.value = 3

    def get_legal_moves(self, board):
        self.legal_moves = Bishop.get_bishop_moves(self.position, board)


class Queen(Rook, Bishop):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'queen'
        self.value = 9

    def get_legal_moves(self, board):
        self.legal_moves = Bishop.get_bishop_moves(self.position, board)
        print(self.legal_moves)


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

        for move in moves[:]:
            x, y = move
            if x < 0 or x > 7 or y < 0 or y > 7:
                moves.remove(move)
                continue

            if board[y][x] == self.color[0]:
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

        for move in moves[:]:
            x, y = move
            if x < 0 or x > 7 or y < 0 or y > 7:
                moves.remove(move)
                continue

            if board[y][x] == self.color[0]:
                moves.remove(move)

        self.legal_moves = moves


class Empty(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'empty'
        self.value = 0

    def get_legal_moves(self):
        return []
