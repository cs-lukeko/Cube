from random import choice
from constants import AXES, FULL_MOVESET

def print_moves(moves: list):
    moves_string = " ".join(moves)
    print(moves_string)

def generate_random_moves(length: int):
    moves = []
    while len(moves) < length:
        move = choice(FULL_MOVESET)

        if len(moves) >= 1:
            if move[0] == moves[-1][0]:
                continue

        if len(moves) >= 2:
            if AXES[move] == AXES[moves[-1]] and AXES[move] == AXES[moves[-2]]:
                continue

        moves.append(move)

    return moves

def u(old_state):
    new_state = old_state.copy()

    temp = [old_state[18], old_state[19], old_state[20]]

    new_state[18] = old_state[9]
    new_state[19] = old_state[10]
    new_state[20] = old_state[11]

    new_state[9] = old_state[45]
    new_state[10] = old_state[46]
    new_state[11] = old_state[47]

    new_state[45] = old_state[36]
    new_state[46] = old_state[37]
    new_state[47] = old_state[38]

    new_state[36] = temp[0]
    new_state[37] = temp[1]
    new_state[38] = temp[2]

    new_state[0] = old_state[6]
    new_state[1] = old_state[3]
    new_state[2] = old_state[0]

    new_state[3] = old_state[7]
    new_state[5] = old_state[1]

    new_state[6] = old_state[8]
    new_state[7] = old_state[5]
    new_state[8] = old_state[2]

    return new_state

def r(old_state):
    new_state = old_state.copy()

    temp = [new_state[2], new_state[5], new_state[8]]

    new_state[2] = old_state[20]
    new_state[5] = old_state[23]
    new_state[8] = old_state[26]

    new_state[20] = old_state[29]
    new_state[23] = old_state[32]
    new_state[26] = old_state[35]

    new_state[29] = old_state[51]
    new_state[32] = old_state[48]
    new_state[35] = old_state[45]

    new_state[51] = temp[0]
    new_state[48] = temp[1]
    new_state[45] = temp[2]

    new_state[9] = old_state[15]
    new_state[10] = old_state[12]
    new_state[11] = old_state[9]

    new_state[12] = old_state[16]
    new_state[14] = old_state[10]

    new_state[15] = old_state[17]
    new_state[16] = old_state[14]
    new_state[17] = old_state[11]
    return new_state

def f(old_state):
    new_state = old_state.copy()

    temp = [new_state[29], new_state[28], new_state[27]]

    new_state[6] = old_state[44]
    new_state[7] = old_state[41]
    new_state[8] = old_state[38]

    new_state[9] = old_state[6]
    new_state[12] = old_state[7]
    new_state[15] = old_state[8]

    new_state[29] = old_state[9]
    new_state[28] = old_state[12]
    new_state[27] = old_state[15]

    new_state[44] = temp[0]
    new_state[41] = temp[1]
    new_state[38] = temp[2]

    new_state[18] = old_state[24]
    new_state[19] = old_state[21]
    new_state[20] = old_state[18]

    new_state[21] = old_state[25]
    new_state[23] = old_state[19]

    new_state[24] = old_state[26]
    new_state[25] = old_state[23]
    new_state[26] = old_state[20]

    return new_state

def d(old_state):
    new_state = old_state.copy()

    temp = [old_state[51], old_state[52], old_state[53]]

    new_state[24] = old_state[42]
    new_state[25] = old_state[43]
    new_state[26] = old_state[44]

    new_state[15] = old_state[24]
    new_state[16] = old_state[25]
    new_state[17] = old_state[26]

    new_state[51] = old_state[15]
    new_state[52] = old_state[16]
    new_state[53] = old_state[17]

    new_state[42] = temp[0]
    new_state[43] = temp[1]
    new_state[44] = temp[2]

    new_state[27] = old_state[33]
    new_state[28] = old_state[30]
    new_state[29] = old_state[27]

    new_state[30] = old_state[34]
    new_state[32] = old_state[28]

    new_state[33] = old_state[35]
    new_state[34] = old_state[32]
    new_state[35] = old_state[29]

    return new_state

def l(old_state):
    new_state = old_state.copy()

    temp = [new_state[27], new_state[30], new_state[33]]

    new_state[0] = old_state[53]
    new_state[3] = old_state[50]
    new_state[6] = old_state[47]

    new_state[18] = old_state[0]
    new_state[21] = old_state[3]
    new_state[24] = old_state[6]

    new_state[27] = old_state[18]
    new_state[30] = old_state[21]
    new_state[33] = old_state[24]

    new_state[53] = temp[0]
    new_state[50] = temp[1]
    new_state[47] = temp[2]

    new_state[36] = old_state[42]
    new_state[37] = old_state[39]
    new_state[38] = old_state[36]

    new_state[39] = old_state[43]
    new_state[41] = old_state[37]

    new_state[42] = old_state[44]
    new_state[43] = old_state[41]
    new_state[44] = old_state[38]

    return new_state

def b(old_state):
    new_state = old_state.copy()

    temp = [new_state[33], new_state[34], new_state[35]]

    new_state[2] = old_state[17]
    new_state[1] = old_state[14]
    new_state[0] = old_state[11]

    new_state[36] = old_state[2]
    new_state[39] = old_state[1]
    new_state[42] = old_state[0]

    new_state[33] = old_state[36]
    new_state[34] = old_state[39]
    new_state[35] = old_state[42]

    new_state[17] = temp[0]
    new_state[14] = temp[1]
    new_state[11] = temp[2]

    new_state[45] = old_state[51]
    new_state[46] = old_state[48]
    new_state[47] = old_state[45]

    new_state[48] = old_state[52]
    new_state[50] = old_state[46]

    new_state[51] = old_state[53]
    new_state[52] = old_state[50]
    new_state[53] = old_state[47]

    return new_state

def r_prime(old_state):
    return r(r(r(old_state)))

def r2(old_state):
    return r(r(old_state))

def l_prime(old_state):
    return l(l(l(old_state)))

def l2(old_state):
    return l(l(old_state))

def u_prime(old_state):
    return u(u(u(old_state)))

def u2(old_state):
    return u(u(old_state))
             
def d_prime(old_state):
    return d(d(d(old_state)))

def d2(old_state):
    return d(d(old_state))

def f_prime(old_state):
    return f(f(f(old_state)))

def f2(old_state):
    return f(f(old_state))

def b_prime(old_state):
    return b(b(b(old_state)))
             
def b2(old_state):
    return b(b(old_state))

MOVE_FUNCTIONS = {
    "U": u,
    "U'": u_prime,
    "U2": u2,
    "D": d,
    "D'": d_prime,
    "D2": d2,
    "R": r,
    "R'": r_prime,
    "R2": r2,
    "L": l,
    "L'": l_prime,
    "L2": l2,
    "F": f,
    "F'": f_prime,
    "F2": f2,
    "B": b,
    "B'": b_prime,
    "B2": b2
}