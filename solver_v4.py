from constants import AXES, GODS_NUMBER, MOVES
from cube import Cube
from moves import apply_moves
from solver import Solver
from time import perf_counter

class SolverV4(Solver):

    @property
    def name(self):
        return "EO-Line only"
    
    def solve(self):
        start_time = perf_counter()

        for depth in range(1, GODS_NUMBER + 1):
            result = self._depth_first_search(self.cube.copy(), depth, [])
            if result is not None:
                self.solution = result
                break

        self.time = perf_counter() - start_time
        return self.solution, self.attempts, self.time
    

    def _depth_first_search(self, cube: Cube, depth_remaining: int, moves_so_far: list):
        if cube.is_eo_solved() and cube.is_eo_line_solved():
            return moves_so_far

        if depth_remaining == 0:
            return None

        for move in MOVES:
            if len(moves_so_far) >= 1:
                if move[0] == moves_so_far[-1][0]:
                    continue

            if len(moves_so_far) >= 2:
                if AXES[move] == AXES[moves_so_far[-1]] and AXES[move] == AXES[moves_so_far[-2]]:
                    continue

            self.attempts += 1
            test_cube = apply_moves(cube.copy(), [move])

            result = self._depth_first_search(test_cube, depth_remaining - 1, moves_so_far + [move])

            if result is not None:
                return result

        return None