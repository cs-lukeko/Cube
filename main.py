# from cube import print_cube_state
from cube import Cube
from moves import generate_random_moves
from solver_v1 import SolverV1
from solver_v2 import SolverV2
from solver_v3 import SolverV3
from solver_v4 import SolverV4
from solver_v5 import SolverV5

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
    solver_version = "5"

    # scramble cube
    scramble_length = 20
    scramble = generate_random_moves(scramble_length)
    cube.apply_moves(scramble)
    scrambled_cube = cube.copy()
    print("Random cube generated.")
    
    # solve cube
    solver = SOLVERS[solver_version](cube)
    print(f"Solving using SolverV{solver_version} ({solver.name})...")
    if scramble_length > solver.max_scramble_length:
        print("Scramble is too complex for this solver. Reduce scramble length or change solver.")
        return
    solution, attempts, time = solver.solve()

    # show cube "animation"
    solver.animate(scrambled_cube)

    # final solution stats
    print(f"Solver: {solver.name}\n")
    print(f"Scramble: {" ".join(scramble)}")
    print(f"Solution ({len(solution)} moves): {" ".join(solution)}")
    solver.print_solve_statistics(attempts, time)
    solver.reconstruction()

main()