from abc import ABC, abstractmethod

from cube import Cube

class Solver(ABC):
    def __init__(self, cube: Cube, scramble_length: int = None, look_up_table: int = None):
        self.cube = cube
        self.scramble_length = scramble_length
        self.look_up_table = look_up_table
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