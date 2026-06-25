from moves import apply_moves
from time import perf_counter
from constants import MOVES, AXES, GODS_NUMBER
from pickle import load
from scrambles import reverse_moves, inverse_moves

attempts = 0

def solve_v3(cube: list, look_up_table: int):
    global attempts
    attempts = 0
    solution = None
    start_time = perf_counter()

    filename = f"look_up_tables/database_{look_up_table}_away_from_solved.pkl"

    with open(filename, "rb") as file:
        database = load(file)
    print("Database loaded...")

    for depth in range(1, GODS_NUMBER + 1):
        solution = depth_first_search(cube.copy(), depth, [], database)
        if solution is not None:
            break

    end_time = perf_counter()
    time = end_time - start_time
    return solution, attempts, time

def depth_first_search(cube: list, depth_remaining: int, moves_so_far: list, database):    
    global attempts
    if tuple(cube.state) in database and depth_remaining == 0:
        database_solution = database[tuple(cube.state)]
        return moves_so_far + inverse_moves(reverse_moves(database_solution))

    if depth_remaining == 0:
        return None

    for move in MOVES:
        if len(moves_so_far) >= 1:
            if move[0] == moves_so_far[-1][0]:
                continue

        if len(moves_so_far) >= 2:
            if AXES[move] == AXES[moves_so_far[-1]] and AXES[move] == AXES[moves_so_far[-2]]:
                continue

        attempts += 1
        test_cube = apply_moves(cube.copy(), [move])

        result = depth_first_search(test_cube, depth_remaining - 1, moves_so_far + [move], database)

        if result is not None:
            return result

    return None
        
def print_solve_statistics(attempts, time):
    print()
    print(f"Solutions attempted = {attempts:,}")
    print(f"Time taken: {(time):.3f}s")
    print(f"Rate: {(attempts / time):,.0f} attempts/s")