# Rubik's Cube Solver

A Python Rubik's cube simulator and solver, built as a learning project to explore search algorithms (DFS, IDDFS, meet-in-the-middle), and look-up tables. 

## How to Run

1. Make sure you're using Python 3.12+ (required for f-string nested quotes used in some print statements).
2. No external dependencies are required — everything uses the standard library (`random`, `time`, `pickle`, `json`, `os`).
3. Generate the look-up tables before running any solver from v3 onwards, since they depend on pre-built databases:
   ```bash
   python look_up_table_to_solved.py
   ```
   This writes `.pkl` files into a `look_up_tables/` folder (e.g. `database_7_moves_dr_to_solved.pkl`, `database_5_moves_full_to_solved.pkl` — see `DATABASES` in `constants.py`). Table generation for higher depths can take a while and use a lot of memory/disk space.
4. Run the solver on a randomly scrambled cube:
   ```bash
   python main.py
   ```
   By default this runs `SolverV5` on a 20-move scramble and prints:
   - A move-by-move "animation" of the cube being solved (printed to the console at ~5 moves/second)
   - The scramble and solution used
   - Solve statistics (attempts, time taken)

   To change the solver or scramble length, edit the `solver_version` and `scramble_length` variables in `main.py`.
5. To benchmark a solver's performance (an Ao5 — average of 5 solves, discarding the best and worst), run:
   ```bash
   python benchmark_test_v2.py
   ```
   This runs `run_benchmark_test_ao5(solver_version, scramble_length)` and saves results to `benchmark_tests/benchmark_test_results.json`, keeping only the best result per solver (by scramble length, then by Ao5 time), and regenerates a human-readable `benchmark_tests/benchmark_test_results.txt` summary. Edit the function call at the bottom of the file to test a different solver or scramble length. (`benchmark_test.py` is the original, simpler version of this script, kept for reference.)

## Project Structure

| File | Purpose |
|---|---|
| `cube.py` | `Cube` class: holds the 54-sticker cube state, applies moves, checks solved/EO/BLDR/DR/cross conditions, and pretty-prints the cube with coloured emoji. |
| `moves.py` | Defines every move as a pure function on a 54-element state list (face turns, wide turns, and whole-cube rotations), plus `generate_random_moves` for creating scrambles. |
| `constants.py` | Move sets (`FULL_MOVESET`, `EO_MOVESET`, `DR_MOVESET`, `RU_MOVESET`, etc.), axis groupings, the solved-state definition, and look-up table file paths. |
| `scrambles.py` | Helpers to reverse and invert a sequence of moves (used to turn a lookup-table solution "back to solved" into a solution "back to scrambled"). |
| `solver.py` | Abstract `Solver` base class — shared timing, stats printing, and the console "animation" playback. |
| `solver_v1.py` – `solver_v5.py` | Successive solver implementations (see below). |
| `look_up_table_to_solved.py` | Generates pickled look-up tables of cube states N moves from solved, via DFS. |
| `benchmark_test.py` / `benchmark_test_v2.py` | Ao5 benchmarking scripts; v2 adds JSON persistence and only keeps the best result per solver. |
| `main.py` | Entry point — scrambles a cube, solves it with a chosen solver, and plays back the solution. |
| `Notes.txt` | Running roadmap and TODO list. |

## Solver Versions

- **V1 — Brute Force (Random):** Repeatedly generates random move sequences of increasing length and checks if they solve the cube. Only viable for scrambles up to ~6 moves.
- **V2 — IDDFS:** Iterative deepening depth-first search over the full move set. Systematic rather than random, but still limited to short scrambles (~6 moves) before the search space becomes too large.
- **V3 — IDDFS + Look-Up Tables:** Same search as V2, but meets in the middle with a pre-computed look-up table of states near solved, roughly doubling the effective search depth reachable in reasonable time.
- **V4 — EO + DR + Look-Up Tables:** Breaks the solve into stages — edge orientation (EO), then domino reduction (DR), then a final look-up-table search — each solved independently via IDDFS on a progressively restricted move set.
- **V5 — EO → BLDR → DR + Look-Up Tables:** Refines V4 by adding an intermediate BLDR (bottom-left 2x2x3 domino reduction) stage between EO and DR, further restricting the move set at each stage (`FULL_MOVESET` → `EO_MOVESET` → `RU_MOVESET` → `DR_MOVESET`) so each search step stays fast even as the cube gets more complex. This is the current best-performing solver.

## Reflection

Overall I'm satisfied with where V5 has landed. My original goal for this project was to build a solver that could reliably find a reasonably short solution to a scrambled cube within about 10 seconds, and V5's latest benchmark results meet that bar comfortably, so I don't have plans to push this particular approach (staged IDDFS + look-up tables) any further for now.

What I'm happy with:
- The staged approach (EO → BLDR → DR → look-up table) turned out to be a satisfying way to make an otherwise intractable search space tractable, and it was rewarding to see solve times drop dramatically between V2/V3 and V4/V5.
- The generic `_depth_first_search` helper in V4/V5, which takes a move set and a "solved" predicate as parameters, kept the staged solvers readable instead of repeating near-identical search code for every stage.
- The benchmarking setup (Ao5, best-single tracking, and now JSON persistence with "only keep improvements" logic in `benchmark_test_v2.py`) gave a clear, honest way to compare solver versions against each other.

What I'm less happy with:
- Solve times, while within my 10-second goal, are still slow compared to what proper heuristic search (e.g. IDA* with a good heuristic) could achieve — V5 still relies on brute-force IDDFS at each stage rather than anything smarter.
- The look-up tables only search outward from the solved state along the standard UD axis; there's no attempt to exploit symmetry or alternative axes, which likely leaves solve length and speed on the table.
- Some of the earlier exploration (e.g. using an LLM API as a solving backend) turned out to be a dead end compared to just using deterministic search/lookup methods, which was a useful but time-costly lesson.

## Potential Future Work

- Try different solving methods beyond the current staged approach — e.g. a full BLD (blindfolded) method, or corners-first / edges-first strategies — to compare structure and performance against the EO → BLDR → DR pipeline.
- Generate more look-up tables and search for EO/DR solutions on axes other than UD (the only axis currently used), potentially reducing solution length or search time.
- Add heuristics (e.g. pattern databases or a proper cost-to-go estimate) to move from plain IDDFS toward something closer to IDA*, which could meaningfully improve solve speed without changing the staged structure.
