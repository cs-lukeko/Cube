from cube import is_solved
from moves import generate_random_moves, apply_moves
from time import perf_counter
from constants import SOLVED_CUBE

# Brute forces 6 random moves until it finds the solution. Takes a long time for any scrambles longer than 6 moves
def solve_v1(cube, scramble_length):
    solution = ""
    attempts = 0
    start_time = perf_counter()
    while cube != SOLVED_CUBE:
        solution = generate_random_moves(scramble_length)
        test_cube = apply_moves(cube.copy(), solution)
        attempts += 1
        if is_solved(test_cube):
            end_time = perf_counter()
            break

    time = end_time - start_time

    return solution, attempts, time

def print_solve_statistics(attempts, time):
    print()
    print(f"Solutions attempted = {attempts:,}")
    print(f"Time taken: {(time):.3f}s")