# from cube import print_cube_state
from moves import generate_random_moves
from solver_v1 import SolverV1
from solver_v2 import SolverV2
from solver_v3 import SolverV3
from solver_v4 import SolverV4
from solver_v5 import SolverV5
from cube import Cube

SOLVERS = {
    "1": SolverV1,
    "2": SolverV2,
    "3": SolverV3,
    "4": SolverV4,
    "5": SolverV5
}

def main():
    # initialise cube
    cube = Cube()

    # pick solver
    # solver_version = input("Which solver version to be used: ")
    solver_version = "5"

    # scramble cube
    scramble_length = 20

    scramble = generate_random_moves(scramble_length)
    cube.apply_moves(scramble)
    print(cube)
    print(f"Scramble: {" ".join(scramble)}")
    print()

    solver = SOLVERS[solver_version](cube)
    if scramble_length > solver.max_scramble_length:
        print("Scramble is too complex for this solver. Reduce scramble length or change solver.")
        return
    solution, attempts, time = solver.solve()

    print(f"Solver: {solver.name}")
    cube.apply_moves(solution)
    print(cube)
    print(f"Solution ({len(solution)} moves): {" ".join(solution)}")
    solver.print_solve_statistics(attempts, time)

main()