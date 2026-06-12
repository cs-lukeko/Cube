from cube import print_cube_state
from moves import *
from scrambles import *
from solver_v1 import solve_v1
from solver_v2 import solve_v2, print_solve_statistics
from constants import SOLVED_CUBE

def main():
    # initialise cube
    cube = SOLVED_CUBE

    # pick solver
    solver = input("Which solver version to be used: ")

    # scramble cube
    scramble_length = 5
    scramble = generate_random_moves(scramble_length)
    cube = apply_moves(cube, scramble)
    print_cube_state(cube)
    print("Scramble: ", end="")
    print_moves(scramble)
    print()

    # solve cube using solver_v1
    if solver == "1":
        print("Version 1 selected: Random Search")
        solution, attempts, time = solve_v1(cube, scramble_length)
        cube = apply_moves(cube, solution)
        print_cube_state(cube)
        print_moves(solution)
        print_solve_statistics(attempts, time)
        if solution == inverse_moves(reverse_moves(scramble)):
            print("Found the exact inverse scramble!")
        print()

    # solve cube using solver_v2
    if solver == "2":
        print("Version 2 selected: Iterative Deepening Depth First Search (IDDFS)")
        solution, attempts, time = solve_v2(cube)
        cube = apply_moves(cube, solution)
        print_cube_state(cube)
        print("Solution: ", end="")
        print_moves(solution)
        print_solve_statistics(attempts, time)
        if solution != inverse_moves(reverse_moves(scramble)):
            print("Found solution different to inverse scramble!")
        else:
            print("Inverse found.")
        print()

main()