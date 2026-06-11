from cube import is_solved
from moves import apply_moves
from time import perf_counter
from constants import MOVES

attempts = 0

# Uses iteratively deepening depth-first search to find the solution in a systematic way rather than random selection of moves. Still takes a long time for scrambles of length 6 or greater.
# Iterative Deepening (ID) = for each loop completed, the depth of search increases by 1
# Depth-First Search (DFS) = explores the length of a branch before moving to the next - opposite of Breadth-First Search (BFS)
def solve_v2(cube: list, max_depth: int):
    total_attempts = 0
    solution = []
    start_time = perf_counter()

    for depth in range(1, max_depth + 1):
        solution, depth_attempts = depth_first_search(cube.copy(), depth, [])
        total_attempts += depth_attempts
        if solution is not None:
            break

    end_time = perf_counter()
    time = end_time - start_time

    return solution, total_attempts, time

def depth_first_search(cube: list, depth_remaining: int, moves_so_far: list):
    if is_solved(cube):
        return moves_so_far, 0

    if depth_remaining == 0:
        return None, 0

    attempts = 0
    for move in MOVES:
        attempts += 1
        test_cube = apply_moves(cube.copy(), [move])

        result, child_attempts = depth_first_search(test_cube, depth_remaining - 1, moves_so_far + [move])
        attempts += child_attempts

        if result is not None:
            return result, attempts

    return None, attempts
        
def print_solve_statistics(attempts, time):
    print()
    print(f"Solutions attempted = {attempts:,}")
    print(f"Time taken: {(time):.3f}s")
    print(f"Rate: {(attempts / time):,.0f} attempts/s")