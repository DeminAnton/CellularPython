from dataclasses import dataclass

@dataclass
class Config:
    grid_rows = 100
    grid_columns = 150
    scale = 4
    x_res = grid_columns * scale
    y_res = grid_rows * scale
    live_color = (0, 0, 0)
    death_color = (255, 255, 255)
    FPS = 50
    init_prob = 0.5
