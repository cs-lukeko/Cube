# Generates file with cube states n moves away from solved
from constants import AXES, EO_MOVESET, DR_MOVESET, FULL_MOVESET
from cube import Cube
from pickle import dump

def generate_look_up_table_to_solved(n: int, moveset):
    database = {}
    depth_first_search(Cube(), n, [], database, moveset)

    set_str = ""
    if moveset == FULL_MOVESET:
        set_str = "_full"
    elif moveset == EO_MOVESET:
        set_str = "_eo"
    elif moveset == DR_MOVESET:
        set_str = "_dr"

    with open(f"look_up_tables/database_{n}_moves{set_str}_to_solved.pkl", "wb") as file:
        dump(database, file)

    print(f"Look-up table {n} ({set_str[1:].upper()}) complete. {len(database):,} states generated")

    return database    
    
def depth_first_search(cube, depth_remaining, moves_so_far, database, moveset):
    key = tuple(cube.state)
    
    if key not in database:
        database[key] = moves_so_far

    if depth_remaining == 0:
        return None

    for move in moveset:
        if len(moves_so_far) >= 1:
            if move[0] == moves_so_far[-1][0]:
                continue

        if len(moves_so_far) >= 2:
            if AXES[move] == AXES[moves_so_far[-1]] and AXES[move] == AXES[moves_so_far[-2]]:
                continue

        next_cube = cube.copy()
        next_cube.apply_moves([move])

        depth_first_search(next_cube, depth_remaining - 1, moves_so_far + [move], database, moveset)

n = 6
for i in range(3, n + 1):
    generate_look_up_table_to_solved(i, FULL_MOVESET)
