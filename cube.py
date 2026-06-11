solved_cube = [
    "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜",
    "🟧", "🟧", "🟧", "🟧", "🟧", "🟧", "🟧", "🟧", "🟧", 
    "🟩", "🟩", "🟩", "🟩", "🟩", "🟩", "🟩", "🟩", "🟩", 
    "🟥", "🟥", "🟥", "🟥", "🟥", "🟥", "🟥", "🟥", "🟥", 
    "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", 
    "🟨", "🟨", "🟨", "🟨", "🟨", "🟨", "🟨", "🟨", "🟨"
    ]

def cube():
    print(solved_cube)

def is_solved(cube):
    if cube == solved_cube:
        return True
    return False

def print_cube_state(cube):
    print(f"       {cube[0]}{cube[1]}{cube[2]}")
    print(f"       {cube[3]}{cube[4]}{cube[5]}")
    print(f"       {cube[6]}{cube[7]}{cube[8]}")

    print(f"{cube[9]}{cube[10]}{cube[11]} {cube[18]}{cube[19]}{cube[20]} {cube[27]}{cube[28]}{cube[29]} {cube[36]}{cube[37]}{cube[38]}")
    print(f"{cube[12]}{cube[13]}{cube[14]} {cube[21]}{cube[22]}{cube[23]} {cube[30]}{cube[31]}{cube[32]} {cube[39]}{cube[40]}{cube[41]}")
    print(f"{cube[15]}{cube[16]}{cube[17]} {cube[24]}{cube[25]}{cube[26]} {cube[33]}{cube[34]}{cube[35]} {cube[42]}{cube[43]}{cube[44]}")

    print(f"       {cube[45]}{cube[46]}{cube[47]}")
    print(f"       {cube[48]}{cube[49]}{cube[50]}")
    print(f"       {cube[51]}{cube[52]}{cube[53]}")

