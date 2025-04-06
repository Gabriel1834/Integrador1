import pygame

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
pygame.display.set_caption("4x4 City - Locked Street Movement")

# Colors
BUILDING_COLOR = (160, 160, 160)
STREET_COLOR = (60, 60, 60)
CAR_COLOR = (255, 0, 0)
BG_COLOR = (30, 30, 30)

# Car setup
car_size = 25
car_speed = 3

# Spawn on a vertical road (centered on first vertical column)
car_x = MARGIN + STREET_WIDTH // 2 - car_size // 2
car_y = MARGIN + STREET_WIDTH + BLOCK_SIZE // 2 - car_size // 2

clock = pygame.time.Clock()
running = True

# Store building rects for collision detection
building_rects = []

def draw_city():
    screen.fill(BG_COLOR)
    building_rects.clear()

    # Draw streets
    for row in range(GRID_SIZE + 1):
        for col in range(GRID_SIZE + 1):
            # Horizontal
            if col < GRID_SIZE:
                x = MARGIN + STREET_WIDTH + col * CELL_SIZE - STREET_WIDTH // 2
                y = MARGIN + row * CELL_SIZE
                pygame.draw.rect(screen, STREET_COLOR, (x, y, BLOCK_SIZE + STREET_WIDTH, STREET_WIDTH))
            # Vertical
            if row < GRID_SIZE:
                x = MARGIN + col * CELL_SIZE
                y = MARGIN + STREET_WIDTH + row * CELL_SIZE - STREET_WIDTH // 2
                pygame.draw.rect(screen, STREET_COLOR, (x, y, STREET_WIDTH, BLOCK_SIZE + STREET_WIDTH))

    # Draw buildings and save their rects
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = MARGIN + STREET_WIDTH + col * CELL_SIZE
            y = MARGIN + STREET_WIDTH + row * CELL_SIZE
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            building_rects.append(rect)
            pygame.draw.rect(screen, BUILDING_COLOR, rect)

def is_colliding(x, y):
    car_rect = pygame.Rect(x, y, car_size, car_size)

    # Check if touching a building
    for building in building_rects:
        if car_rect.colliderect(building):
            return True

    # Check if out of bounds
    if x < MARGIN or y < MARGIN or x + car_size > WIDTH - MARGIN or y + car_size > HEIGHT - MARGIN:
        return True

    return False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Save current position to try move
    new_x, new_y = car_x, car_y

    if keys[pygame.K_LEFT]:
        new_x -= car_speed
    if keys[pygame.K_RIGHT]:
        new_x += car_speed
    if keys[pygame.K_UP]:
        new_y -= car_speed
    if keys[pygame.K_DOWN]:
        new_y += car_speed

    # Draw city and check collision
    draw_city()
    if not is_colliding(new_x, new_y):
        car_x, car_y = new_x, new_y  # Update if no collision

    # Draw the car
    pygame.draw.rect(screen, CAR_COLOR, (car_x, car_y, car_size, car_size))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
