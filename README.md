# Rubik's Cube Solver

A Python Rubik's cube simulator and solver, built as a learning project to explore search algorithms (DFS, IDDFS, meet-in-the-middle), and look-up tables. This program has been setup to use SolverV5 (the final implementation) only and all previous iterations can be considered obsolete.

## How to Run

1. Generate the look-up table as it is required to use SolverV5:

Create a sub-folder within the main folder called `look_up_tables/`, then run:
   ```bash
   python look_up_table_to_solved.py
   ```
   This writes `.pkl` files into a `look_up_tables/` folder. The file is approximately 108MB large.
2. Run the solver on a randomly scrambled cube:
   ```bash
   python main.py
   ```
   By default this runs `SolverV5` on a 20-move scramble and prints:
   - A move-by-move "animation" of the cube being solved (printed to the console at ~5 moves/second)
   - The scramble and solution used
   - Solve statistics (attempts, time taken)

3. To simulate an average of 5 (i.e. official speedcubing average) that truncates the best and worst of the 5 solves:

Create a sub-folder within the main folder called `benchmark_tests/`, then run:
   ```bash
   python benchmark_test_v2.py
   ```
   This saves the raw results to `benchmark_tests/benchmark_test_results.json` and a summary `benchmark_tests/benchmark_test_results.txt`. If you run the benchmark test multiple time, only the best average of 5 will be retained in the benchmark results files.

## Project Structure

| File | Purpose |
|---|---|
| `cube.py` | `Cube` class: holds the 54-sticker cube state, applies moves, checks solved/EO/BLDR/DR conditions, and displays the cube with coloured emoji. |
| `moves.py` | Defines every move as a pure function on a 54-element state list (face turns, wide turns, and whole-cube rotations), plus `generate_random_moves` for creating scrambles. |
| `constants.py` | Move sets (`FULL_MOVESET`, `EO_MOVESET`, `DR_MOVESET`, `RU_MOVESET`, etc.), axes groupings, the solved-state definition, and look-up table file paths. |
| `scrambles.py` | Helpers to reverse and invert a sequence of moves. |
| `solver.py` | Abstract `Solver` base class. Shared timing, stats printing, and the console "animation" playback. |
| `solver_v1.py` – `solver_v5.py` | Successive solver implementations (see below). |
| `look_up_table_to_solved.py` | Generates pickled look-up tables of cube states N moves from solved, via DFS. |
| `benchmark_test.py` / `benchmark_test_v2.py` | Ao5 benchmarking scripts; v2 adds JSON persistence and only keeps the best result per solver. |
| `main.py` | Entry point — scrambles a cube, solves it with a chosen solver, and plays back the solution. |

## Solver Versions

- **V1 — Brute Force (Random):** Repeatedly generates random move sequences of increasing length and checks if they solve the cube. Only viable for scrambles up to ~6 moves.
- **V2 — IDDFS:** Iterative deepening depth-first search over the full move set. Systematic rather than random, but still limited to short scrambles (~6 moves) before the search space becomes too large.
- **V3 — IDDFS + Look-Up Tables:** Same search as V2, but meets in the middle with a pre-computed look-up table of states near solved, roughly doubling the effective search depth reachable in reasonable time.
- **V4 — EO + DR + Look-Up Tables:** Breaks the solve into stages — edge orientation (EO), then domino reduction (DR), then a final look-up-table search — each solved independently via IDDFS on a progressively restricted move set. Again, only plausible for smaller scramble lengths.
- **V5 — EO → BLDR → DR + Look-Up Tables:** Refines V4 by adding an intermediate BLDR (bottom-left 2x2x3 domino reduction) stage between EO and DR, further restricting the move set at each stage (`FULL_MOVESET` → `EO_MOVESET` → `RU_MOVESET` → `DR_MOVESET`) so each search step stays fast even as the cube gets more complex. This is the current best-performing solver. Can handle any possible cube state and solve times range from 2.5 seconds to 90 seconds, although it averages around 10 seconds.

## Reflection

Overall I'm satisfied with where V5 has landed. My original goal for this project was to build a solver that could find a reasonably short solution to a scrambled cube within about 10 seconds (inspired by my personal best of around 11.5 seconds). After simulating a few competitions (Ao5s), the solver usually satisfies this goal with a Ao5 under 10 seconds and a move count under 30. The best Ao5 it did was 4.74 seconds.

## Potential Future Work

- Try different solving methods beyond the current staged approach — e.g. a full BLD (blindfolded) method, or corners-first / edges-first strategies. These probably wouldn't be faster or more efficient, but would be fun to play around with.
- Generate more look-up tables and search for EO/DR solutions on axes other than UD (the only axis currently used), potentially reducing solution length or search time.
- Add heuristics (e.g. pattern databases or a proper cost-to-go estimate) to move from plain IDDFS toward something closer to IDA*, which could meaningfully improve solve speed without changing the staged structure.
- Change the cube state from 54 stickers to 20 pieces which may improve performance.
- Implement partial solvers such as cross solutions, F2L+1 solutions, DR solutions, etc.