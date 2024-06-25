import random

grid_len:int = 300

class Cell():
    def __init__(self, state: bool, position) -> None:
        self.state:bool = state
        self.position:int = position
        
    def __repr__(self) -> str:
        return f"state: {self.state}, pos: {self.position}"

class GameGrid():
    def __init__(self, grid: list|None = None) -> None:
        if grid is None:
            grid = random.choices((True, False), k=grid_len)
        self.grid = [Cell(state, pos) for pos, state in enumerate(grid)]

            
            
    def neighbors(self, cell: Cell) -> str:
        if cell.position == 0:
            left = '0'
            center = '1' if cell.state else '0'
            right = '1' if self.grid[1].state else '0'
            return left + center + right
        elif cell.position == grid_len - 1:
            left = '1' if self.grid[-2].state else '0'
            center = '1' if cell.state else '0'
            right = '0'
            return left + center + right
        
        left = '1' if self.grid[cell.position - 1].state else '0'
        center = '1' if cell.state else '0'
        right = '1' if self.grid[cell.position + 1].state else '0'
        return left + center + right
        
    
    def rule(self, cell: Cell) -> bool:
        key = self.neighbors(cell)
        rule_dict = {
            "000": 1,
            "001": 1,
            "010": 0,
            "011": 0,
            "100": 1,
            "101": 1,
            "110": 0,
            "111": 0
        }
        return bool(rule_dict[key])
    
    def step(self) -> list:
        new_grid = list()
        for cell in self.grid:
            new_cell = Cell(self.rule(cell), cell.position)
            new_grid.append(new_cell)
        self.grid = new_grid
        return new_grid
    



import pygame

size = 3
x_res = size * grid_len
y_res = size // 3 * 2 * grid_len

pygame.init()
screen = pygame.display.set_mode((x_res, y_res))
pygame.display.set_caption("Primitive Cellular Automata")
clock = pygame.time.Clock()

my_grid = GameGrid()
print(my_grid.grid)
screen.fill((255, 255, 255))
for count in range(y_res):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    for cell in my_grid.grid:
        if cell.state:
            pygame.draw.rect(screen, 
                             (0,0,0), 
                            (cell.position * size,
                             count * size,                            
                             size,
                             size))  # Отрисовка красного квадрата
    pygame.display.flip()  # Обновление экрана
    my_grid.step()
    clock.tick(10)

input()
pygame.quit()
