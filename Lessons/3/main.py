from grid import GameGrid, Cell
from config import Config

import pygame

pygame.init()
screen = pygame.display.set_mode((Config.x_res, Config.y_res))
pygame.display.set_caption("Game live")
clock = pygame.time.Clock()

my_grid = GameGrid()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Config.death_color)  # Заливка фона черным цветом
    for row in range(Config.grid_rows):
        for column in range(Config.grid_columns):
            cell: Cell =  my_grid.grid[row][column]
            if cell.state == True:
                pygame.draw.rect(screen, 
                                 Config.live_color, 
                                 (column * Config.scale,
                                  row * Config.scale,
                                  Config.scale,
                                  Config.scale))  # Отрисовка красного квадрата
    pygame.display.flip()  # Обновление экрана
    my_grid.step()

    clock.tick(Config.FPS)  # Ограничение до 60 FPS

pygame.quit()
