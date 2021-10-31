from operator import add, sub
class Piece:

    def __init__(self, team, x, y, name):
        self.name = name
        self.team = team
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.team} {self.name} on [{self.x}, {self.y}]'

    def __eq__(self, other):
        return (self.value == self.value)

    def __add__(self, other):
        return self.value + other.value

class Bishop(Piece):

    @classmethod
    def get_diags(cls, x, y):
        ops = [
                (add, add), (sub, sub),
                (add, sub), (sub, add)
                ]

        diags = set()
        for op in ops:
            for offset in range(8):
                for op_x, op_y in ops:
                    diag_x = op_x(x, offset)
                    diag_y = op_y(y, offset)
                    if (
                            (0 <= diag_x <= 7 and 0 <= diag_y <= 7) and
                            (diag_x != x and diag_y != y)
                        ):
                        diags.add((diag_x, diag_y))

        return sorted(diags)

    def __init__(self, team, x, y):
        super().__init(team, x, y, name='Bishop')
        self.legal_moves = Bishop.get_moves(self.x, self.y)
        self.value = 3

class Rook(Piece):

    @classmethod
    def get_moves(cls, x, y):
        ops = add, sub
        coords = set()
        for op in ops:
            for offset in range(8):
                op_x = op(x, offset)
                if (0 <= op_x <= 7):
                    coords.add((op_x, y))
                op_y = op(y, offset)
                if (0 <= op_y <= 7):
                    coords.add((x, op_y))

        return sorted(coords)

    def __init__(self, team, x, y):
        super().__init__(team, x, y, name='Rook')
        self.legal_moves = Rook.get_moves(self.x, self.y)
        self.value = 5

class Knight(Piece):

    @classmethod
    def get_moves(cls, x, y):
        ops = [
                ((add, 2), (add, 1)), ((add, 2), (sub, 1)),
                ((sub, 2), (add, 1)), ((sub, 2), (sub, 1)),
                ((add, 1), (add, 2)), ((add, 1), (sub, 2)),
                ((sub, 1), (add, 2)), ((sub, 1), (sub, 2))
               ]

        coords = set()
        for x_chg, y_chg in ops:
            new_x = x_chg[0](x, x_chg[1])
            new_y = y_chg[0](y, y_chg[1])
            if (
                    (0 <= new_x <= 7 and 0 <= new_y <= 7) and
                    (new_x != x and neww_y != y)
                ):
                coords.add((new_x, new_y))

        return sorted(coords)

    def __init__(self, team, x, y):
        super().__init__(team, x, y, name='Knight')
        self.legal_moves = Knight.get_moves(self.x, self.y)
        self.value = 3

class Queen(Piece):

    @classmethod
    def get_moves(cls, x, y):
        return sorted(set(Bishop.get_moves(x, y) + Rook.get_moves(x, y)))

    def __init__(self, team, x, y):
        super().__init__(team, x, y, name='Queen')
        self.legal_moves = Queen.get_moves(self.x, self.y)
        self.value = 9

class Pawn(Piece):

    @classmethod
    def get_moves(cls, x, y):
        coords = set()
        if y+1 <= 7:
            coords.add((x, y+1))
        if x+1 <= 7:
            coords.add((x+1, y+1))
        if x-1 <= 7:
            coords.add((x-1, y+1))

    def __init__(self, team, x, y):
        super().__init__(team, x, y, name='Pawn')
        self.legal_moves = Pawn.get_moves(self.x, self.y)
        self.value = 1
