from pickle import load
from constants import *
from cube import Cube
from scrambles import inverse_moves, reverse_moves
from solver import Solver
from time import perf_counter

# Uses IDDFS at each stage plus look_up_tables (from solved) to solve the final step.
# Solves in the following steps:
# EO using FULL_MOVESET
# BLDR (bottom-left 2x2x3 DR) using EO_MOVESET
# DR using RU_MOVESET
# Solved using DR_MOVESET
class SolverV5(Solver):
    eo_solution = []
    bldr_solution = []
    dr_solution = []
    end_solution = []

    @property
    def name(self):
        return "EO > BLDR > DR + Look-Up Tables"
    
    def solve(self):
        start_time = perf_counter()

        print("Loading database...")
        # Load solved datbase
        filename = DATABASES["dr_to_solved"]
        with open(filename, "rb") as file:
            solved_database = load(file)
        print(f"Database loaded: {filename}")

        # solve EO
        print("Solving EO...")
        eo_solution = None
        for depth in range(1, GODS_NUMBER + 1):
            print(f"Depth: {depth} - {(perf_counter() - start_time):.1f}s")
            result = self._depth_first_search(self.cube.copy(), depth, [], FULL_MOVESET, self._eo_solved)
            if result is not None:
                eo_solution = result
                self.eo_solution = eo_solution
                break
        eo_cube = self.cube.copy()
        eo_cube.apply_moves(eo_solution)
        print(f"EO found - {(perf_counter() - start_time):.1f}s - {" ".join(eo_solution)}\n")

        # solve bldr
        print("Solving BLDR...")
        bldr_solution = None
        for depth in range(1, GODS_NUMBER + 1):
            print(f"Depth: {depth} - {(perf_counter() - start_time):.1f}s")
            result = self._depth_first_search(eo_cube.copy(), depth, [], EO_MOVESET, self._bldr_solved)
            if result is not None:
                bldr_solution = result
                self.bldr_solution = bldr_solution
                break
        bldr_cube = eo_cube.copy()
        bldr_cube.apply_moves(bldr_solution)
        print(f"BLDR found - {(perf_counter() - start_time):.1f}s - {" ".join(bldr_solution)}\n")

        # solve DR
        print("Solving DR...")
        dr_solution = None
        for depth in range(1, GODS_NUMBER + 1):
            print(f"Depth: {depth} - {(perf_counter() - start_time):.1f}s")
            result = self._depth_first_search(bldr_cube.copy(), depth, [], RU_MOVESET, self._dr_solved)
            if result is not None:
                dr_solution = result
                self.dr_solution = dr_solution
                break
        dr_cube = bldr_cube.copy()
        dr_cube.apply_moves(dr_solution)
        print(f"DR found - {(perf_counter() - start_time):.1f}s - {" ".join(dr_solution)}\n")

        # search until a state in the look-up table is found
        print("Solving rest of cube...")
        end_solution = None
        for depth in range(1, GODS_NUMBER + 1):
            print(f"Depth: {depth} - {(perf_counter() - start_time):.1f}s")
            self._end_result = None
            result = self._depth_first_search(dr_cube.copy(), depth, [], DR_MOVESET, self._end_solved, solved_database)
            if result is not None:
                end_solution = self._end_result
                self.end_solution = end_solution
                break
        print(f"Solution found - {(perf_counter() - start_time):.1f}s - {" ".join(end_solution)}\n")

        self.solution = eo_solution + bldr_solution + dr_solution + end_solution
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
            test_cube = cube.copy()
            test_cube.apply_moves([move])
            result = self._depth_first_search(test_cube, depth_remaining - 1, moves_so_far + [move], moveset, is_solved, database)
            if result is not None:
                return result

        return None
    
    # "solved" state for EO
    def _eo_solved(self, cube, moves_so_far, database):
        return cube.is_eo_solved()

    # "solved" state for bldr
    def _bldr_solved(self, cube, moves_so_far, database):
        return cube.is_bldr_solved()

    # "solved" state for DR
    def _dr_solved(self, cube, moves_so_far, database):
        return cube.is_dr_solved()
    
    # "solved" state for rest of cube
    def _end_solved(self, cube, moves_so_far, database):
        if database is None:
            return False
        if tuple(cube.state) in database:
            db_solution = database[tuple(cube.state)]
            self._end_result = moves_so_far + inverse_moves(reverse_moves(db_solution))
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

    def reconstruction(self):
        super().reconstruction()
        print(f"({len(self.solution)} moves)\n")
        print(f"EO:    {" ".join(self.eo_solution)} ({len(self.eo_solution)} moves)")
        print(f"BLDR:  {" ".join(self.bldr_solution)} ({len(self.bldr_solution)} moves)")
        print(f"DR:    {" ".join(self.dr_solution)} ({len(self.dr_solution)} moves)")
        print(f"End:   {" ".join(self.end_solution)} ({len(self.end_solution)} moves)")