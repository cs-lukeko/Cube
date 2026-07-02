from cube import *
from moves import generate_random_moves, apply_moves
from time import perf_counter
from solver import Solver

# Brute forces 6 random moves until it finds the solution. Takes a long time for any scrambles longer than 6 moves
class SolverV1(Solver):

    def __init__(self, cube: Cube, scramble_length: int):
        super().__init__(cube)
        self.scramble_length = scramble_length

    @property
    def name(self):
        return "Brute Force - Random"

    def solve(self):
        start_time = perf_counter()

        while True:
            self.solution = generate_random_moves(self.scramble_length)
            test_cube = apply_moves(self.cube.copy(), self.solution)
            self.attempts += 1
            if test_cube.is_solved():
                end_time = perf_counter()
                break

        self.time = end_time - start_time

        return self.solution, self.attempts, self.time