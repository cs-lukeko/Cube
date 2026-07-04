# Generates file with cube states n moves away from solved
from constants import DR_MOVESET, FULL_MOVESET, AXES, EO_MOVESET
from cube import Cube
from pickle import dump

# change these variables
moveset = EO_MOVESET
n = 6

def generate_look_up_table_to_solved(n: int):
    database = {}
    depth_first_search(Cube(), n, [], database)

    set_str = ""
    if moveset == FULL_MOVESET:
        set_str = ""
    elif moveset == EO_MOVESET:
        set_str = "_eo"
    elif moveset == DR_MOVESET:
        set_str = "_dr"

    with open(f"look_up_tables/database_{n}_moves{set_str}_to_solved.pkl", "wb") as file:
        dump(database, file)

    print(f"Look-up table {n} complete. {len(database):,} states generated")

    return database    
    
def depth_first_search(cube, depth_remaining, moves_so_far, database):
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

        cube.apply_moves([move])

        depth_first_search(cube, depth_remaining - 1, moves_so_far + [move], database)

for i in range(1, n + 1):
    generate_look_up_table_to_solved(i)