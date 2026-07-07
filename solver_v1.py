from cube import *
from moves import generate_random_moves
from time import perf_counter
from solver import Solver

# Brute forces 6 random moves until it finds the solution. Takes a long time for any scrambles longer than 6 moves
class SolverV1(Solver):

    def __init__(self, cube: Cube, max_scramble_length: int = 6):
        super().__init__(cube)
        self.max_scramble_length = max_scramble_length


    @property
    def name(self):
        return "Brute Force - Random"

    def solve(self):
        start_time = perf_counter()

        found = False
        while True:
            for i in range(1, self.max_scramble_length + 1):
                test_cube = self.cube.copy()
                test_solution = generate_random_moves(i)
                test_cube.apply_moves(test_solution)
                self.attempts += 1
                if test_cube.is_solved():
                    self.solution = test_solution
                    found = True
                    break
            if found:
                break

        self.time = perf_counter() - start_time

        return self.solution, self.attempts, self.time