from dataclasses import dataclass


@dataclass
class Config:
    grid_rows = 180
    grid_columns = 260
    scale = 4
    x_res = grid_columns * scale
    y_res = grid_rows * scale
    poison_energy = 15
    bacteria_energy = 25
    probs = [1 - 0.8, 0.01, 0.05, 0.02]
    colors = {
        "empty":(255,255,255),
        "poison":(255, 0, 0),
        "plant":(0, 255, 0),
        "bacteria":(0, 0, 255)
    }
    FPS = 1
