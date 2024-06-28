from gameframe import Grid, Config, Plant, Poison, Bacteria

import pygame

pygame.init()
screen = pygame.display.set_mode((Config.x_res, Config.y_res))
pygame.display.set_caption("Bactria wars")
clock = pygame.time.Clock()

my_grid = Grid()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Config.colors["empty"])  # Заливка фона черным цветом
    for row, cell_list in enumerate(my_grid.grid):
        for column, cell in enumerate(cell_list):
            if isinstance(cell, Poison):
                color = "poison"
            elif isinstance(cell, Plant):
                color = "plant"
            elif isinstance(cell, Bacteria):
                color = "bacteria"
            else:
                color = "empty"
            
            pygame.draw.rect(
                    screen,
                    Config.colors[color],
                    (
                        column * Config.scale,
                        row * Config.scale,
                        Config.scale,
                        Config.scale,
                    ),
                )  # Отрисовка красного квадрата
    pygame.display.flip()  # Обновление экрана
    my_grid.step()
    clock.tick(Config.FPS)

pygame.quit()
