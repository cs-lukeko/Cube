from moves import apply_moves
from time import perf_counter
from constants import MOVES, AXES, GODS_NUMBER
from pickle import load
from scrambles import reverse_moves, inverse_moves

attempts = 0

def solve_v3(cube: list):
    global attempts
    attempts = 0
    solution = None
    start_time = perf_counter()

    with open("look_up_tables/database_6_away_from_solved.pkl", "rb") as file:
        database = load(file)

    for depth in range(1, GODS_NUMBER + 1):
        solution = depth_first_search(cube.copy(), depth, [], database)
        if solution is not None:
            break

    end_time = perf_counter()
    time = end_time - start_time
    print(attempts)
    return solution, attempts, time

def depth_first_search(cube: list, depth_remaining: int, moves_so_far: list, database):    
    global attempts
    if tuple(cube) in database:
        database_solution = database[tuple(cube)]
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