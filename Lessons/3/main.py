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
        if (row == 0) and (column == 0):
            pass # угловая
        elif (row == 0) and (column == Config.grid_columns - 1):
            pass # угловая
        
        elif ((row == Config.grid_rows - 1) and 
             (column == Config.grid_columns - 1)):
            pass
        
        elif ((row == Config.grid_rows - 1) and 
             (column == 0)):
            pass
        
        if (row == 0):
            pass
        elif (row == Config.grid_rows - 1):
            pass
        elif (column == 0):
            pass
        elif (column == Config.grid_columns - 1):
            pass
        
        neighbors_list.append(self.grid[row - 1][column - 1])
        neighbors_list.append(self.grid[row][column - 1])
        neighbors_list.append(self.grid[row + 1][column - 1])
        neighbors_list.append(self.grid[row - 1][column])
        neighbors_list.append(self.grid[row + 1][column])
        neighbors_list.append(self.grid[row - 1][column + 1])
        neighbors_list.append(self.grid[row][column + 1])
        neighbors_list.append(self.grid[row + 1][column + 1])
        
        
        
    
    def step(self):
        new_grid = self.grid.copy()
        for raw in self.grid():
            for cell in raw:
                