from abc import ABC, abstractmethod

class Solver(ABC):
    def __init__(self, cube):
        self.cube = cube
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