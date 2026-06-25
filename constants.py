AXES = {
    "U": "UD", "U'": "UD", "U2": "UD",
    "R": "RL", "R'": "RL", "R2": "RL",
    "F": "FB", "F'": "FB", "F2": "FB",
    "D": "UD", "D'": "UD", "D2": "UD",
    "L": "RL", "L'": "RL", "L2": "RL",
    "B": "FB", "B'": "FB", "B2": "FB"
}

MOVES = [
    "U", "U'", "U2", 
    "R", "R'", "R2", 
    "F", "F'", "F2", 
    "D", "D'", "D2", 
    "L", "L'", "L2", 
    "B", "B'", "B2"
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