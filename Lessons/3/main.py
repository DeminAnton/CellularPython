from config import Config

class Cell:
    def __init__(self, state = True):
        self.state = state
        
        
class GameGrid:
    def __init__(self) -> None:
        self.grid = [[Cell() for column in range(
                      Config.grid_columns)]
                      for row in range(Config.grid_rows)]
        
    def neighbors(self, coordinates: tuple) -> list:
        neighbors_list = []
        row, column = coordinates
        neighbors_coords_row = [row + i for i in range(-1, 2)]
        neighbors_coords_colomns = [column + i for i in range(-1, 2)]
        neighbors_coords = []
        for nrow in neighbors_coords_row:
            for ncolumn in neighbors_coords_colomns:
                if ((nrow >= 0 and nrow < Config.grid_rows) and
                    (ncolumn >= 0 and ncolumn < Config.grid_columns) and
                    (column != ncolumn or row != nrow)):
                    neighbors_coords.append((nrow,ncolumn))
        neighbors_list = [self.grid[i[0]][i[1]] for i in neighbors_coords]
        return neighbors_list
        
    
    def step(self):
        new_grid = self.grid.copy()
        for row in range(Config.grid_rows):
            for column in range(Config.grid_columns):
                neighbors_list: list[Cell] = self.neighbors((row, column))
                neighbors_list = [n.state for n in neighbors_list]
                living = sum(neighbors_list)
                if living == 3:
                    new_grid[row][column] = Cell(True)
                elif living == 2:
                    new_grid[row][column] = self.grid[row][column]
                else:
                    new_grid[row][column] = Cell(False)
        self.grid = new_grid
                
            
grid = GameGrid()
print(grid.neighbors((9,9)), "\n ", grid.neighbors((5, 3)))