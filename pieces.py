from operator import add, sub
class Piece:

    def __init__(self, name, team, x, y):
        self.name = name
        self.team = team
        self.x = x
        self.y = y

class Bishop(Piece):

    @clsmethod
    def get_diags(x, y):
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
        super().__init(name='Bishop', team, x, y)
        self.legal_moves = Bishop.get_moves(self.x, self.y)

class Rook(Piece):

    @clsmethod
    def get_moves(x, y):
        ops = add, sub
        coords = set()
        for op in ops:
            coord = set()
            for offset in range(8):
                op_x = op(x, offset)
                if (0 <= op_x <= 7):
                    coord.add((op_x, y))
                op_y = op(y, offset)
                if (0 <= op_y <= 7):
                    coord.add((x, op_y))
            coords.add(i) for i in coord

        return sorted(coords)

    def __init__(self, team, x, y):
        super().__init__(name='Rook', team, x, y)
        self.legal_moves = Rook.get_moves(x, y)

class Knight(Piece):

    @clsmethod
    def get_knightmoves(x, y):
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

class Queen(Piece):

    @clsmethod
    def get_queenmoves(x, y):
        return sorted(set(Bishop.get_moves(x, y) + Rook.get_moves(x, y)))


def get_pawnmoves (x, y):
    return (x+1, y)


print(get_pawnmoves(3, 4))
