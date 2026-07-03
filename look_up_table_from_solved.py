# Generates file with cube states n moves away from solved
from constants import DR_MOVESET, FULL_MOVESET, AXES, EO_MOVESET
from cube import Cube
from pickle import dump
from moves import apply_moves

# change these variables
set = EO_MOVESET
n = 6

def generate_look_up_table_to_solved(n: int):
    database = {}
    depth_first_search(Cube(), n, [], database)

    set_str = ""
    if set == FULL_MOVESET:
        set_str = ""
    elif set == EO_MOVESET:
        set_str = "_eo"
    elif set == DR_MOVESET:
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

    for move in set:
        if len(moves_so_far) >= 1:
            if move[0] == moves_so_far[-1][0]:
                continue

        if len(moves_so_far) >= 2:
            if AXES[move] == AXES[moves_so_far[-1]] and AXES[move] == AXES[moves_so_far[-2]]:
                continue

        next_cube = apply_moves(cube, [move])

        depth_first_search(next_cube, depth_remaining - 1, moves_so_far + [move], database)

for i in range(1, n + 1):
    generate_look_up_table_to_solved(i)