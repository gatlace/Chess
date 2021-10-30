from operator import add, sub

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

def get_rankfile(x, y):
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
        if (0 <= new_x <= 7 and 0 <= new_y <= 7):
            coords.add((new_x, new_y))

    return sorted(coords)

def get_queenmoves(x, y):
    return sorted(set(get_rankfile(x, y) + get_diags(x, y)))

def get_pawnmoves (x, y):


print(get_queenmoves(3, 4))
