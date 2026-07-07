AXES = {
    "U": "UD", "U'": "UD", "U2": "UD",
    "R": "RL", "R'": "RL", "R2": "RL",
    "F": "FB", "F'": "FB", "F2": "FB",
    "D": "UD", "D'": "UD", "D2": "UD",
    "L": "RL", "L'": "RL", "L2": "RL",
    "B": "FB", "B'": "FB", "B2": "FB"
}

FULL_MOVESET = [ # 18 moves total
    "U", "U'", "U2", 
    "R", "R'", "R2", 
    "F", "F'", "F2", 
    "D", "D'", "D2", 
    "L", "L'", "L2", 
    "B", "B'", "B2"
]

EO_MOVESET = [ # 14 moves total
    "U", "U'", "U2",
    "D", "D'", "D2",
    "R", "R'", "R2",
    "L", "L'", "L2",
    "F2",
    "B2"]

DR_MOVESET = [ # 10 moves total
    "U", "U'", "U2",
    "D", "D'", "D2",
    "R2",
    "L2",
    "F2",
    "B2"]

RU_MOVESET = [ # 6 moves total
    "U", "U'", "U2",
    "R", "R'", "R2"
    ]

FACES = ["U", "R", "F", "D", "L", "B"]

# ⬜🟥🟩🟨🟧🟦
SOLVED_CUBE = [
    "W", "W", "W", "W", "W", "W", "W", "W", "W", # U
    "R", "R", "R", "R", "R", "R", "R", "R", "R", # R
    "G", "G", "G", "G", "G", "G", "G", "G", "G", # F
    "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", # D
    "O", "O", "O", "O", "O", "O", "O", "O", "O", # L
    "B", "B", "B", "B", "B", "B", "B", "B", "B"  # B
    ]

GODS_NUMBER = 20

DATABASES = {
    "dr_to_solved": "look_up_tables/database_7_moves_dr_to_solved.pkl",
    "full_to_solved": "look_up_tables/database_5_moves_full_to_solved.pkl"
}