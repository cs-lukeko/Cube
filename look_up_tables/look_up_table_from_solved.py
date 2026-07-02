# Generates file with cube states n moves away from solved
from constants import MOVES, AXES, EO_MOVESET
from cube import Cube
from pickle import dump
from moves import apply_moves

def generate_look_up_table(n: int):
    database = {}
    depth_first_search(Cube(), n, [], database)

    with open(f"look_up_tables/database_{n}_away_from_solved_eo.pkl", "wb") as file:
        dump(database, file)

    print(f"{len(database):,} states generated")

    return database    
    
def depth_first_search(cube, depth_remaining, moves_so_far, database):
    key = tuple(cube.state)
    
    if key not in database:
        database[key] = moves_so_far

    if depth_remaining == 0:
        return None

    for move in EO_MOVESET:
        if len(moves_so_far) >= 1:
            if move[0] == moves_so_far[-1][0]:
                continue

        if len(moves_so_far) >= 2:
            if AXES[move] == AXES[moves_so_far[-1]] and AXES[move] == AXES[moves_so_far[-2]]:
                continue

        next_cube = apply_moves(cube, [move])

        depth_first_search(next_cube, depth_remaining - 1, moves_so_far + [move], database)

generate_look_up_table(8)
