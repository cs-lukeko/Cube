from cube import *
from moves import *
from scrambles import *
from solver_v1 import *

def main():
    # initialise cube
    cube = solved_cube

    # scramble cube
    scramble = generate_random_moves(6)
    cube = apply_moves(cube, scramble)
    print_cube_state(cube)
    print_moves(scramble)
    print()

    # solve cube
    solution, attempts, time = solve_v1(cube)
    cube = apply_moves(cube, solution)
    print_cube_state(cube)
    print_moves(solution)
    print_solve_statistics(attempts, time)
    if solution == inverse_moves(reverse_moves(scramble)):
        print("Found the exact inverse scramble!")
    print()

main()