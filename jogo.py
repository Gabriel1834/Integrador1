import main
import pygame
import random

pygame.init()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Fonte'
font = pygame.font.SysFont(None, 48)

# Comandos possíveis
commands = ["Vire à esquerda", "Vire à direita", "Vá para frente"]
keys_map = {
    "Vire à esquerda": pygame.K_LEFT,
    "Vire à direita": pygame.K_RIGHT,
    "Vá para frente": pygame.K_UP,
}

clock = pygame.time.Clock()
running = True


def show_message(message, color):
    text_surface = font.render(message, True, color)
    main.screen.blit(
        text_surface,
        (main.WIDTH // 2 - text_surface.get_width() // 2, main.HEIGHT // 2 + 100),
    )


def draw_challenge(command):
    main.screen.fill(BLACK)
    instruction = font.render(command, True, WHITE)
    main.screen.blit(
        instruction,
        (main.WIDTH // 2 - instruction.get_width() // 2, main.HEIGHT // 2 - 50),
    )
    pygame.display.flip()


def start_game():
    global running
    running = True
    while running:
        command = random.choice(commands)
        draw_challenge(command)
        waiting_input = True

        while waiting_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                elif event.type == pygame.KEYDOWN:
                    if event.key == keys_map[command]:
                        draw_challenge(command)
                        show_message("Parabéns, você acertou!", GREEN)
                    else:
                        draw_challenge(command)
                        show_message("Que pena, você errou!", RED)

                    pygame.display.flip()
                    pygame.time.delay(1500)
                    waiting_input = False

        clock.tick(60)

    pygame.quit()
