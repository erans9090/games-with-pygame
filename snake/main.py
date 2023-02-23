import pygame
from sys import exit
import properties
import ui
import logger

logger = logger.Logger() 
ui = ui.UI(logger)

ui.main_menu()


# set mode
# properties.hard()

clock = pygame.time.Clock()

ui.draw_food()

ui.draw_snake()

if properties.borders:
    ui.draw_borders()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            ui.update_direction(event.key)
    

    if ui.snake.gameover():
        ui.gameover()
        
    ui.is_food_eaten()
    ui.snake.move_snake()

    ui.draw_snake()
    ui.draw_food()
    if properties.borders:
        ui.draw_borders()
    

    pygame.display.update()
    ui.screen.fill(properties.background_color)

    clock.tick(properties.speed)


