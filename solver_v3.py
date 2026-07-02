from moves import apply_moves
from time import perf_counter
from constants import FULL_MOVESET, AXES, GODS_NUMBER
from pickle import load
from scrambles import reverse_moves, inverse_moves
from solver import Solver
from cube import Cube

class SolverV3(Solver):

    def __init__(self, cube: Cube, look_up_table: int):
        super().__init__(cube)
        self.look_up_table = look_up_table

    @property
    def name(self):
        return "IDDFS + Look-up Tables"

    def solve(self):
        start_time = perf_counter()

        filename = f"look_up_tables/database_{self.look_up_table}_away_from_solved.pkl"

        with open(filename, "rb") as file:
            database = load(file)

        for depth in range(1, GODS_NUMBER + 1):
            result = self._depth_first_search(self.cube.copy(), depth, [], database)
            if result is not None:
                self.solution = result
                break

        self.time = perf_counter() - start_time

        return self.solution, self.attempts, self.time

    def _depth_first_search(self, cube: Cube, depth_remaining: int, moves_so_far: list, database):    
        if tuple(cube.state) in database and depth_remaining == 0:
            database_solution = database[tuple(cube.state)]
            return moves_so_far + inverse_moves(reverse_moves(database_solution))

        if depth_remaining == 0:
            return None

        for move in FULL_MOVESET:
            if len(moves_so_far) >= 1:
                if move[0] == moves_so_far[-1][0]:
                    continue

            if len(moves_so_far) >= 2:
                if AXES[move] == AXES[moves_so_far[-1]] and AXES[move] == AXES[moves_so_far[-2]]:
                    continue

            self.attempts += 1
            test_cube = apply_moves(cube.copy(), [move])

            result = self._depth_first_search(test_cube, depth_remaining - 1, moves_so_far + [move], database)

            if result is not None:
                return result

        return None