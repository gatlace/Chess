class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.position = (x, y)
        self.legal_moves = self.get_legal_moves()

    def __str__(self):
        return self.color + ' ' + self.__class__.__name__


class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'pawn'
        self.value = 1

    def get_legal_moves(self, board):
        moves = []
        x, y = self.position
        if self.color == 'black':
            if y != 6:
                moves.extend([(x, y+1)])
            else:
                moves.extend([(x, y+1), (x, y+2)]),
        elif self.color == 'white':
            if y != 1:
                moves.extend([(x, y + 1)])
            else:
                moves.extend([(x, y + 1),
                             (x, y + 2)])

        self.legal_moves = moves

    def get_capture_moves(self):
        moves = []
        x, y = self.position
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
        x, y = self.position
        moves = [(x, i) for i in range(8)]
        moves.extend([(i, y) for i in range(8)])

        self.legal_moves = moves


class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'bishop'
        self.value = 3

    def get_legal_moves(self, board):
        x, y = self.position
        moves = []

        up_left, up_right, down_left, down_right = False, False, False, False
        for i in range(1, 8):
            if up_left is True:
                if x - i > -1 and y - i > -1:
                    if board[x - i][y - i].color == self.color:
                        up_left = False
                    else:
                        moves.append((x - i, y - i))
            if up_right is True:
                if x + i < 8 and y - i > -1:
                    if board[x + i][y - i].color == self.color:
                        up_right = False
                    else:
                        moves.append((x + i, y - i))
            if down_left is True:
                if x - i > -1 and y + i < 8:
                    if board[x - i][y + i].color == self.color:
                        down_left = False
                    else:
                        moves.append((x - i, y + i))
            if down_right is True:
                if x + i < 8 and y + i < 8:
                    if board[x + i][y + i].color == self.color:
                        down_right = False
                    else:
                        moves.append((x + i, y + i))

        return moves


class Queen(Rook, Bishop):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'queen'
        self.value = 9

    def get_legal_moves(self):
        return Rook.get_legal_moves(self).extend(Bishop.get_legal_moves(self))


class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'knight'
        self.value = 3

    def get_legal_moves(self):
        x, y = self.position
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

        return moves


class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'king'
        self.value = 100

    def get_legal_moves(self):
        x, y = self.position
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

        return moves


class Empty(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.type = 'empty'
        self.value = 0

    def get_legal_moves(self):
        return []


bishop = Bishop('white', 4, 5)
