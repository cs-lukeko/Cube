import json
import os
from cube import Cube
from moves import generate_random_moves
from solver_v1 import SolverV1
from solver_v2 import SolverV2
from solver_v3 import SolverV3
from solver_v4 import SolverV4

SOLVERS = [
    SolverV1,
    SolverV2,
    SolverV3,
    SolverV4,
]

RESULTS_FILE = "benchmark_tests/benchmark_test_results.json"


def load_results() -> dict:
    """Read existing results from file. Returns empty dict if file doesn't exist."""
    if not os.path.exists(RESULTS_FILE):
        return {}
    with open(RESULTS_FILE, "r") as file:
        return json.load(file)


def save_results(results: dict):
    """Write all results back to file."""
    os.makedirs("benchmark_tests", exist_ok=True)
    with open(RESULTS_FILE, "w") as file:
        json.dump(results, file, indent=4)


def run_benchmark_test_ao5(solver_version: int, scramble_length: int):
    print(f"\n--- Running benchmark: SolverV{solver_version}, scramble length {scramble_length} ---")

    scrambles = []
    solutions = []
    times = []
    number_of_moves = []
    best_index = 0
    best_single = float("inf")

    # run ao5
    for i in range(5):
        cube = Cube()
        scramble = generate_random_moves(scramble_length)
        scrambles.append(scramble)
        cube.apply_moves(scramble)

        solver = SOLVERS[solver_version - 1](cube, scramble_length=scramble_length)
        solution, attempts, time = solver.solve()

        solutions.append(solution)
        number_of_moves.append(len(solution))
        times.append(time)

        if time < best_single:
            best_single = time
            best_index = i

        print(f"  Solve {i + 1}: {time:.2f}s - Scramble: {' '.join(scramble)} / Solution: {' '.join(solution)}")

    # calculate stats
    sorted_times = sorted(times)
    ao5 = sum(sorted_times[1:4]) / 3
    average_moves = sum(number_of_moves) / len(number_of_moves)
    fewest_moves = min(number_of_moves)

    print(f"Ao5 = {ao5:.2f}s, Best single = {best_single:.2f}s")

    # build result object
    new_result = {
        "solver_version": solver_version,
        "scramble_length": scramble_length,
        "ao5": round(ao5, 3),
        "best_single": round(best_single, 3),
        "average_moves": round(average_moves, 2),
        "fewest_moves": fewest_moves,
        "best_scramble": " ".join(scrambles[best_index]),
        "best_solution": " ".join(solutions[best_index]),
        "all_solves": [
            {
                "scramble": " ".join(scrambles[i]),
                "solution": " ".join(solutions[i]),
                "solution_length": number_of_moves[i],
                "time": round(times[i], 3)
            }
            for i in range(5)
        ]
    }

    # load existing results and compare
    results = load_results()
    key = f"SolverV{solver_version}"

    if key not in results:
        results[key] = new_result
        print(f"First result for {key} — saved.")
    elif new_result["scramble_length"] > results[key]["scramble_length"]:
        print(f"Higher scramble length for {key} ({new_result['scramble_length']} > {results[key]['scramble_length']}) — updated.")
        results[key] = new_result
    elif new_result["scramble_length"] == results[key]["scramble_length"] and new_result["ao5"] < results[key]["ao5"]:
        print(f"New best Ao5 for {key}! {new_result['ao5']:.3f}s beats {results[key]['ao5']:.3f}s — updated.")
        results[key] = new_result
    else:
        print(f"No improvement for {key}. Existing result retained.")

    save_results(results)
    print(f"Results saved to {RESULTS_FILE}")
    update_results_txt_file()


def update_results_txt_file():
    """Display all benchmark results as a formatted txt report."""
    results = load_results()

    if not results:
        print("No benchmark results found.")
        return

    lines = []
    for key, r in results.items():
        lines.append(f"Benchmark test using {key} with scramble of length {r['scramble_length']}.")
        lines.append(f"Ao5: {r['ao5']:.2f}s, Single: {r['best_single']:.2f}s")
        lines.append(f"Average moves: {r['average_moves']:.2f}, Fewest moves: {r['fewest_moves']}")
        lines.append(f"Best single:")
        lines.append(f"    Scramble: {r['best_scramble']}")
        lines.append(f"    Solution: {r['best_solution']}")
        lines.append("")

    report = "\n".join(lines)

    report_file = "benchmark_tests/benchmark_test_results.txt"
    os.makedirs("benchmark_tests", exist_ok=True)
    with open(report_file, "w") as file:
        file.write(report)
    print(f"Report saved to {report_file}")


# run tests (solver_version, scramble_length)
# run_benchmark_test_ao5(1, 5)
# run_benchmark_test_ao5(2, 5)
# run_benchmark_test_ao5(3, 11)
run_benchmark_test_ao5(4, 20)