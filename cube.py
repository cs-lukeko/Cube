from constants import SOLVED_CUBE

class Cube:
    def __init__(self, state = None):
        if state is None:
            self.state = SOLVED_CUBE.copy()
        else:
            self.state = state.copy()

    def copy(self):
        return Cube(self.state)

    def is_solved(self):
        return self.state == SOLVED_CUBE

    def __str__(self):
        cube = self.state.copy() # copies cube STATE, not Cube
        for i in range(len(cube)):
            if cube[i] == "W":
                cube[i] = "⬜"
            elif cube[i] == "R":
                cube[i] = "🟥"
            elif cube[i] == "G":
                cube[i] = "🟩"
            elif cube[i] == "Y":
                cube[i] = "🟨"
            elif cube[i] == "O":
                cube[i] = "🟧"
            elif cube[i] == "B":
                cube[i] = "🟦"

        return (
            f"       {cube[0]}{cube[1]}{cube[2]}\n"
            f"       {cube[3]}{cube[4]}{cube[5]}\n"
            f"       {cube[6]}{cube[7]}{cube[8]}\n"
            f"{cube[36]}{cube[37]}{cube[38]} {cube[18]}{cube[19]}{cube[20]} {cube[9]}{cube[10]}{cube[11]} {cube[45]}{cube[46]}{cube[47]}\n"
            f"{cube[39]}{cube[40]}{cube[41]} {cube[21]}{cube[22]}{cube[23]} {cube[12]}{cube[13]}{cube[14]} {cube[48]}{cube[49]}{cube[50]}\n"
            f"{cube[42]}{cube[43]}{cube[44]} {cube[24]}{cube[25]}{cube[26]} {cube[15]}{cube[16]}{cube[17]} {cube[51]}{cube[52]}{cube[53]}\n"
            f"       {cube[27]}{cube[28]}{cube[29]}\n"
            f"       {cube[30]}{cube[31]}{cube[32]}\n"
            f"       {cube[33]}{cube[34]}{cube[35]}"
        )

    def count_oriented_edges(self):
        oriented_edges = 0

        EDGES = [
            [self.state[7], self.state[19]],  # UF
            [self.state[5], self.state[10]],  # UR
            [self.state[1], self.state[46]],  # UB
            [self.state[3], self.state[37]],  # UL
            [self.state[23], self.state[12]], # FR
            [self.state[21], self.state[41]], # FL
            [self.state[48], self.state[14]], # BR
            [self.state[50], self.state[39]], # BL
            [self.state[28], self.state[25]], # DF
            [self.state[32], self.state[16]], # DR
            [self.state[34], self.state[52]], # DB
            [self.state[30], self.state[43]]  # DL
        ]

        for edge in EDGES:
            if self.is_oriented(edge[0], edge[1]):
                oriented_edges += 1

        return oriented_edges

    def is_oriented(self, edge_1: str, edge_2: str):
        if edge_1 == "W" or edge_1 == "Y":
            return True
        elif (edge_1 == "B" or edge_1 == "G") and (edge_2 == "R" or edge_2 == "O"):
            return True
        return False

    def is_eo_solved(self):
        return self.count_oriented_edges() == 12
    
    def is_eo_line_solved(self):
        return self.state[25] == "G" and self.state[28] == "Y" and self.state[52] == "B" and self.state[34] == "Y"

    def is_cross_solved(self):
        return self.state[25] == "G" and self.state[28] == "Y" and self.state[52] == "B" and self.state[34] == "Y" and self.state[16] == "R" and self.state[32] == "Y" and self.state[43] == "O" and self.state[30] == "Y"

    def is_dr_solved(self):
        # check U is correct
        for i in range(9):
            if not (self.state[i] == "Y" or self.state[i] =="W"):
                return False
        # check D is correct
        for i in range(27, 36):
            if not (self.state[i] == "Y" or self.state[i] =="W"):
                return False
        # check middle slice is correct
        if not (self.state[21] == "B" or self.state[21] == "G") and (self.state[23] == "B" or self.state[23] == "G") and (self.state[48] == "B" or self.state[48] == "G") and (self.state[50] == "B" or self.state[50] == "G"):
            return False
        return True