from dataclasses import dataclass

@dataclass
class Config:
    grid_rows = 40
    grid_columns = 80
    scale = 10
    x_res = grid_columns * scale
    y_res = grid_rows * scale
    live_color = (0, 0, 0)
    death_color = (255, 255, 255)
    FPS = 30
