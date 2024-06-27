from dataclasses import dataclass

@dataclass
class Config:
    grid_rows = 180
    grid_columns = 260
    scale = 4
    x_res = grid_columns * scale
    y_res = grid_rows * scale
    poison_energy = 10
    bacteria_energy = 5
    probs = [1 - 0.11, 0.05, 0.05, 0.01]