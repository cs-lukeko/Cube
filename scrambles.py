def inverse_moves(moves: list):
    inversed_moves = []
    for move in moves:
        if len(move) == 1:
            inversed_moves.append(move + "'")
        elif move[1] == "'":
            inversed_moves.append(move[0])
        else:
            inversed_moves.append(move)
    return inversed_moves

def reverse_moves(moves: list):
    reversed_moves = moves[::-1]
    return reversed_moves