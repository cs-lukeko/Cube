# from cube import print_cube_state
from moves import generate_random_moves
from solver_v1 import SolverV1
from solver_v2 import SolverV2
from solver_v3 import SolverV3
from solver_v4 import SolverV4
from solver_v5 import SolverV5
from cube import Cube

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

    # solve cube using SolverV1
    if solver_version == "1":
        solver = SolverV1(cube)
        if scramble_length > solver.max_scramble_length:
            print("Scramble is too complex for this solver. Reduce scramble length or change solver.")
            return
        else:
            solution, attempts, time = solver.solve()

    # solve cube using SolverV2
    if solver_version == "2":
        solver = SolverV2(cube)
        if scramble_length > solver.max_scramble_length:
            print("Scramble is too complex for this solver. Reduce scramble length or change solver.")
            return
        else:
            solution, attempts, time = solver.solve()

    # solve cube using SolverV3
    if solver_version == "3":
        solver = SolverV3(cube)
        if scramble_length > solver.max_scramble_length:
            print("Scramble is too complex for this solver. Reduce scramble length or change solver.")
            return
        else:
            solution, attempts, time = solver.solve()

    # solve cube using SolverV4
    if solver_version == "4":
        solver = SolverV4(cube)
        if scramble_length > solver.max_scramble_length:
            print("Scramble is too complex for this solver. Reduce scramble length or change solver.")
            return
        else:
            solution, attempts, time = solver.solve()

    # solve cube using SolverV5
    if solver_version == "5":
        solver = SolverV5(cube)
        if scramble_length > solver.max_scramble_length:
            print("Scramble is too complex for this solver. Reduce scramble length or change solver.")
            return
        else:
            solution, attempts, time = solver.solve()

    print(f"Solver: {solver.name}")
    cube.apply_moves(solution)
    print(cube)
    print(f"Solution ({len(solution)} moves): {" ".join(solution)}")
    solver.print_solve_statistics(attempts, time)

main()