from pickle import load
from constants import AXES, DR_MOVESET, GODS_NUMBER, FULL_MOVESET, EO_MOVESET
from cube import Cube
from moves import apply_moves
from scrambles import inverse_moves, reverse_moves
from solver import Solver
from time import perf_counter

class SolverV4(Solver):

    def __init__(self, cube: Cube, look_up_table: int):
        super().__init__(cube)
        self.look_up_table = look_up_table

    @property
    def name(self):
        return "EO (using IDDFS) + DR (using IDDFS) + Look-Up Tables"
    
    def solve(self):
        start_time = perf_counter()

        filename = f"look_up_tables/database_{self.look_up_table}_away_from_solved_dr.pkl"
        with open(filename, "rb") as file:
            database = load(file)

        # solve EO
        eo_solution = None
        for depth in range(1, GODS_NUMBER + 1):
            result = self._depth_first_search(self.cube.copy(), depth, [], FULL_MOVESET, self._eo_solved)
            if result is not None:
                eo_solution = result
                break

        # solve DR
        eo_cube = apply_moves(self.cube.copy(), eo_solution)
        dr_solution = None
        for depth in range(1, GODS_NUMBER + 1):
            result = self._depth_first_search(eo_cube.copy(), depth, [], EO_MOVESET, self._dr_solved)
            if result is not None:
                dr_solution = result
                break

        # search until a state in the look-up table is found
        dr_cube = apply_moves(eo_cube, dr_solution)
        middle_solution = None
        for depth in range(1, GODS_NUMBER + 1):
            self._middle_result = None
            result = self._depth_first_search(dr_cube.copy(), depth, [], DR_MOVESET, self._middle_solved, database)
            if result is not None:
                middle_solution = self._middle_result
                break

        self.solution = eo_solution + dr_solution + middle_solution
        self._tidy_solution()
        self.time = perf_counter() - start_time
        return self.solution, self.attempts, self.time
    
    # generic dfs function, pass in the step "solved" condition and appropriate database and moveset
    def _depth_first_search(self, cube: Cube, depth_remaining: int, moves_so_far: list, moveset: list, is_solved, database=None):
        if is_solved(cube, moves_so_far, database):
            return moves_so_far

        if depth_remaining == 0:
            return None

        for move in moveset:
            if len(moves_so_far) >= 1:
                if move[0] == moves_so_far[-1][0]:
                    continue
            if len(moves_so_far) >= 2:
                if AXES[move] == AXES[moves_so_far[-1]] and AXES[move] == AXES[moves_so_far[-2]]:
                    continue

            self.attempts += 1
            result = self._depth_first_search(
                apply_moves(cube.copy(), [move]), depth_remaining - 1, moves_so_far + [move], moveset, is_solved, database
            )
            if result is not None:
                return result

        return None
    
    # "solved" state for EO
    def _eo_solved(self, cube, moves_so_far, database):
        return cube.is_eo_solved()
    
    # "solved" state for DR
    def _dr_solved(self, cube, moves_so_far, database):
        return cube.is_dr_solved()
    
    # "solved" state for rest of cube
    def _middle_solved(self, cube, moves_so_far, database):
        if database is None:
            return False
        if tuple(cube.state) in database:
            db_solution = database[tuple(cube.state)]
            self._middle_result = moves_so_far + inverse_moves(reverse_moves(db_solution))
            return True
        return False
    
    def _tidy_solution(self):
        tidy_solution = []
        for i in range(len(self.solution)):
            if i != 0 and self.solution[i][0] == self.solution[i - 1][0]:
                continue
            elif i == len(self.solution) - 1:
                tidy_solution.append(self.solution[i])
                continue
            elif self.solution[i][0] == self.solution[i + 1][0]:
                agg_move = 0
                # combine moves
                for j in range(i, i + 2):
                    if len(self.solution[j]) == 1:
                        agg_move += 1
                    elif self.solution[j][1] == "'":
                        agg_move -= 1
                    elif self.solution[j][1] == "2":
                        agg_move +=  2
                # append new move
                if agg_move == 0 or agg_move == 4:
                    pass
                elif agg_move == 1:
                    tidy_solution.append(self.solution[i][0])
                elif agg_move == 2 or agg_move == -2:
                    tidy_solution.append(self.solution[i][0] + "2")
                elif agg_move == 3 or agg_move == -1:
                    tidy_solution.append(self.solution[i][0] + "'")
            else:
                tidy_solution.append(self.solution[i])
        self.solution = tidy_solution