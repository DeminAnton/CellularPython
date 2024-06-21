from config import Config
from random import choices

class Cell:
    def __init__(self, state = True, coords=(0,0)):
        self.state = state
        self.row, self.column = coords
    
    def __repr__(self):
        return f"({self.row}, {self.column}) - {self.state}"
        
        
class GameGrid:
    def __init__(self, grid: list | None = None) -> None:
        if grid is None:
            self.grid = [[Cell(choices((False, True),
                                       (1- Config.init_prob,
                                        Config.init_prob))[0], 
                               (row, column)) 
                          for column in range(Config.grid_columns)]
                          for row in range(Config.grid_rows)]
        else:
            self.grid = grid.copy()
        
    def neighbors(self, cell:Cell, region: int = 1) -> list:
        neighbors_list = []
        row, column = (cell.row, cell.column)
        neighbors_coords_row = [row + i for i in range(-region, region + 1) if 0 <= row + i < Config.grid_rows]
        neighbors_coords_colomns = [column + i for i in range(-region, region + 1) if 0 <= column + i < Config.grid_columns]
        for nrow in neighbors_coords_row:
            for ncolumn in neighbors_coords_colomns:
                if column != ncolumn or row != nrow:
                    neighbors_list.append(self.grid[nrow][ncolumn])
        return neighbors_list
    
    def rules(self, cell):
        neighbors: list[Cell] = self.neighbors(cell, 2)
        neighbors_state = [n.state for n in neighbors]
        living = sum(neighbors_state)
        if living == 3:
            return Cell(True, (cell.row, cell.column)) 
        elif living == 2:
            return Cell(cell.state, (cell.row, cell.column))
        return Cell(False, (cell.row, cell.column))

        
    
    def step(self):
        new_grid = []
        
        for cell_list in self.grid:
            cell_row = []
            for cell in cell_list:
                cell_row.append(self.rules(cell))
            new_grid.append(cell_row)
            
        self.grid = new_grid
        