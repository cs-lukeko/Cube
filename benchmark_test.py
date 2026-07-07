from cube import Cube
from moves import generate_random_moves
from solver_v1 import SolverV1
from solver_v2 import SolverV2
from solver_v3 import SolverV3
from solver_v4 import SolverV4
from solver_v5 import SolverV5

SOLVERS = [
    SolverV1,
    SolverV2,
    SolverV3,
    SolverV4,
    SolverV5
]

def run_benchmark_test_ao5(solver_version: int, scramble_length: int):
    scrambles = []
    solutions = []
    times = []
    number_of_moves = []
    best_index = 0
    best_single = float("inf")

    # run ao5 for given solver and scramble length
    for i in range(5):
        cube = Cube()
        scramble = generate_random_moves(scramble_length)
        scrambles.append(scramble)
        cube.apply_moves(scramble)
        solver = SOLVERS[solver_version - 1](cube, scramble_length = scramble_length)
        solution, attempts, time = solver.solve()
        solutions.append(solution)
        number_of_moves.append(len(solution))
        times.append(time)
        if time < best_single:
            best_single = time
            best_index = i
        print(f"{time:.2f}s - Scramble: {" ".join(scramble)} / Solution: {" ".join(solution)}")

    # truncate
    times.sort()
    ao5 = sum(times[1:4]) / 3
    print(f"Ao5 = {ao5:.2f}s")

    # moves stats
    average_moves = sum(number_of_moves) / len(number_of_moves)
    number_of_moves.sort()
    fewest_moves = number_of_moves[0]

    # best solution
    best_scramble = scrambles[best_index]
    best_solution = solutions[best_index]

    result_str = (
        f"Benchmark test using SolverV{solver_version} with scramble of length {scramble_length}.\n"
        f"Ao5: {ao5:.2f}s, Single: {best_single:.2f}s\n"
        f"Average moves: {average_moves:.2f}, Fewest moves: {fewest_moves}\n"
        f"Best single:\n"
        f"    Scramble: {" ".join(best_scramble)}\n"
        f"    Solution: {" ".join(best_solution)}\n\n"
    )

    with open("benchmark_tests/benchmark_test_results.txt", "a") as file:
        file.write(f"{result_str}")
        print(f"Result saved to {file.name}\n")

# run tests (solver_version, scramble_length)
run_benchmark_test_ao5(1, 5)
run_benchmark_test_ao5(2, 5)
run_benchmark_test_ao5(3, 12)
run_benchmark_test_ao5(4, 20)