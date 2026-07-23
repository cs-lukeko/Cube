from abc import ABC, abstractmethod
from time import perf_counter

from cube import Cube

class Solver(ABC):
    def __init__(self, cube: Cube):
        self.cube = cube
        self.max_scramble_length = float('inf')
        self.solution = []
        self.attempts = 0
        self.time = 0.0

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod 
    def solve(self):
        pass

    def print_solve_statistics(self, attempts, time):
        print(f"Solutions attempted = {attempts:,}")
        print(f"Time taken: {(time):.3f}s")
        print()

    def animate(self, cube: Cube):
        solution_remaining = self.solution.copy()
        new_cube = cube.copy()

        times_per_second = 5
        interval = 1 / times_per_second
        next_time = perf_counter()
        while len(solution_remaining) > 0:
            current_time = perf_counter()
            if current_time >= next_time:
                new_cube.apply_moves([solution_remaining[0]])
                print(new_cube)
                print()
                solution_remaining = solution_remaining[1:]
                next_time += interval

    @abstractmethod
    def reconstruction(self):
        print("Reconstruction: ", end="")
        pass