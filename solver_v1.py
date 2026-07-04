from cube import *
from moves import generate_random_moves
from time import perf_counter
from solver import Solver

# Brute forces 6 random moves until it finds the solution. Takes a long time for any scrambles longer than 6 moves
class SolverV1(Solver):

    def __init__(self, cube: Cube, scramble_length: int = 6, look_up_table: int = None):
        super().__init__(cube)
        self.scramble_length = scramble_length

    @property
    def name(self):
        return "Brute Force - Random"

    def solve(self):
        start_time = perf_counter()

        while True:
            test_cube = self.cube.copy()
            test_solution = generate_random_moves(self.scramble_length)
            test_cube.apply_moves(test_solution)
            self.attempts += 1
            if test_cube.is_solved():
                self.solution = test_solution
                break

        self.time = perf_counter() - start_time

        return self.solution, self.attempts, self.time