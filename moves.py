import random

def print_moves(moves: list):
    moves_string = " ".join(moves)
    print(moves_string)

def generate_random_moves(length: int):
    possible_moves = ["U", "D", "F", "B", "R", "L"]
    possible_modifications = ["", "'", "2"]
    axes = {
        "F": "FB",
        "B": "FB",
        "U": "UD",
        "D": "UD",
        "R": "RL",
        "L": "RL"
    }
    moves = []
    while len(moves) < length:
        move = random.choice(possible_moves)

        if len(moves) >= 1:
            if move == moves[-1]:
                continue

        if len(moves) >= 2:
            if axes[move] == axes[moves[-1]] and axes[move] == axes[moves[-2]]:
                continue

        moves.append(move)

    for i in range(len(moves)):
        moves[i] += random.choice(possible_modifications)

    return moves

def apply_moves(old_state, moves_list):
    new_state = old_state.copy()
    for move in moves_list:
        if move == "U":
            new_state = u(new_state)
        elif move == "U'":
            new_state = u(u(u(new_state)))
        elif move == "U2":
            new_state = u(u(new_state))
        elif move == "D":
            new_state = d(new_state)
        elif move == "D'":
            new_state = d(d(d(new_state)))
        elif move == "D2":
            new_state = d(d(new_state))
        elif move == "R":
            new_state = r(new_state)
        elif move == "R'":
            new_state = r(r(r(new_state)))
        elif move == "R2":
            new_state = r(r(new_state))
        elif move == "L":
            new_state = l(new_state)
        elif move == "L'":
            new_state = l(l(l(new_state)))
        elif move == "L2":
            new_state = l(l(new_state))
        elif move == "F":
            new_state = f(new_state)
        elif move == "F'":
            new_state = f(f(f(new_state)))
        elif move == "F2":
            new_state = f(f(new_state))
        elif move == "B":
            new_state = b(new_state)
        elif move == "B'":
            new_state = b(b(b(new_state)))
        elif move == "B2":
            new_state = b(b(new_state))
    return new_state

def r(old_state):
    new_state = old_state.copy()

    temp = [new_state[2], new_state[5], new_state[8]]

    new_state[2] = old_state[20]
    new_state[5] = old_state[23]
    new_state[8] = old_state[26]

    new_state[20] = old_state[47]
    new_state[23] = old_state[50]
    new_state[26] = old_state[53]

    new_state[47] = old_state[42]
    new_state[50] = old_state[39]
    new_state[53] = old_state[36]

    new_state[42] = temp[0]
    new_state[39] = temp[1]
    new_state[36] = temp[2]

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

    temp = [new_state[0], new_state[3], new_state[6]]

    new_state[0] = old_state[44]
    new_state[3] = old_state[41]
    new_state[6] = old_state[38]

    new_state[44] = old_state[45]
    new_state[41] = old_state[48]
    new_state[38] = old_state[51]

    new_state[45] = old_state[18]
    new_state[48] = old_state[21]
    new_state[51] = old_state[24]

    new_state[18] = temp[0]
    new_state[21] = temp[1]
    new_state[24] = temp[2]

    new_state[9] = old_state[15]
    new_state[10] = old_state[12]
    new_state[11] = old_state[9]

    new_state[12] = old_state[16]
    new_state[14] = old_state[10]

    new_state[15] = old_state[17]
    new_state[16] = old_state[14]
    new_state[17] = old_state[11]

    return new_state

def u(old_state):
    new_state = old_state.copy()

    temp = [old_state[18], old_state[19], old_state[20]]

    new_state[18] = old_state[27]
    new_state[19] = old_state[28]
    new_state[20] = old_state[29]

    new_state[27] = old_state[36]
    new_state[28] = old_state[37]
    new_state[29] = old_state[38]

    new_state[36] = old_state[9]
    new_state[37] = old_state[10]
    new_state[38] = old_state[11]

    new_state[9] = temp[0]
    new_state[10] = temp[1]
    new_state[11] = temp[2]

    new_state[0] = old_state[6]
    new_state[1] = old_state[3]
    new_state[2] = old_state[0]

    new_state[3] = old_state[7]
    new_state[5] = old_state[1]

    new_state[6] = old_state[8]
    new_state[7] = old_state[5]
    new_state[8] = old_state[2]

    return new_state

def d(old_state):
    new_state = old_state.copy()

    temp = [old_state[42], old_state[43], old_state[44]]

    new_state[24] = old_state[15]
    new_state[25] = old_state[16]
    new_state[26] = old_state[17]

    new_state[33] = old_state[24]
    new_state[34] = old_state[25]
    new_state[35] = old_state[26]

    new_state[42] = old_state[33]
    new_state[43] = old_state[34]
    new_state[44] = old_state[35]

    new_state[15] = temp[0]
    new_state[16] = temp[1]
    new_state[17] = temp[2]

    new_state[45] = old_state[51]
    new_state[46] = old_state[48]
    new_state[47] = old_state[45]

    new_state[48] = old_state[52]
    new_state[50] = old_state[46]

    new_state[51] = old_state[53]
    new_state[52] = old_state[50]
    new_state[53] = old_state[47]

    return new_state

def f(old_state):
    new_state = old_state.copy()

    temp = [new_state[6], new_state[7], new_state[8]]

    new_state[6] = old_state[17]
    new_state[7] = old_state[14]
    new_state[8] = old_state[11]

    new_state[17] = old_state[47]
    new_state[14] = old_state[46]
    new_state[11] = old_state[45]

    new_state[47] = old_state[27]
    new_state[46] = old_state[30]
    new_state[45] = old_state[33]

    new_state[27] = temp[0]
    new_state[30] = temp[1]
    new_state[33] = temp[2]

    new_state[18] = old_state[24]
    new_state[19] = old_state[21]
    new_state[20] = old_state[18]

    new_state[21] = old_state[25]
    new_state[23] = old_state[19]

    new_state[24] = old_state[26]
    new_state[25] = old_state[23]
    new_state[26] = old_state[20]

    return new_state

def b(old_state):
    new_state = old_state.copy()

    temp = [new_state[0], new_state[1], new_state[2]]

    new_state[0] = old_state[29]
    new_state[1] = old_state[32]
    new_state[2] = old_state[35]

    new_state[29] = old_state[53]
    new_state[32] = old_state[52]
    new_state[35] = old_state[51]

    new_state[53] = old_state[15]
    new_state[52] = old_state[12]
    new_state[51] = old_state[9]

    new_state[15] = temp[0]
    new_state[12] = temp[1]
    new_state[9] = temp[2]

    new_state[36] = old_state[42]
    new_state[37] = old_state[39]
    new_state[38] = old_state[36]

    new_state[39] = old_state[43]
    new_state[41] = old_state[37]

    new_state[42] = old_state[44]
    new_state[43] = old_state[41]
    new_state[44] = old_state[38]

    return new_state