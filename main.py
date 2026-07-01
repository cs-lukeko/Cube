# from cube import print_cube_state
from moves import *
from scrambles import *
from solver_v1 import SolverV1
from solver_v2 import SolverV2
from solver_v3 import SolverV3
from cube import *

def main():
    # initialise cube
    cube = Cube()

    # pick solver
    # solver = input("Which solver version to be used: ")
    solver_version = "3"

    # scramble cube
    scramble_length = 10

    scramble = generate_random_moves(scramble_length)
    cube = apply_moves(cube, scramble)
    print(cube)
    print(f"Scramble: {" ".join(scramble)}")
    print()

    # solve cube using SolverV1
    if solver_version == "1":
        solver = SolverV1(cube, scramble_length)
        solution, attempts, time = solver.solve(scramble_length)

    # solve cube using SolverV2
    if solver_version == "2":
        solver = SolverV2(cube)
        solution, attempts, time = solver.solve()

    # solve cube using solver_v3
    if solver_version == "3":
        look_up_table = 5
        solver = SolverV3(cube, look_up_table)
        solution, attempts, time = solver.solve()    

    print(f"Solver: {solver.name}")
    cube = apply_moves(cube, solution)
    print(cube)
    print(f"Solution: {" ".join(solution)}")
    solver.print_solve_statistics(attempts, time)

main()