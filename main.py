import menu
import pygame


# pygame

pygame.init()

# Grid and layout settings
GRID_SIZE = 4
BLOCK_SIZE = 100
STREET_WIDTH = 40 
MARGIN = 50
CELL_SIZE = BLOCK_SIZE + STREET_WIDTH
CITY_WIDTH = GRID_SIZE * BLOCK_SIZE + (GRID_SIZE + 1) * STREET_WIDTH
WIDTH = HEIGHT = CITY_WIDTH + 2 * MARGIN

screen = pygame.display.set_mode((WIDTH, HEIGHT))

if __name__ == "__main__":
    menu.menu_loop()