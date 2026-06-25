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
